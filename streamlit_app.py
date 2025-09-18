import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DocStream", layout="wide")

# --- Full HTML, CSS, JS Code ---
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DocStream - Netflix Style Document Manager</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
        }
        
        .hero-gradient {
            background: linear-gradient(to right, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0.5) 50%, rgba(0,0,0,0.1) 100%);
        }
        .document-card {
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .document-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        .upload-area {
            border: 2px dashed rgba(255,255,255,0.3);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            border-radius: 16px;
            backdrop-filter: blur(10px);
            background: rgba(20, 20, 20, 0.6);
        }
        .upload-area:hover {
            border-color: #e50914;
            background: rgba(229,9,20,0.15);
        }
        .feature-card {
            background: rgba(30, 30, 30, 0.6);
            border-radius: 16px;
            padding: 32px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }
        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(40, 40, 40, 0.8);
        }
        .nav-glass {
            backdrop-filter: blur(10px);
            background: rgba(0, 0, 0, 0.5);
        }
    </style>
</head>
<body class="bg-black text-white">
    <!-- Navbar -->
    <nav class="fixed top-0 w-full z-50 nav-glass px-6 py-4 border-b border-gray-800/50">
        <div class="flex justify-between items-center">
            <div class="flex items-center">
                <span class="text-red-600 font-bold text-3xl mr-2">DOC</span>
                <span class="text-white font-bold text-3xl">STREAM</span>
            </div>
            <div class="flex items-center space-x-6">
                <button class="text-white hover:text-gray-300">
                    <i data-feather="search"></i>
                </button>
                <button class="text-white hover:text-gray-300">
                    <i data-feather="bell"></i>
                </button>
                <div class="w-8 h-8 rounded bg-red-600 flex items-center justify-center">
                    <i data-feather="user" class="text-white"></i>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative h-screen flex items-center hero-gradient">
        <div class="absolute inset-0 bg-cover bg-center opacity-20" style="background-image: url('http://static.photos/minimal/1200x630/42');"></div>
        <div class="container mx-auto px-6 relative z-10" data-aos="fade-up">
            <h1 class="text-6xl font-bold mb-6 tracking-tight">Your Documents, <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-red-600 to-pink-500">Streamed</span> Securely</h1>
            <p class="text-xl mb-8 max-w-2xl text-gray-300">Upload, manage and extract information from your documents with our powerful AI tools. All in one modern interface.</p>
            
            <!-- Upload Area -->
            <div class="upload-area p-12 mb-8 cursor-pointer text-center" id="uploadArea">
                <i data-feather="upload" class="w-16 h-16 mx-auto text-gray-400 mb-6"></i>
                <h3 class="text-2xl font-semibold mb-3">Drag & Drop Your Documents Here</h3>
                <p class="text-gray-400 mb-6">or click to browse files</p>
                <input type="file" id="fileInput" class="hidden" multiple>
                <button class="bg-gradient-to-r from-red-600 to-pink-500 hover:from-red-700 hover:to-pink-600 text-white px-8 py-3 rounded-lg font-medium transition-all duration-300 transform hover:scale-105">Select Files</button>
            </div>

            <!-- Action Buttons (hidden by default) -->
            <div class="flex space-x-4 hidden" id="actionButtons">
                <button class="bg-red-600 hover:bg-red-700 text-white px-6 py-3 rounded-lg flex items-center">
                    <i data-feather="send" class="mr-2"></i> Send Documents
                </button>
                <button class="bg-gray-800 hover:bg-gray-700 text-white px-6 py-3 rounded-lg flex items-center">
                    <i data-feather="file-text" class="mr-2"></i> Extract Information
                </button>
            </div>
        </div>
    </section>

    <!-- Recent Documents Section -->
    <section class="py-16 bg-gray-900">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl font-bold mb-8">Recent Documents</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <div class="document-card bg-gray-800/50 backdrop-blur-sm" data-aos="fade-up">
                    <div class="h-40 bg-gray-700 flex items-center justify-center">
                        <i data-feather="file-text" class="w-12 h-12 text-gray-400"></i>
                    </div>
                    <div class="p-4">
                        <h3 class="font-semibold mb-2">Quarterly Report.pdf</h3>
                        <p class="text-gray-400 text-sm">Uploaded 2 days ago</p>
                    </div>
                </div>
                <div class="document-card bg-gray-800 rounded-lg overflow-hidden" data-aos="fade-up" data-aos-delay="100">
                    <div class="h-40 bg-gray-700 flex items-center justify-center">
                        <i data-feather="file-text" class="w-12 h-12 text-gray-400"></i>
                    </div>
                    <div class="p-4">
                        <h3 class="font-semibold mb-2">Contract.docx</h3>
                        <p class="text-gray-400 text-sm">Uploaded 1 week ago</p>
                    </div>
                </div>
                <div class="document-card bg-gray-800 rounded-lg overflow-hidden" data-aos="fade-up" data-aos-delay="200">
                    <div class="h-40 bg-gray-700 flex items-center justify-center">
                        <i data-feather="file-text" class="w-12 h-12 text-gray-400"></i>
                    </div>
                    <div class="p-4">
                        <h3 class="font-semibold mb-2">Invoice.xlsx</h3>
                        <p class="text-gray-400 text-sm">Uploaded 2 weeks ago</p>
                    </div>
                </div>
                <div class="document-card bg-gray-800 rounded-lg overflow-hidden" data-aos="fade-up" data-aos-delay="300">
                    <div class="h-40 bg-gray-700 flex items-center justify-center">
                        <i data-feather="file-text" class="w-12 h-12 text-gray-400"></i>
                    </div>
                    <div class="p-4">
                        <h3 class="font-semibold mb-2">Presentation.pptx</h3>
                        <p class="text-gray-400 text-sm">Uploaded 3 weeks ago</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="py-16 bg-black">
        <div class="container mx-auto px-6">
            <h2 class="text-3xl font-bold mb-12 text-center">Powerful Document Management</h2>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="feature-card text-center" data-aos="fade-up">
                    <div class="w-20 h-20 bg-gradient-to-r from-red-600 to-pink-500 rounded-full flex items-center justify-center mx-auto mb-6">
                        <i data-feather="upload" class="w-10 h-10 text-white"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-4">Easy Upload</h3>
                    <p class="text-gray-300">Drag and drop your documents or browse your files with our simple interface.</p>
                </div>
                <div class="text-center" data-aos="fade-up" data-aos-delay="100">
                    <div class="w-16 h-16 bg-red-600 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-feather="shield" class="w-8 h-8 text-white"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">Secure Storage</h3>
                    <p class="text-gray-400">Your documents are encrypted and stored securely in our cloud infrastructure.</p>
                </div>
                <div class="text-center" data-aos="fade-up" data-aos-delay="200">
                    <div class="w-16 h-16 bg-red-600 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i data-feather="zap" class="w-8 h-8 text-white"></i>
                    </div>
                    <h3 class="text-xl font-semibold mb-2">AI Extraction</h3>
                    <p class="text-gray-400">Extract key information automatically with our advanced AI technology.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900/80 backdrop-blur-sm py-12 border-t border-gray-800/50">
        <div class="container mx-auto px-6">
            <div class="flex flex-col md:flex-row justify-between">
                <div class="mb-8 md:mb-0">
                    <div class="flex items-center mb-4">
                        <span class="text-red-600 font-bold text-2xl mr-2">DOC</span>
                        <span class="text-white font-bold text-2xl">STREAM</span>
                    </div>
                    <p class="text-gray-400 max-w-xs">The Netflix-style document management platform for professionals.</p>
                </div>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-8">
                    <div>
                        <h4 class="text-white font-semibold mb-4">Company</h4>
                        <ul class="space-y-2">
                            <li><a href="#" class="text-gray-400 hover:text-white">About</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">Careers</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">Contact</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-white font-semibold mb-4">Resources</h4>
                        <ul class="space-y-2">
                            <li><a href="#" class="text-gray-400 hover:text-white">Help Center</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">API Docs</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">Community</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-white font-semibold mb-4">Legal</h4>
                        <ul class="space-y-2">
                            <li><a href="#" class="text-gray-400 hover:text-white">Privacy</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">Terms</a></li>
                            <li><a href="#" class="text-gray-400 hover:text-white">Security</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center">
                <p class="text-gray-400 mb-4 md:mb-0">© 2023 DocStream. All rights reserved.</p>
                <div class="flex space-x-6">
                    <a href="#" class="text-gray-400 hover:text-white"><i data-feather="twitter"></i></a>
                    <a href="#" class="text-gray-400 hover:text-white"><i data-feather="facebook"></i></a>
                    <a href="#" class="text-gray-400 hover:text-white"><i data-feather="linkedin"></i></a>
                    <a href="#" class="text-gray-400 hover:text-white"><i data-feather="instagram"></i></a>
                </div>
            </div>
        </div>
    </footer>

    <script>
        AOS.init({ duration: 800, easing: 'ease-in-out', once: true });
        feather.replace();

        document.getElementById('uploadArea').addEventListener('click', function() {
            document.getElementById('fileInput').click();
        });

        document.getElementById('fileInput').addEventListener('change', function(e) {
            if (e.target.files.length > 0) {
                document.getElementById('actionButtons').classList.remove('hidden');
                const uploadArea = document.getElementById('uploadArea');
                uploadArea.innerHTML = `
                    <i data-feather="check-circle" class="w-12 h-12 mx-auto text-green-500 mb-4"></i>
                    <h3 class="text-xl font-semibold mb-2">${e.target.files.length} File(s) Selected</h3>
                    <p class="text-gray-400 mb-4">Ready for processing</p>
                `;
                feather.replace();
            }
        });
    </script>
</body>
</html>
"""

# Render in Streamlit
components.html(html_code, height=2000, scrolling=True)
