<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shader Cache Coin - Aluminum Prime Mining Protocol</title>
    <meta name="description" content="Shader Cache Coin - A proof-of-work system that mines prime numbers from GPU shader caches. First phase: Aluminum Coin with 50 tables of 10M primes each.">
    <meta name="author" content="Eldho Philip Abraham">
    <meta name="keywords" content="shader cache, cryptocurrency, mining, prime numbers, proof-of-work, aluminum coin, CS2, NVIDIA">
    
    <!-- Open Graph / Social Media -->
    <meta property="og:title" content="Shader Cache Coin - Aluminum Prime Mining">
    <meta property="og:description" content="Mine primes from your GPU shader caches. 50 tables × 10M primes = 500M total primes.">
    <meta property="og:image" content="https://github.com/user-attachments/assets/8a965cc6-c3ba-4768-ac2b-2a6217ee9507">
    <meta property="og:type" content="website">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔨</text></svg>">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0f0f1a 100%);
            color: #e0e0e0;
            line-height: 1.6;
            min-height: 100vh;
        }

        /* Custom Cursor / Selection */
        ::selection {
            background: #00d4ff;
            color: #0a0a0a;
        }

        /* Header / Hero */
        .hero {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(0,212,255,0.1) 0%, rgba(9,9,121,0.2) 100%);
            border-bottom: 1px solid rgba(0,212,255,0.3);
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #00d4ff, #7b2ff7);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 30px rgba(0,212,255,0.3);
        }

        .hero .badge {
            display: inline-block;
            background: rgba(0,212,255,0.2);
            border: 1px solid #00d4ff;
            border-radius: 50px;
            padding: 0.5rem 1.5rem;
            font-size: 0.9rem;
            margin-top: 1rem;
            backdrop-filter: blur(10px);
        }

        .hero .aluminum-icon {
            font-size: 4rem;
            margin: 1rem 0;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        /* Stats / Metrics */
        .stats-container {
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            padding: 3rem 2rem;
            background: rgba(0,0,0,0.3);
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }

        .stat-card {
            background: rgba(10,10,20,0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1.5rem 2rem;
            text-align: center;
            min-width: 180px;
            border: 1px solid rgba(0,212,255,0.2);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            border-color: #00d4ff;
            box-shadow: 0 10px 30px rgba(0,212,255,0.1);
        }

        .stat-number {
            font-size: 2.5rem;
            font-weight: bold;
            color: #00d4ff;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #aaa;
        }

        /* Main Content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Sections */
        .section {
            background: rgba(15,15,25,0.6);
            backdrop-filter: blur(5px);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(255,255,255,0.05);
        }

        .section h2 {
            font-size: 1.8rem;
            margin-bottom: 1.5rem;
            border-left: 4px solid #00d4ff;
            padding-left: 1rem;
        }

        .section h3 {
            margin: 1.5rem 0 1rem 0;
            color: #00d4ff;
        }

        /* Code Blocks */
        pre {
            background: #0a0a0f;
            border-radius: 12px;
            padding: 1.5rem;
            overflow-x: auto;
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 0.85rem;
            line-height: 1.5;
            border: 1px solid rgba(0,212,255,0.2);
            margin: 1rem 0;
        }

        code {
            font-family: 'Fira Code', 'Courier New', monospace;
            background: rgba(0,212,255,0.1);
            padding: 0.2rem 0.4rem;
            border-radius: 6px;
            font-size: 0.85rem;
        }

        /* Tiers / Tables */
        .tiers-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 1.5rem;
        }

        .tier-card {
            background: linear-gradient(135deg, rgba(0,0,0,0.5), rgba(0,212,255,0.05));
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid rgba(0,212,255,0.2);
            transition: all 0.3s ease;
        }

        .tier-card.bronze { border-top: 4px solid #cd7f32; }
        .tier-card.silver { border-top: 4px solid #c0c0c0; }
        .tier-card.gold { border-top: 4px solid #ffd700; }

        .tier-card h3 {
            margin-top: 0;
        }

        .tier-price {
            font-size: 1.8rem;
            font-weight: bold;
            margin: 1rem 0;
        }

        .tier-price span {
            font-size: 0.9rem;
            color: #aaa;
        }

        /* Buttons */
        .btn-group {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin: 2rem 0;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.8rem 1.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
            border: none;
        }

        .btn-primary {
            background: linear-gradient(135deg, #00d4ff, #7b2ff7);
            color: white;
            box-shadow: 0 4px 15px rgba(0,212,255,0.3);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,212,255,0.4);
        }

        .btn-outline {
            background: transparent;
            border: 1px solid #00d4ff;
            color: #00d4ff;
        }

        .btn-outline:hover {
            background: rgba(0,212,255,0.1);
            transform: translateY(-2px);
        }

        /* Flow Diagram */
        .flow-diagram {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin: 2rem 0;
        }

        .flow-step {
            flex: 1;
            text-align: center;
            background: rgba(0,0,0,0.3);
            padding: 1rem;
            border-radius: 12px;
            min-width: 120px;
        }

        .flow-arrow {
            font-size: 2rem;
            color: #00d4ff;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 3rem 2rem;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 3rem;
            background: rgba(0,0,0,0.3);
        }

        .footer a {
            color: #00d4ff;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .stat-number { font-size: 1.8rem; }
            .flow-arrow { display: none; }
            .flow-step { margin-bottom: 1rem; }
            .section { padding: 1.5rem; }
        }

        /* Image placeholder / Banner */
        .banner-image {
            width: 100%;
            max-width: 800px;
            margin: 2rem auto;
            display: block;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
            border: 1px solid rgba(0,212,255,0.2);
        }

        /* Mining animation */
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .mining-status {
            animation: pulse 2s infinite;
        }
    </style>
</head>
<body>

    <!-- Hero Section -->
    <div class="hero">
        <div class="aluminum-icon">🔨</div>
        <h1>Shader Cache Coin</h1>
        <p style="font-size: 1.2rem; margin-bottom: 1rem;">Proof-of-Work Mining • Prime Number Protocol • Zero Waste</p>
        <div class="badge">
            ⚡ PHASE 1: ALUMINUM COIN • ACTIVE MINING ⚡
        </div>
    </div>

    <!-- Stats -->
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">50</div>
            <div class="stat-label">Tables per Bronze</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">10M</div>
            <div class="stat-label">Primes per Table</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">500M</div>
            <div class="stat-label">Total Primes</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">~300h</div>
            <div class="stat-label">Mining ETA (500M)</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">44MB</div>
            <div class="stat-label">RAM Usage</div>
        </div>
    </div>

    <div class="container">
        <!-- Image Banner -->
        <img class="banner-image" src="https://github.com/user-attachments/assets/8a965cc6-c3ba-4768-ac2b-2a6217ee9507" alt="Shader Cache Coin Architecture Diagram">
        
        <!-- About Section -->
        <div class="section">
            <h2>📖 What is Shader Cache Coin?</h2>
            <p><strong>Shader Cache Coin (SCC)</strong> is a novel proof-of-work system that mines prime numbers from existing GPU shader cache files. Instead of wasting energy on arbitrary hashing, SCC repurposes the shader caches generated by games like CS2, Valorant, and other modern titles.</p>
            <p style="margin-top: 1rem;">The protocol extracts 32-bit integers from cache binaries, tests them for primality using optimized algorithms, and assembles them into verifiable linked list tables. Each complete table contains <strong>10 million verified primes</strong>.</p>
            
            <h3>🔬 How It Works</h3>
            <div class="flow-diagram">
                <div class="flow-step">🎮 Play Games<br><small>(Generate Shader Caches)</small></div>
                <div class="flow-arrow">→</div>
                <div class="flow-step">📁 Scan Cache Files<br><small>NVIDIA/AMD/Steam</small></div>
                <div class="flow-arrow">→</div>
                <div class="flow-step">🔢 Extract 32-bit Ints<br><small>4-byte chunks</small></div>
                <div class="flow-arrow">→</div>
                <div class="flow-step">✅ Miller-Rabin Test<br><small>Primality Verification</small></div>
                <div class="flow-arrow">→</div>
                <div class="flow-step">🔗 Build Linked Lists<br><small>10M primes/table</small></div>
            </div>
        </div>

        <!-- Mining Tiers -->
        <div class="section">
            <h2>💰 Mining Tiers & Tokenomics</h2>
            <p>Shader Cache Coin operates on a tiered system based on table completion. Each tier represents a different level of mining commitment and reward potential.</p>
            
            <div class="tiers-grid">
                <div class="tier-card bronze">
                    <h3>🥉 BRONZE</h3>
                    <div class="tier-price">$5 <span>fixed ICO</span></div>
                    <p><strong>50 Tables</strong><br>500 Million Primes</p>
                    <p style="font-size: 0.85rem; color: #aaa;">~14-20 days mining</p>
                    <hr style="margin: 1rem 0; border-color: rgba(255,255,255,0.1);">
                    <small>✓ Entry Level</small><br>
                    <small>✓ Community Access</small>
                </div>
                <div class="tier-card silver">
                    <h3>🥈 SILVER (Q3 2026)</h3>
                    <div class="tier-price">$7 <span>fixed ICO</span></div>
                    <p><strong>75 Tables</strong><br>750 Million Primes</p>
                    <p style="font-size: 0.85rem; color: #aaa;">~21-30 days mining</p>
                    <hr style="margin: 1rem 0; border-color: rgba(255,255,255,0.1);">
                    <small>✓ Priority Mining</small><br>
                    <small>✓ Governance Rights</small>
                </div>
                <div class="tier-card gold">
                    <h3>🏆 GOLD (Q1 2027)</h3>
                    <div class="tier-price">$10 <span>fixed ICO</span></div>
                    <p><strong>100 Tables</strong><br>1 Billion Primes</p>
                    <p style="font-size: 0.85rem; color: #aaa;">~28-40 days mining</p>
                    <hr style="margin: 1rem 0; border-color: rgba(255,255,255,0.1);">
                    <small>✓ Lifetime Rewards</small><br>
                    <small>✓ NFT Badge</small>
                </div>
            </div>
        </div>

        <!-- Code Example -->
        <div class="section">
            <h2>💻 Quick Start & Installation</h2>
            <h3>Prerequisites</h3>
            <ul style="margin-left: 2rem; margin-bottom: 1rem;">
                <li>Python 3.6+</li>
                <li>NVIDIA/AMD GPU with shader cache files</li>
                <li>Any game that generates caches (CS2, Valorant, Apex, etc.)</li>
            </ul>
            
            <h3>Installation</h3>
            <pre><code># Clone the repository
git clone https://github.com/yourusername/shader-cache-coin.git
cd shader-cache-coin

# Run the Aluminum miner
python aluminum_miner.py --scan

# Mine from your largest cache file
python aluminum_miner.py "C:\Users\YourName\AppData\Local\NVIDIA\DXCache\*.nvph"</code></pre>

            <h3>Core Mining Algorithm (Python)</h3>
            <pre><code>def mine_from_file(filepath: str):
    """Extract primes from any binary file"""
    num_tables = 50
    primes_per_table = 10_000_000
    
    with open(filepath, 'rb') as f:
        while chunk := f.read(4):
            num = int.from_bytes(chunk, 'little')
            
            if is_prime_fast(num):
                current_table.append(num)
                
                if len(current_table) >= primes_per_table:
                    save_table(current_table)
                    print(f"✅ Table {table_id} COMPLETE!")
                    table_id += 1</code></pre>
        </div>

        <!-- Why Aluminum -->
        <div class="section">
            <h2>🔬 Why "Aluminum" for Phase 1?</h2>
            <p>Aluminum represents the perfect balance of <strong>accessibility and scarcity</strong>. Just as aluminum was once more precious than gold before refinement, Phase 1 SCC requires real computational work but remains achievable on consumer hardware.</p>
            <ul style="margin-left: 2rem; margin-top: 1rem;">
                <li>✅ <strong>Lightweight</strong> - Only 44MB RAM usage</li>
                <li>✅ <strong>Resumable</strong> - Save/load progress checkpoints</li>
                <li>✅ <strong>Verifiable</strong> - Each table can be independently audited</li>
                <li>✅ <strong>Cheat-proof</strong> - Miller-Rabin validation detects composite injections</li>
            </ul>
        </div>

        <!-- Performance Metrics -->
        <div class="section">
            <h2>📊 Performance Benchmarks</h2>
            <div class="tiers-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
                <div class="stat-card">
                    <div class="stat-number">~185/sec</div>
                    <div class="stat-label">Primes on i5 CPU</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">~500/sec</div>
                    <div class="stat-label">Primes on i9 CPU</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">35GB</div>
                    <div class="stat-label">Data for 50 Tables</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Resume Mining</div>
                </div>
            </div>
            <p style="margin-top: 1.5rem; text-align: center;" class="mining-status">⚡ Currently mining Aluminum Phase 1 - 50 tables target ⚡</p>
        </div>

        <!-- Call to Action -->
        <div class="btn-group">
            <a href="#" class="btn btn-primary">📥 Download Miner (v2.0)</a>
            <a href="#" class="btn btn-outline">📖 Read Whitepaper</a>
            <a href="#" class="btn btn-outline">🌐 Join Discord</a>
            <a href="#" class="btn btn-outline">📊 Leaderboard</a>
        </div>

        <!-- FAQ Preview -->
        <div class="section">
            <h2>❓ FAQ</h2>
            <details style="margin-bottom: 1rem;">
                <summary style="cursor: pointer; font-weight: bold; padding: 0.5rem;">What files can I mine from?</summary>
                <p style="margin-top: 0.5rem;">Any large binary file with high entropy works: NVIDIA DXCache (`.nvph`), Steam shader caches, game installers, video files, or backup archives.</p>
            </details>
            <details style="margin-bottom: 1rem;">
                <summary style="cursor: pointer; font-weight: bold; padding: 0.5rem;">Do I need a powerful GPU?</summary>
                <p style="margin-top: 0.5rem;">No! The current miner uses CPU only. GPU acceleration (CUDA) is planned for Phase 2.</p>
            </details>
            <details style="margin-bottom: 1rem;">
                <summary style="cursor: pointer; font-weight: bold; padding: 0.5rem;">How do I verify my mined tables?</summary>
                <p style="margin-top: 0.5rem;">Run `python aluminum_miner.py --verify` to check all 50 tables against Miller-Rabin primality tests.</p>
            </details>
            <details>
                <summary style="cursor: pointer; font-weight: bold; padding: 0.5rem;">Is this real cryptocurrency?</summary>
                <p style="margin-top: 0.5rem;">SCC is a proof-of-work system that could be tokenized. Phase 1 establishes the mining infrastructure; tokenomics and exchange listing are planned for Phase 2.</p>
            </details>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <p>© 2026 Shader Cache Coin Protocol</p>
        <p style="margin-top: 0.5rem; font-size: 0.85rem;">Developed by Eldho Philip Abraham, Kanayannur, Kerala</p>
        <p style="margin-top: 1rem;">
            <a href="#">GitHub</a> • 
            <a href="#">Documentation</a> • 
            <a href="#">License (MIT)</a> • 
            <a href="#">Security Report</a>
        </p>
        <p style="margin-top: 1rem; font-size: 0.75rem; color: #666;">
            Shader Cache Coin is a proof-of-concept project. Always verify mining software integrity.
        </p>
    </div>
</body>
</html>
