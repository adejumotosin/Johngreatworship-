import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="JohnGreat Music Audit",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2563EB;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #3B82F6;
    }
    .critical-metric {
        background-color: #FEF2F2;
        border-left: 4px solid #DC2626;
    }
    .good-metric {
        background-color: #F0FDF4;
        border-left: 4px solid #10B981;
    }
    .warning-metric {
        background-color: #FFFBEB;
        border-left: 4px solid #F59E0B;
    }
    .progress-bar {
        height: 20px;
        border-radius: 10px;
        background-color: #E5E7EB;
        margin: 10px 0;
    }
    .progress-fill {
        height: 100%;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-weight: bold;
        line-height: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for navigation
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'Executive Summary'

# Sidebar navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2694/2694989.png", width=100)
    st.title("JohnGreat Music Audit")
    st.markdown("---")
    
    sections = {
        "📊 Executive Summary": "Executive Summary",
        "🎵 Streaming Analysis": "Streaming Analysis",
        "📱 Social Media Audit": "Social Media Audit",
        "🔄 Conversion Analysis": "Conversion Analysis",
        "🎬 Content Quality": "Content Quality",
        "🔥 7 Critical Issues": "Critical Issues",
        "🎯 90-Day Action Plan": "Action Plan",
        "📈 KPIs & Metrics": "KPIs",
        "🚀 Recommendations": "Recommendations",
        "📋 Appendix": "Appendix"
    }
    
    for icon_label, section_name in sections.items():
        if st.button(icon_label, key=section_name, use_container_width=True):
            st.session_state.current_section = section_name

# Data for metrics
metrics_data = {
    'Current': {
        'spotify_listeners': 2,
        'instagram_followers': 33,
        'youtube_subscribers': 849,
        'tiktok_followers': 1,
        'facebook_followers': 3,
        'email_subscribers': 0,
        'total_streams': 1000,
        'content_quality': 9,
        'brand_consistency': 8,
        'audience_size': 1,
        'engagement': 2,
        'streaming_performance': 1
    },
    'Target 90-Day': {
        'spotify_listeners': 500,
        'instagram_followers': 300,
        'youtube_subscribers': 1000,
        'tiktok_followers': 500,
        'facebook_followers': 100,
        'email_subscribers': 100,
        'total_streams': 15000,
        'content_quality': 9,
        'brand_consistency': 9,
        'audience_size': 6,
        'engagement': 7,
        'streaming_performance': 6
    }
}

def create_progress_bar(current, target, color="#3B82F6"):
    progress = min(current / target * 100, 100) if target > 0 else 0
    return f"""
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress}%; background-color: {color};">
            {progress:.1f}%
        </div>
    </div>
    <div style="display: flex; justify-content: space-between; font-size: 0.9rem;">
        <span>Current: {current}</span>
        <span>Target: {target}</span>
    </div>
    """

# Executive Summary Section
if st.session_state.current_section == "Executive Summary":
    st.markdown('<h1 class="main-header">🎵 JohnGreat Music - Complete Social Media & Streaming Audit</h1>', unsafe_allow_html=True)
    st.markdown("### Strategic Brand Analysis & 90-Day Growth Plan")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Spotify Monthly Listeners", metrics_data['Current']['spotify_listeners'], 
                 f"Target: {metrics_data['Target 90-Day']['spotify_listeners']}")
    with col2:
        st.metric("Instagram Followers", metrics_data['Current']['instagram_followers'],
                 f"Target: {metrics_data['Target 90-Day']['instagram_followers']}")
    with col3:
        st.metric("YouTube Subscribers", metrics_data['Current']['youtube_subscribers'],
                 f"Target: {metrics_data['Target 90-Day']['youtube_subscribers']}")
    
    st.markdown("---")
    
    # Brand Health Score
    st.markdown('<h2 class="sub-header">📊 Brand Health Score: 3.2/10</h2>', unsafe_allow_html=True)
    
    scores = {
        'Content Quality': 9,
        'Brand Consistency': 8,
        'Audience Size': 1,
        'Engagement Rate': 2,
        'Streaming Performance': 1
    }
    
    weights = {
        'Content Quality': 0.2,
        'Brand Consistency': 0.15,
        'Audience Size': 0.25,
        'Engagement Rate': 0.2,
        'Streaming Performance': 0.2
    }
    
    # Calculate weighted score
    weighted_score = sum(scores[k] * weights[k] for k in scores)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        for category, score in scores.items():
            st.markdown(f"**{category}**: {score}/10")
            st.progress(score/10)
    
    with col2:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown(f"### Overall Score: {weighted_score:.1f}/10")
        st.markdown("**Status:** Critical Intervention Required")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # The Paradox
    st.markdown('<h2 class="sub-header">⚡ The Paradox</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
        st.markdown("### ✅ What's Present")
        st.markdown("""
        - Professional music production
        - Cinematic music videos
        - Consistent branding
        - Multi-platform distribution
        - Professional photography
        - Clear messaging
        - All infrastructure in place
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown("### ❌ What's Missing")
        st.markdown("""
        - Audience growth strategy
        - Paid advertising (£0 spent)
        - Community engagement
        - Playlist placements
        - Artist collaborations
        - Email list (owned audience)
        - Consistent posting schedule
        - Content strategy aligned with algorithms
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# Streaming Analysis Section
elif st.session_state.current_section == "Streaming Analysis":
    st.markdown('<h1 class="main-header">🎵 Streaming Performance Analysis</h1>', unsafe_allow_html=True)
    
    # Spotify Analysis
    st.markdown('<h2 class="sub-header">Spotify - The Core Crisis</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown("### 🎯 Monthly Listeners")
        st.markdown(f"# {metrics_data['Current']['spotify_listeners']}")
        st.markdown(f"**Target:** {metrics_data['Target 90-Day']['spotify_listeners']}")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown("### 📊 Total Streams")
        st.markdown(f"# < 1,000")
        st.markdown("**Target:** 15,000+")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown("### 🎵 Songs Released")
        st.markdown(f"# 2")
        st.markdown("**Period:** 8 months")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Song Performance
    st.markdown("### Song Performance")
    
    song_data = pd.DataFrame({
        'Song': ['Made Up My Mind (ft. FaithFave)', 'No One Like You'],
        'Release Date': ['June 15, 2025', 'September 2025'],
        'Estimated Streams': [650, 350],
        'Stream Range': ['400-700', '100-300'],
        'Status': ['Below Threshold', 'Below Threshold']
    })
    
    st.dataframe(song_data, use_container_width=True)
    
    # Critical Issues
    st.markdown("### Critical Issues Identified")
    
    issues = [
        "❌ **Algorithm Not Triggered**: Requires ~1,000 streams in first 28 days",
        "❌ **Zero Playlist Placements**: No editorial or algorithmic playlists",
        "❌ **No Pre-Save Campaign**: Songs dropped without preparation",
        "❌ **Conversion Crisis**: 0.23% YouTube → Spotify conversion (Industry: 5-15%)"
    ]
    
    for issue in issues:
        st.markdown(issue)
    
    # Competitive Benchmarking
    st.markdown('<h2 class="sub-header">Competitive Benchmarking</h2>', unsafe_allow_html=True)
    
    benchmark_data = pd.DataFrame({
        'Artist Profile': ['Established (3+ years)', 'Rising (1-2 years)', 'Early Stage (0-1 year)', 'JohnGreat (8 months)'],
        'Monthly Listeners': ['10,000-50,000', '1,000-10,000', '100-1,000', '2'],
        'Strategy': ['Consistent releases, playlist placements', 'Active social media, collaborations', 'Building from church community', 'Professional content, zero promotion']
    })
    
    st.dataframe(benchmark_data, use_container_width=True)

# Social Media Audit Section
elif st.session_state.current_section == "Social Media Audit":
    st.markdown('<h1 class="main-header">📱 Social Media Platform Audit</h1>', unsafe_allow_html=True)
    
    # Platform Overview
    st.markdown("### Platform Overview")
    
    platform_data = pd.DataFrame({
        'Platform': ['YouTube', 'Instagram', 'Facebook', 'TikTok', 'Twitter/X'],
        'Followers': [849, 33, 3, 1, 0],
        'Growth Rate': ['0.47/day', '0.14/day', '0.01/day', '0.01/day', '0/day'],
        'Engagement': ['142 views/video', '2-4 likes/post', '0-1 reactions', '123 views/video', '2-14 views/post'],
        'Status': ['Confused Identity', 'Newborn Account', 'Dead Platform', 'Missed Opportunity', 'Abandoned']
    })
    
    st.dataframe(platform_data, use_container_width=True)
    
    # YouTube Analysis
    st.markdown('<h2 class="sub-header">YouTube - The Confused Giant</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Content Breakdown
        - **Prayer/Ministry Videos:** 90-95% of content
          - Very low views: 50-300 each
          - Minimal thumbnails
          - 1-3 hour sessions
        
        - **Music Videos:** 5-10% of content
          - Higher views: 1,000-2,000
          - Professional production
          - 3-5 minutes
        """)
    
    with col2:
        st.markdown("""
        ### The Problem
        Music videos get **10-15× more views** than prayer content, 
        yet 90% of uploads are prayer videos.
        
        **Result:** Algorithm confusion, stalled growth
        """)
    
    # Recommendations
    st.markdown("### Recommendations")
    
    tab1, tab2, tab3 = st.tabs(["Option A: Two Channels", "Option B: Integrated Worship", "Option C: Music-First Hybrid"])
    
    with tab1:
        st.markdown("""
        ### Two-Channel Strategy
        - **JohnGreat Music** (Main): Music videos, Shorts, performances
        - **JohnGreat Ministry** (Secondary): Prayer sessions, devotionals
        
        **Pros:** Clear positioning, better algorithm optimization
        **Cons:** Double the management effort
        """)
    
    with tab2:
        st.markdown("""
        ### Integrated Worship Format
        - Transform prayer sessions into "Soaking Worship" experiences
        - Format: 15 min music → 30 min prayer → 15 min music
        - Market as "Worship & Prayer" not "Episode #X"
        
        **Pros:** Authentic to brand, unified audience
        **Cons:** Still algorithm-unfriendly format
        """)
    
    with tab3:
        st.markdown("""
        ### Music-First Hybrid (Recommended)
        - **70% music content** (videos, Shorts, performances)
        - **30% short devotionals** (5-10 min, not 1-3 hours)
        - Clear separation in playlists
        - Thumbnails distinguish content types
        
        **Pros:** Algorithm-friendly, maintains ministry aspect
        **Cons:** Requires content shift
        """)

# Conversion Analysis Section
elif st.session_state.current_section == "Conversion Analysis":
    st.markdown('<h1 class="main-header">🔄 Cross-Platform Conversion Analysis</h1>', unsafe_allow_html=True)
    
    # Conversion Funnel
    st.markdown("### The Broken Conversion Funnel")
    
    funnel_data = pd.DataFrame({
        'Stage': ['Discovery', 'Follow', 'Engage', 'Stream'],
        'Platform': ['All Social Media', 'Social Media', 'Social Media', 'Spotify'],
        'Current Count': [886, 886, '150-200', 2],
        'Conversion Rate': ['100%', '100%', '17-23%', '0.23%'],
        'Industry Standard': ['N/A', 'N/A', '20-40%', '5-15%']
    })
    
    st.dataframe(funnel_data, use_container_width=True)
    
    # Visual Funnel
    st.markdown("### Visual Conversion Funnel")
    
    fig = go.Figure(go.Funnel(
        y = ["Discovery (886)", "Followers (886)", "Engagers (~175)", "Streamers (2)"],
        x = [886, 886, 175, 2],
        textposition = "inside",
        textinfo = "value+percent initial",
        opacity = 0.65,
        marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA"]},
        connector = {"line": {"color": "royalblue", "width": 3}}
    ))
    
    fig.update_layout(title="Conversion Funnel Breakdown")
    st.plotly_chart(fig, use_container_width=True)
    
    # WhatsApp Dependency
    st.markdown('<div class="metric-card warning-metric">', unsafe_allow_html=True)
    st.markdown("### 📱 WhatsApp Dependency Problem")
    st.markdown("""
    **50% of YouTube traffic comes from WhatsApp**
    
    **What This Means:**
    - ✅ Shows core network (good foundation)
    - ❌ Network exhaustion (same people see everything)
    - ❌ No organic growth mechanism
    - ❌ Can't scale beyond immediate circle
    
    **Solution:** Convert WhatsApp network → Email list → Build beyond
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Content Quality Section
elif st.session_state.current_section == "Content Quality":
    st.markdown('<h1 class="main-header">🎬 Content Quality & Production Analysis</h1>', unsafe_allow_html=True)
    
    # Quality Scores
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
        st.markdown("### 🎵 Music Production")
        st.markdown("# 8.5/10")
        st.markdown("**Strengths:** Professional mixing, emotional delivery")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
        st.markdown("### 🎥 Visual Content")
        st.markdown("# 9/10")
        st.markdown("**Strengths:** Cinematic quality, consistent aesthetic")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
        st.markdown("### 📝 Copywriting")
        st.markdown("# 7.5/10")
        st.markdown("**Strengths:** Clear messaging, scripture integration")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # The Identity Tension
    st.markdown('<h2 class="sub-header">🎭 The Identity Tension</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### JohnGreat Music
        What social media says:
        - Gospel musician
        - Worship artist  
        - Contemporary sound
        - Music releases
        """)
    
    with col2:
        st.markdown("""
        ### JohnGreat Ministry
        What YouTube shows:
        - Prayer minister
        - "Praying with Jesus" series
        - Hour-long devotionals
        - Ministry content
        """)
    
    # Recommended Position
    st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
    st.markdown("### 🎯 Recommended Positioning")
    st.markdown("""
    **"Gospel worship artist and ministry leader - bringing worship and prayer together 
    through music and devotional content"**
    
    **How to Execute:**
    - YouTube: Integrate music INTO prayer content (soaking worship format)
    - Social Media: Lead with music, support with ministry messages
    - Streaming: Pure music focus
    - Ministry content: Shorter formats (5-10 min devotionals)
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Critical Issues Section
elif st.session_state.current_section == "Critical Issues":
    st.markdown('<h1 class="main-header">🔥 The 7 Critical Issues</h1>', unsafe_allow_html=True)
    
    issues = [
        {
            "title": "1. Content Confusion Crisis",
            "description": "YouTube identity split between music (10%) and prayer (90%) content",
            "impact": "Algorithm confusion, stalled growth at 0.47 subs/day",
            "solution": "Music-first hybrid strategy (70% music, 30% short devotionals)"
        },
        {
            "title": "2. Community Catastrophe", 
            "description": "Zero engagement across platforms (Instagram: following 4, TikTok: following 0)",
            "impact": "Invisible to gospel music community, no collaborations",
            "solution": "'30-30-30 Engagement Rule' - 30 min/day genuine engagement"
        },
        {
            "title": "3. Conversion Catastrophe",
            "description": "0.23% YouTube → Spotify conversion (Industry: 5-15%)",
            "impact": "849 YouTube subs = only 2 Spotify listeners",
            "solution": "Clear CTAs in videos, pinned comments, end screens"
        },
        {
            "title": "4. Collaboration Void",
            "description": "No cross-promotion, features, or community integration",
            "impact": "Missing gospel music's collaboration-driven growth",
            "solution": "Identify 5 UK gospel artists for collaboration outreach"
        },
        {
            "title": "5. Campaign Abandonment Pattern",
            "description": "Launch platforms → post 2-4 weeks → ghost → restart",
            "impact": "Algorithm penalty, harder each restart",
            "solution": "Content flywheel system + batch creation"
        },
        {
            "title": "6. £0 Budget Blindness",
            "description": "Confirmed £0 spent on paid advertising",
            "impact": "Beautiful content with zero reach",
            "solution": "Minimum £50/month budget for targeted growth"
        },
        {
            "title": "7. Email List Void",
            "description": "Zero owned audience (no email list)",
            "impact": "Completely dependent on social media algorithms",
            "solution": "Build email list with free worship guide lead magnet"
        }
    ]
    
    for i, issue in enumerate(issues):
        with st.expander(f"{issue['title']}", expanded=(i==0)):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Description:** {issue['description']}")
                st.markdown(f"**Impact:** {issue['impact']}")
            with col2:
                st.markdown(f"**Solution:** {issue['solution']}")
            
            # Progress tracking
            progress = st.slider(f"Progress on fixing {issue['title']}", 0, 100, 0, key=f"progress_{i}")
            st.progress(progress/100)

# Action Plan Section
elif st.session_state.current_section == "Action Plan":
    st.markdown('<h1 class="main-header">🎯 90-Day Action Plan</h1>', unsafe_allow_html=True)
    
    # Timeline Visualization
    st.markdown("### 📅 90-Day Timeline Overview")
    
    timeline_data = pd.DataFrame({
        'Month': ['Month 1: Foundation', 'Month 2: Momentum', 'Month 3: Scale'],
        'Focus': ['Stop the bleeding, fix foundations', 'Build community, increase streaming', 'Multiply what works, establish system'],
        'Budget': ['£50-100', '£100-150', '£150-200'],
        'Time Commitment': ['1-2 hours/day', '1-2 hours/day', '1-2 hours/day'],
        'Key Deliverables': ['All platforms reactivated, email list setup', 'First collaboration, playlist placements', '500+ monthly listeners, sustainable system']
    })
    
    st.dataframe(timeline_data, use_container_width=True)
    
    # Month 1 Detailed Plan
    st.markdown('<h2 class="sub-header">📋 Month 1: Foundation (Days 1-30)</h2>', unsafe_allow_html=True)
    
    weeks = [
        {
            "week": "Week 1: Emergency Fixes",
            "tasks": [
                "Day 1: Content audit & strategy session",
                "Day 2: YouTube emergency optimization",
                "Day 3: Instagram reactivation",
                "Day 4: TikTok resurrection",
                "Day 5: Email list setup",
                "Day 6: Facebook reactivation",
                "Day 7: Twitter/X revival"
            ]
        },
        {
            "week": "Week 2: Content & Engagement",
            "tasks": [
                "Daily 30-min engagement routine",
                "Batch content creation (3 new Reels)",
                "First email campaign launch",
                "Community engagement push",
                "Collaboration outreach (5 artists)"
            ]
        },
        {
            "week": "Week 3: Paid Promotion Launch",
            "tasks": [
                "Set up Instagram Reels ads (£30-40)",
                "Facebook ad campaign (£20)",
                "Organic content push support",
                "Email campaign #2",
                "Mid-campaign performance check"
            ]
        },
        {
            "week": "Week 4: Optimization & Momentum",
            "tasks": [
                "Content repurposing",
                "Collaboration follow-up",
                "First Instagram Live (30 min)",
                "Platform optimization round 2",
                "Month 1 review & Month 2 planning"
            ]
        }
    ]
    
    for week in weeks:
        with st.expander(week["week"], expanded=True):
            for task in week["tasks"]:
                st.markdown(f"- {task}")
    
    # Interactive Task Tracker
    st.markdown("### ✅ Task Completion Tracker")
    
    sample_tasks = [
        "YouTube thumbnails redesigned",
        "Instagram bio updated",
        "Email list setup complete",
        "First 7 Reels scheduled",
        "Collaboration outreach sent",
        "First ad campaign launched"
    ]
    
    for task in sample_tasks:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.markdown(task)
        with col2:
            status = st.selectbox(f"Status for {task}", ["Not Started", "In Progress", "Completed"], key=f"status_{task}")
        with col3:
            due_date = st.date_input(f"Due date for {task}", datetime.now() + timedelta(days=7), key=f"date_{task}")

# KPIs Section
elif st.session_state.current_section == "KPIs":
    st.markdown('<h1 class="main-header">📈 90-Day Key Performance Indicators</h1>', unsafe_allow_html=True)
    
    # Primary KPI
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 PRIMARY KPI: Spotify Monthly Listeners")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Starting Point", "2 listeners")
    with col2:
        st.metric("90-Day Target", "500 listeners")
    with col3:
        current = st.number_input("Current Progress", min_value=0, max_value=1000, value=2, key="current_listeners")
        progress = min(current / 500 * 100, 100)
        st.metric("Progress", f"{progress:.1f}%")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # KPI Dashboard
    st.markdown("### 📊 KPI Dashboard")
    
    kpis = [
        ("Spotify Monthly Listeners", 2, 500, current),
        ("Instagram Followers", 33, 300, 33),
        ("TikTok Followers", 1, 500, 1),
        ("Email Subscribers", 0, 100, 0),
        ("Total Streams (90 days)", 1000, 15000, 1000)
    ]
    
    for kpi_name, start, target, current_val in kpis:
        col1, col2, col3, col4 = st.columns([2, 1, 1, 3])
        with col1:
            st.markdown(f"**{kpi_name}**")
        with col2:
            st.markdown(f"Start: {start}")
        with col3:
            st.markdown(f"Target: {target}")
        with col4:
            progress = min(current_val / target * 100, 100) if target > 0 else 0
            st.progress(progress/100)
    
    # Success Assessment
    st.markdown("### 🎯 Success Assessment Guide")
    
    assessment_data = pd.DataFrame({
        'Result Range': ['500+ listeners', '300-499 listeners', '100-299 listeners', '50-99 listeners', '< 50 listeners'],
        'Assessment': ['🎉 TARGET EXCEEDED', '✅ STRONG PROGRESS', '🟡 MODERATE PROGRESS', '🟠 SLOW PROGRESS', '🔴 MINIMAL PROGRESS'],
        'Next Steps': ['Ready for next phase', 'On track, continue', 'Need strategy refinement', 'Major overhaul needed', 'Fundamental issues to address']
    })
    
    st.dataframe(assessment_data, use_container_width=True)

# Recommendations Section
elif st.session_state.current_section == "Recommendations":
    st.markdown('<h1 class="main-header">🚀 Post-90-Day Strategic Recommendations</h1>', unsafe_allow_html=True)
    
    # Scenario Planning
    st.markdown("### 📋 Scenario-Based Planning")
    
    scenario = st.selectbox(
        "Select expected 90-day outcome:",
        ["Target Achieved (500+ listeners)", "Moderate Progress (100-499 listeners)", "Minimal Progress (< 100 listeners)"]
    )
    
    if scenario == "Target Achieved (500+ listeners)":
        st.markdown('<div class="metric-card good-metric">', unsafe_allow_html=True)
        st.markdown("""
        ### Status: MOMENTUM ESTABLISHED ✅
        
        **Next 90 Days Focus:**
        1. **Scale What's Working:** Double down on best platforms
        2. **New Music Release:** Launch with full campaign
        3. **Monetization Preparation:** Playlist curator programs, sync licensing
        4. **Performance Opportunities:** Church bookings, virtual concerts
        
        **Target (Day 180):** 1,500-2,000 monthly listeners
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    elif scenario == "Moderate Progress (100-499 listeners)":
        st.markdown('<div class="metric-card warning-metric">', unsafe_allow_html=True)
        st.markdown("""
        ### Status: FOUNDATION LAID, REFINEMENT NEEDED 🟡
        
        **Next 90 Days Focus:**
        1. **Platform Optimization:** Master ONE promising platform first
        2. **Content Quality:** Reduce quantity, increase quality
        3. **Community Deepening:** Focus on 100 superfans
        4. **Collaboration Priority:** Feature on other artists' songs
        
        **Target (Day 180):** 500-1,000 monthly listeners
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        st.markdown('<div class="metric-card critical-metric">', unsafe_allow_html=True)
        st.markdown("""
        ### Status: FUNDAMENTAL STRATEGY REVISION REQUIRED 🔴
        
        **Root Cause Analysis Needed:**
        - Strategy isn't working? (different approach needed)
        - Execution inconsistent? (didn't follow plan)
        - Market fit issue? (music/positioning)
        
        **Strategic Pivot Options:**
        - Option A: Double down (if execution was issue)
        - Option B: Strategy overhaul (if plan was issue)
        - Option C: Hybrid approach (if budget was issue)
        
        **Target (Day 180):** 200-500 monthly listeners
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Top 5 Priorities
    st.markdown("### 🎯 Top 5 Priorities (Next 90 Days)")
    
    priorities = [
        ("1. Master ONE Platform", "Don't spread thin. Choose Instagram OR TikTok and become excellent there first."),
        ("2. Build Email List to 250+", "This becomes your career foundation for direct fan communication."),
        ("3. Secure 2-3 Meaningful Collaborations", "Features on other artists' songs for audience access."),
        ("4. Establish Content Flywheel", "Batch creation system for sustainable content production."),
        ("5. Hit 1,000 Monthly Listeners", "Milestone that unlocks algorithm engagement and opportunities.")
    ]
    
    for title, description in priorities:
        with st.expander(title, expanded=True):
            st.markdown(description)
            priority_status = st.select_slider(
                f"Priority status for {title}",
                options=["Not Started", "Planning", "In Progress", "Completed"],
                key=f"priority_{title}"
            )

# Appendix Section
elif st.session_state.current_section == "Appendix":
    st.markdown('<h1 class="main-header">📋 Appendix & Resources</h1>', unsafe_allow_html=True)
    
    # Content Ideas Bank
    st.markdown('<h2 class="sub-header">💡 Content Ideas Bank (50 Ideas)</h2>', unsafe_allow_html=True)
    
    tabs = st.tabs(["Music Content", "Testimony/Faith", "Behind-the-Scenes", "Engagement"])
    
    with tabs[0]:
        st.markdown("""
        ### Music Content (15 Ideas)
        1. Full song music video
        2. Acoustic version
        3. Piano-only instrumental
        4. Lyric video
        5. Behind-the-scenes recording session
        6. "How I wrote this song" story
        7. Song meaning breakdown
        8. Cover of popular gospel song
        9. Mashup/medley
        10. Live performance clip
        """)
    
    with tabs[1]:
        st.markdown("""
        ### Testimony/Faith Content (15 Ideas)
        1. Personal salvation story
        2. "Why I do music" testimony
        3. Season of struggle → God's faithfulness
        4. Scripture that inspires music
        5. Prayer moment
        6. Worship experience story
        7. "God moment" of the week
        8. Answered prayer share
        9. Faith challenge overcome
        10. Ministry moment
        """)
    
    with tabs[2]:
        st.markdown("""
        ### Behind-the-Scenes (10 Ideas)
        1. Morning routine
        2. Songwriting process
        3. Practice session
        4. Equipment tour
        5. Workspace setup
        6. Day in the life
        7. Collaboration session
        8. Photo shoot BTS
        9. Video shoot BTS
        10. "Real life" moments
        """)
    
    with tabs[3]:
        st.markdown("""
        ### Engagement/Community (10 Ideas)
        1. Q&A (ask me anything)
        2. Poll: "Which song should I cover?"
        3. "Comment your favorite worship song"
        4. Shoutout to supporters
        5. Duet challenge
        6. "Finish the lyrics" game
        7. Prayer request invitation
        8. Testimony share invitation
        9. "Tag someone who needs this"
        10. Collaboration callout
        """)
    
    # Tools & Resources
    st.markdown('<h2 class="sub-header">🛠️ Tools & Resources</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Free Tools
        **Content Creation:**
        - CapCut (video editing)
        - Canva (graphics)
        - InShot (quick mobile edits)
        
        **Scheduling:**
        - Later (30 posts free)
        - Buffer (10 posts free)
        - TikTok native scheduler
        
        **Email Marketing:**
        - Mailchimp (500 subscribers free)
        - ConvertKit (300 subscribers free)
        """)
    
    with col2:
        st.markdown("""
        ### Budget Templates
        
        **£50/Month Budget:**
        - Instagram Reels Ads: £35
        - Facebook Community Ads: £15
        → Expected: 30-50 new listeners
        
        **£100/Month Budget:**
        - Instagram: £50
        - TikTok: £30
        - YouTube: £20
        → Expected: 50-80 new listeners
        
        **£200/Month Budget:**
        - Instagram: £80
        - TikTok: £60
        - YouTube: £40
        - Retargeting: £20
        → Expected: 100-150 new listeners
        """)
    
    # Weekly Checklist
    st.markdown('<h2 class="sub-header">📅 Weekly Checklist Template</h2>', unsafe_allow_html=True)
    
    checklist_data = pd.DataFrame({
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Tasks': [
            'Plan week, schedule Reels, community engagement',
            'Post TikTok, respond to comments, engage with 10 artists',
            'YouTube check, email engagement, community engagement',
            'Post TikTok, Instagram Stories, playlist pitching',
            'Post TikTok, Facebook groups, analytics check',
            'Instagram Reel, deep community engagement, content creation',
            'REST or minimal engagement only, reflection'
        ]
    })
    
    st.dataframe(checklist_data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>JohnGreat Music Audit & Growth Plan • Prepared by Oluwatosin Adejumo • Audit Date: January 15, 2026</p>
    <p>This interactive dashboard provides the complete 90-day strategy to grow from 2 to 500+ monthly listeners.</p>
</div>
""", unsafe_allow_html=True)