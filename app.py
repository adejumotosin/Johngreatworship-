import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="JohnGreat Music - Strategic Audit & Growth Plan",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #8B4789;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #8B4789 0%, #D4A574 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-left: 4px solid #8B4789;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .action-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-left: 4px solid #ffc107;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-left: 4px solid #28a745;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .risk-box {
        background-color: #f8d7da;
        padding: 1.5rem;
        border-left: 4px solid #dc3545;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem;
        font-size: 1.1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎵 Navigation")
st.sidebar.markdown("**JohnGreat Music Audit**")
section = st.sidebar.radio(
    "Go to:",
    [
        "Executive Summary",
        "Streaming Performance", 
        "Social Media Audit",
        "Critical Issues",
        "90-Day Action Plan",
        "KPIs & Targets",
        "Content Strategy",
        "Budget Scenarios",
        "Email Marketing",
        "Quick Wins"
    ]
)

# Header
st.markdown('<div class="main-header">🎵 JohnGreat Music</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Strategic Social Media & Streaming Audit | 90-Day Growth Plan</div>', unsafe_allow_html=True)
st.markdown("**Prepared by:** Oluwatosin Adejumo (Social Media Manager)")
st.markdown("**Audit Date:** January 15, 2026 | **Audit Period:** June 2025 - January 2026 (8 months)")
st.divider()

# ============================================
# SECTION 1: EXECUTIVE SUMMARY
# ============================================
if section == "Executive Summary":
    st.header("I. Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card"><h2>3.2/10</h2><p>Brand Health Score</p></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card"><h2>2</h2><p>Spotify Monthly Listeners</p></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card"><h2>886</h2><p>Total Social Followers</p></div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card"><h2>< 1,000</h2><p>Streams Per Song</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("The Paradox: Professional Content, Zero Audience")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>✅ What's Present (Excellent Foundation)</h4>
        <ul>
        <li>Professional music production quality</li>
        <li>Cinematic music videos</li>
        <li>Consistent branding across platforms</li>
        <li>Multi-platform distribution (Spotify, Apple Music, YouTube, TIDAL)</li>
        <li>Professional photography and cover art</li>
        <li>Clear messaging and strong copywriting</li>
        <li>All infrastructure in place (Linktree, social profiles)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="risk-box">
        <h4>❌ What's Missing (Critical Gaps)</h4>
        <ul>
        <li>Audience growth strategy</li>
        <li>Paid advertising (£0 spent confirmed)</li>
        <li>Community engagement</li>
        <li>Playlist placements</li>
        <li>Collaboration with other artists</li>
        <li>Email list (owned audience)</li>
        <li>Consistent posting schedule</li>
        <li>Content strategy aligned with algorithms</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Brand Health Breakdown")
    
    health_data = {
        'Category': ['Content Quality', 'Brand Consistency', 'Audience Size', 'Engagement Rate', 'Streaming Performance'],
        'Score': [9, 8, 1, 2, 1],
        'Weight': [20, 15, 25, 20, 20],
        'Weighted Score': [1.8, 1.2, 0.25, 0.4, 0.2]
    }
    
    df_health = pd.DataFrame(health_data)
    
    fig = go.Figure(data=[
        go.Bar(
            x=df_health['Category'],
            y=df_health['Score'],
            marker=dict(
                color=df_health['Score'],
                colorscale=[[0, '#dc3545'], [0.5, '#ffc107'], [1, '#28a745']],
                cmin=0,
                cmax=10
            ),
            text=df_health['Score'],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Score: %{y}/10<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title="Brand Health Score Components (Out of 10)",
        yaxis_title="Score",
        xaxis_title="",
        height=400,
        yaxis=dict(range=[0, 10])
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>💡 Key Insight</h4>
    <p><strong>JohnGreat has a "distribution problem," not a "content quality problem."</strong></p>
    <p>The music is excellent. The visuals are professional. The branding is consistent. 
    What's missing is the STRATEGY to get it in front of people who would love it.</p>
    <p><strong>Solution:</strong> This 90-day plan provides that distribution strategy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Current State vs. Industry Benchmarks")
    
    benchmark_data = {
        'Metric': ['Spotify Monthly Listeners', 'Instagram Followers', 'Email Subscribers', 'Playlist Placements'],
        'JohnGreat (Current)': [2, 33, 0, 0],
        'Industry Minimum': [500, 500, 100, 5],
        'Gap': ['99.6% below', '93.4% below', '100% below', '100% below']
    }
    
    df_benchmark = pd.DataFrame(benchmark_data)
    st.dataframe(df_benchmark, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="action-box">
    <h4>🎯 90-Day Mission</h4>
    <p><strong>Transform JohnGreat from 2 listeners to 500+ monthly listeners while building sustainable growth systems.</strong></p>
    <p><strong>Primary Goals:</strong></p>
    <ul>
    <li>Increase Spotify monthly listeners: 2 → 500+ (250x growth)</li>
    <li>Grow Instagram following: 33 → 300+ (9x growth)</li>
    <li>Build email list: 0 → 100+ subscribers</li>
    <li>Establish content flywheel (sustainable system)</li>
    <li>Secure 2-3 artist collaborations</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 2: STREAMING PERFORMANCE
# ============================================
elif section == "Streaming Performance":
    st.header("II. Streaming Performance Analysis")
    
    st.markdown("""
    <div class="risk-box">
    <h3>🚨 Critical Crisis: 2 Monthly Listeners</h3>
    <p><strong>After 8 months of professional content and 2 single releases, JohnGreat has only 2 monthly Spotify listeners.</strong></p>
    <p>This is the #1 priority to fix.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Spotify Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Monthly Listeners", "2", help="Industry minimum: 500-1,000 for emerging artists")
        st.metric("Songs Released", "2", delta="Made Up My Mind, No One Like You")
    
    with col2:
        st.metric("Streams Per Song", "< 1,000", delta_color="off", help="After 7 months for Made Up My Mind")
        st.metric("Estimated Total Streams", "500-1,000", delta_color="off")
    
    with col3:
        st.metric("Playlist Placements", "0", delta_color="inverse")
        st.metric("Algorithm Engagement", "None", delta_color="inverse", help="Need 1,000+ streams to trigger")
    
    st.markdown("---")
    
    st.subheader("Competitive Benchmarking")
    
    comparison_data = {
        'Artist Stage': ['Established (3+ years)', 'Rising (1-2 years)', 'Early Stage (0-1 year)', 'JohnGreat (8 months)'],
        'Monthly Listeners': [25000, 5000, 500, 2],
        'Strategy': [
            'Playlist placements, church network, label support',
            'Active social media, collaborations, local performances',
            'Building from church community, organic growth',
            'Professional content, zero promotion'
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    
    fig = go.Figure(data=[
        go.Bar(
            x=df_comparison['Artist Stage'],
            y=df_comparison['Monthly Listeners'],
            marker_color=['#28a745', '#ffc107', '#17a2b8', '#dc3545'],
            text=df_comparison['Monthly Listeners'],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Listeners: %{y:,}<br><extra></extra>'
        )
    ])
    
    fig.update_layout(
        title="UK Gospel Artist Monthly Listeners by Stage",
        yaxis_title="Monthly Listeners (Log Scale)",
        yaxis_type="log",
        height=450
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("The Conversion Crisis: YouTube → Spotify")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Current Funnel (BROKEN):**
        
        ```
        849 YouTube subscribers
        ↓ (only 16.7% watch videos)
        142 regular viewers
        ↓ (CONVERSION BREAKS HERE)
        2 Spotify monthly listeners
        
        = 0.23% conversion rate
        ```
        """)
        
        st.markdown("""
        <div class="risk-box">
        <h4>Problem Identified</h4>
        <p><strong>849 subscribers should generate 42-127 listeners (5-15% conversion)</strong></p>
        <p>Current: 2 listeners = <strong>95% below minimum</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **What's Broken:**
        
        1. **No Clear CTAs in Videos**
           - Videos don't end with "Stream on Spotify"
           - No pinned comments with streaming links
           - No end screens linking to music
        
        2. **YouTube Content Confusion**
           - 90% prayer content (50-300 views)
           - 10% music content (1,000-2,000 views)
           - Subscribers don't know what to expect
        
        3. **No Email Reminder System**
           - Can't remind people when new music drops
           - One-time post, then forgotten
        """)
    
    st.markdown("---")
    
    st.subheader("Multi-Platform Streaming Presence")
    
    platforms = {
        'Platform': ['Spotify', 'Apple Music', 'YouTube Music', 'TIDAL', 'Amazon Music', 'Deezer'],
        'Status': ['✅ Active', '✅ Active', '✅ Active', '✅ Active', '✅ Likely', '✅ Likely'],
        'Est. Monthly Streams': [90, 50, 30, 10, 15, 5],
        'Note': ['2 listeners', 'Unknown metrics', 'Unknown', 'Unknown', 'Unknown', 'Unknown']
    }
    
    df_platforms = pd.DataFrame(platforms)
    st.dataframe(df_platforms, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>✅ Distribution is Correct</h4>
    <p>Music is accessible on ALL major platforms. The problem is NOT distribution infrastructure.</p>
    <p>The problem is <strong>PROMOTION</strong>. No one knows the music exists.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("90-Day Streaming Growth Roadmap")
    
    timeline_data = {
        'Day': [0, 30, 60, 90],
        'Target Listeners': [2, 50, 200, 500],
        'Strategy': ['Baseline', 'Fix conversion + paid ads', 'Playlist placements + collaboration', 'Scale what works']
    }
    
    df_timeline = pd.DataFrame(timeline_data)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df_timeline['Day'],
        y=df_timeline['Target Listeners'],
        mode='lines+markers',
        name='Target Growth',
        line=dict(color='#8B4789', width=4),
        marker=dict(size=12),
        fill='tozeroy',
        fillcolor='rgba(139, 71, 137, 0.2)'
    ))
    
    fig.add_hline(y=500, line_dash="dash", line_color="green", annotation_text="Industry Minimum")
    
    fig.update_layout(
        title="90-Day Spotify Listener Growth Trajectory",
        xaxis_title="Days",
        yaxis_title="Monthly Listeners",
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="action-box">
    <h4>🎯 How We'll Hit 500 Listeners</h4>
    <p><strong>Month 1 (2 → 50):</strong></p>
    <ul>
    <li>Fix YouTube→Spotify conversion (add CTAs, pinned comments, end screens)</li>
    <li>Launch email list (capture existing audience)</li>
    <li>Start paid ads (£50-100: Instagram/Facebook targeting gospel music fans)</li>
    <li>Pitch to 20 independent playlist curators</li>
    </ul>
    <p><strong>Month 2 (50 → 200):</strong></p>
    <ul>
    <li>Secure playlist placements (even small playlists help)</li>
    <li>Launch collaboration (cross-promote with another artist)</li>
    <li>Scale ads to £100-150/month</li>
    <li>Email list drives streams for existing songs</li>
    </ul>
    <p><strong>Month 3 (200 → 500):</strong></p>
    <ul>
    <li>Spotify algorithm starts working (Release Radar, Discover Weekly)</li>
    <li>Viral TikTok/Instagram Reel potential</li>
    <li>Collaboration releases (joint single if ready)</li>
    <li>Community word-of-mouth kicks in</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 3: SOCIAL MEDIA AUDIT
# ============================================
elif section == "Social Media Audit":
    st.header("III. Social Media Platform Audit")
    
    st.markdown("**Complete cross-platform analysis with actionable insights**")
    
    st.markdown("---")
    
    # Platform summary cards
    st.subheader("Platform Health Scores")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    platforms_health = [
        ("YouTube", 4.0, 849, "🟡"),
        ("Instagram", 2.0, 33, "🔴"),
        ("Facebook", 1.0, 3, "🔴"),
        ("TikTok", 1.0, 1, "🔴"),
        ("Twitter/X", 0.5, 0, "🔴")
    ]
    
    for col, (platform, score, followers, status) in zip([col1, col2, col3, col4, col5], platforms_health):
        with col:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': platform, 'font': {'size': 14}},
                gauge={
                    'axis': {'range': [None, 10]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 3], 'color': "#ffcccc"},
                        {'range': [3, 6], 'color': "#ffffcc"},
                        {'range': [6, 10], 'color': "#ccffcc"}
                    ],
                }
            ))
            fig.update_layout(height=200, margin=dict(l=10, r=10, t=40, b=10))
            st.plotly_chart(fig, use_container_width=True)
            st.caption(f"{status} {followers:,} followers")
    
    st.markdown("---")
    
    # Platform tabs
    platform_tabs = st.tabs(["📺 YouTube", "📸 Instagram", "🎬 TikTok", "📘 Facebook", "🐦 Twitter/X"])
    
    # YouTube Tab
    with platform_tabs[0]:
        st.subheader("YouTube: The Confused Giant")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Subscribers", "849", help="After nearly 5 years")
            st.metric("Total Videos", "181")
        
        with col2:
            st.metric("Avg Views/Video", "142", help="16.7% of subscribers watch")
            st.metric("Growth Rate", "0.47 subs/day")
        
        with col3:
            st.metric("Channel Age", "5 years", delta="Since March 2020")
            st.metric("Total Views", "25,793")
        
        st.markdown("---")
        
        st.markdown("""
        <div class="risk-box">
        <h4>🚨 Critical Issue: Content Identity Crisis</h4>
        <p><strong>The Problem:</strong> 90% of content is 1-3 hour prayer sessions (50-300 views each), 
        but 10% music content gets 10-15x more views (1,000-2,000 views)</p>
        <p><strong>Impact:</strong> YouTube algorithm doesn't know who to recommend the channel to. 
        Subscribers came for music, see prayer content → don't watch → algorithm stops promoting channel.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Content performance comparison
        content_performance = {
            'Content Type': ['Music Videos', 'Prayer Sessions (1-3 hours)', 'YouTube Shorts', 'Devotionals'],
            'Avg Views': [1500, 200, 350, 150],
            '% of Content': [10, 85, 3, 2],
            'Subscriber Engagement': ['High', 'Very Low', 'Medium', 'Low']
        }
        
        df_content = pd.DataFrame(content_performance)
        
        fig = go.Figure(data=[
            go.Bar(
                name='Avg Views',
                x=df_content['Content Type'],
                y=df_content['Avg Views'],
                marker_color='#8B4789',
                text=df_content['Avg Views'],
                textposition='outside'
            ),
            go.Bar(
                name='% of Content',
                x=df_content['Content Type'],
                y=df_content['% of Content'],
                marker_color='#D4A574',
                text=[f"{val}%" for val in df_content['% of Content']],
                textposition='outside',
                yaxis='y2'
            )
        ])
        
        fig.update_layout(
            title="YouTube Content Performance vs. Effort Allocation",
            barmode='group',
            height=400,
            yaxis=dict(title='Average Views'),
            yaxis2=dict(title='% of Content', overlaying='y', side='right'),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solutions</h4>
        <p><strong>Option A (Recommended): Music-First Hybrid</strong></p>
        <ul>
        <li>70% music content (videos, Shorts, performances)</li>
        <li>30% short devotionals (5-10 min, not 1-3 hours)</li>
        <li>OR: Integrate music INTO prayer (soaking worship format)</li>
        </ul>
        <p><strong>Quick Wins (Week 1):</strong></p>
        <ul>
        <li>Redesign 10 music video thumbnails (emotion-led + text)</li>
        <li>Rewrite 10 titles (SEO-optimized: "Gospel Worship Song About...")</li>
        <li>Add pinned comments: "🎧 Stream on Spotify → [link]"</li>
        <li>Add end screens (Subscribe + Spotify link)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Instagram Tab
    with platform_tabs[1]:
        st.subheader("Instagram: The Newborn Account")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Followers", "33", help="After 8 months")
        
        with col2:
            st.metric("Following", "4", help="Not engaging with community")
        
        with col3:
            st.metric("Total Posts", "8", delta="~1 post/month")
        
        with col4:
            st.metric("Account Age", "8 months", delta="Created June 2025")
        
        st.markdown("---")
        
        # Historical metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**30-Day Historical Performance (Peak Period):**")
            historical_data = {
                'Metric': ['Views', 'Profile Visits', 'Link Taps', 'Saves'],
                'Value': [1662, 88, 1, 2],
                'Trend': ['-57.7%', '-43.2%', '0.06% conv', 'Low utility']
            }
            df_hist = pd.DataFrame(historical_data)
            st.dataframe(df_hist, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("**Best Performing Content:**")
            best_posts = {
                'Post': ['Staircase/outdoor piano', 'Music video teaser', 'Spotify player graphic'],
                'Engagement': ['100 likes, 1 comment', '1,887 views (Reel)', '263 views (Reel)']
            }
            df_best = pd.DataFrame(best_posts)
            st.dataframe(df_best, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="risk-box">
        <h4>🚨 Critical Issues</h4>
        <ol>
        <li><strong>Catastrophic Conversion:</strong> 1,662 views → 1 link tap = 0.06% (industry: 1-3%)</li>
        <li><strong>Save Rate Crisis:</strong> 2 saves vs 200+ likes = 1:100 ratio (should be 1:10)</li>
        <li><strong>Algorithm Penalty:</strong> Views declined 57.7% → algorithm deprioritizing account</li>
        <li><strong>Posting Inconsistency:</strong> 8 posts in 8 months, then abandoned</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Instagram Growth Strategy</h4>
        <p><strong>Content Formula (Post Daily):</strong></p>
        <ul>
        <li>1 Reel/day (30-60 sec worship moments, behind-the-scenes, testimonies)</li>
        <li>3-5 Stories/day (personal, relatable, Q&A)</li>
        <li>Framework posts (1/week): "5 Scripture-Based Worship Tips" (carousel)</li>
        </ul>
        <p><strong>Engagement Strategy (30 min/day):</strong></p>
        <ul>
        <li>Follow 20 UK gospel artists</li>
        <li>Comment on 10 gospel music posts (genuine engagement)</li>
        <li>Respond to ALL comments within 1 hour</li>
        </ul>
        <p><strong>Paid Ads (£30-50/month if budget available):</strong></p>
        <ul>
        <li>Boost best-performing Reels</li>
        <li>Target: UK, 18-45, Gospel Music interests</li>
        <li>Expected: 30-50 new followers/month</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # TikTok Tab
    with platform_tabs[2]:
        st.subheader("TikTok: The Missed Opportunity")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Followers", "1", help="After months of existence", delta_color="inverse")
        
        with col2:
            st.metric("Following", "0", help="Zero community engagement")
        
        with col3:
            st.metric("Total Likes", "5", help="Across ALL videos")
        
        st.markdown("---")
        
        video_performance = {
            'Video': ['Performance clip', 'Music video clip', 'Spotify promo', 'Blue abstract', 'Golden lights', 'Piano outdoor'],
            'Views': [184, 166, 127, 120, 136, 7],
            'Status': ['Best', 'Good', 'OK', 'OK', 'OK', 'Critical']
        }
        
        df_tiktok = pd.DataFrame(video_performance)
        
        fig = px.bar(
            df_tiktok,
            x='Video',
            y='Views',
            color='Views',
            color_continuous_scale='purples',
            text='Views'
        )
        
        fig.update_traces(textposition='outside')
        fig.update_layout(
            title="TikTok Video Performance (All-Time)",
            height=350,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
        <h4>💡 TikTok Reality for Gospel Musicians in 2026</h4>
        <p>TikTok is THE platform for gospel music discovery. Artists with 0 followers routinely get 50K+ views if content hits.</p>
        <p><strong>Why JohnGreat Failed:</strong></p>
        <ul>
        <li>Wrong content format (posting music video clips instead of TikTok-native content)</li>
        <li>Zero community engagement (following 0 people = invisible)</li>
        <li>Inconsistent posting (~6 videos total, need 1-3/day)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="action-box">
        
        <h4>✅ TikTok Revival Strategy</h4>
        <p><strong>Viral Formula (Test 10 variations):</strong></p>
        <ol>
        <li><strong>Testimony Hook:</strong> "I was going through [relatable struggle]...then this song came on [emotion]"</li>
        <li><strong>POV Videos:</strong> "POV: You finally surrender to God" + worship audio</li>
        <li><strong>Worship Challenge:</strong> Duet trending worship sounds</li>
        <li><strong>Behind-the-Scenes:</strong> Quick studio/clips showing song creation</li>
        <li><strong>Raw Worship:</strong> Unedited worship moments (30-60 sec)</li>
        </ol>
        <p><strong>30-Day TikTok Resurrection:</strong></p>
        <ul>
        <li>Post 1 TikTok/day for 30 days (15-30 seconds each)</li>
        <li>Use trending sounds (gospel, worship, Christian)</li>
        <li>Engage: Follow 50 gospel artists, comment on 20 videos/day</li>
        <li>Expected: 100-500 followers in 30 days</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Facebook Tab
    with platform_tabs[3]:
        st.subheader("Facebook: The Ghost Town")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Page Followers", "3", help="After 8 months")
        
        with col2:
            st.metric("Page Likes", "2", help="Essentially inactive")
        
        with col3:
            st.metric("Ad Spending", "£0", help="No Facebook ads run")
        
        st.markdown("---")
        
        st.markdown("""
        <div class="risk-box">
        <h4>🚨 Why Facebook Failed</h4>
        <ul>
        <li><strong>Wrong Content Strategy:</strong> Posting music to 3 followers = talking to empty room</li>
        <li><strong>No Community Leverage:</strong> Not active in gospel music Facebook groups</li>
        <li><strong>Wrong Format:</strong> Facebook rewards video (Live, Reels) not static posts</li>
        <li><strong>No Events:</strong> Missing virtual album launches, worship nights</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Current Post Performance:**")
            facebook_posts = {
                'Post': ['Song announcement', 'Reel teaser', 'Made Up My Mind video'],
                'Engagement': ['0 reactions, 0 comments', '0 reactions, 0 comments', '2 comments']
            }
            df_fb = pd.DataFrame(facebook_posts)
            st.dataframe(df_fb, use_container_width=True, hide_index=True)
        
        with col2:
            st.markdown("**Gospel Groups Opportunity:**")
            st.markdown("""
            **Active UK Gospel Facebook Groups:**
            - Gospel Music Lovers (500K+ members)
            - UK Christian Music (200K+ members)
            - African Gospel Music Worldwide (300K+ members)
            - Gospel Music Artists Network (50K+ members)
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Facebook Resurrection Plan</h4>
        <p><strong>Month 1 Strategy:</strong></p>
        <ol>
        <li><strong>Join 5 Gospel Groups:</strong> Gospel Music Lovers, UK Christian Music, etc.</li>
        <li><strong>Engage Daily:</strong> Comment on 5 posts/day in groups (genuine engagement)</li>
        <li><strong>Content Format:</strong>
            - Facebook Live (30 min worship sessions)
            - Facebook Reels (repurpose Instagram content)
            - Event creation (virtual album listening)</li>
        <li><strong>Target:</strong> 50 followers in 30 days (from group engagement)</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

    # Twitter/X Tab
    with platform_tabs[4]:
        st.subheader("Twitter/X: The Abandoned Outpost")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Followers", "0", help="After 8 months")
        
        with col2:
            st.metric("Following", "1", help="Essentially inactive")
        
        with col3:
            st.metric("Total Posts", "3", help="All in July 2025, then silent")
        
        st.markdown("---")
        
        tweet_performance = {
            'Tweet': ['Birthday + song announcement', 'Music video promo', 'Scripture + promo'],
            'Views': [14, 4, 2],
            'Engagement': ['0 likes, 0 retweets', '0 likes, 0 retweets', '0 likes, 0 retweets']
        }
        
        df_tweets = pd.DataFrame(tweet_performance)
        st.dataframe(df_tweets, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="insight-box">
        <h4>💡 Twitter/X for Gospel Artists</h4>
        <p>Twitter is the <strong>#1 platform for connecting with other artists, curators, and industry</strong>.</p>
        <p><strong>What JohnGreat Missed:</strong></p>
        <ul>
        <li>#GospelMusic trending conversations</li>
        <li>#WorshipWednesday community</li>
        <li>Playlist curators actively searching for new music</li>
        <li>Networking with other UK gospel artists</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Twitter/X Revival Strategy</h4>
        <p><strong>Daily Routine (15 min/day):</strong></p>
        <ul>
        <li><strong>Follow:</strong> 20 UK gospel artists, 10 playlist curators, 5 gospel blogs</li>
        <li><strong>Engage:</strong> Comment on 5 gospel music tweets/day</li>
        <li><strong>Post:</strong> 1 tweet/day (song snippet, behind-the-scenes, scripture)</li>
        <li><strong>Join:</strong> #WorshipWednesday, #GospelMusic, #NewMusicFriday conversations</li>
        </ul>
        <p><strong>Target:</strong> 50 followers in 30 days (from networking)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Cross-Platform Strategy Summary")
    
    strategy_matrix = {
        'Platform': ['YouTube', 'Instagram', 'TikTok', 'Facebook', 'Twitter/X'],
        'Priority': ['Medium', 'High', 'High', 'Low', 'Medium'],
        'Time/Day': ['20 min', '30 min', '20 min', '10 min', '10 min'],
        'Focus': ['Fix conversion, content strategy', 'Daily Reels, community building', 'Viral content, daily posting', 'Group engagement, Live events', 'Networking, curator relationships'],
        '30-Day Target': ['+20 subs', '+50 followers', '+100 followers', '+50 followers', '+50 followers']
    }
    
    df_strategy = pd.DataFrame(strategy_matrix)
    st.dataframe(df_strategy, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>📊 Total Social Media Growth Potential (90 Days)</h4>
    <p><strong>Current:</strong> 886 total followers across all platforms</p>
    <p><strong>90-Day Target:</strong> 2,000+ total followers</p>
    <p><strong>Growth Strategy:</strong> Focus on Instagram + TikTok (highest growth potential), 
    optimize YouTube conversion, minimal maintenance on Facebook/Twitter</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 4: CRITICAL ISSUES
# ============================================
elif section == "Critical Issues":
    st.header("IV. Critical Issues - The '7 Deadly Sins'")
    
    st.markdown("""
    <div class="risk-box">
    <h3>🚨 SEVEN CRITICAL ISSUES PREVENTING GROWTH</h3>
    <p>These issues must be addressed IMMEDIATELY in Month 1.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs for each critical issue
    issue_tabs = st.tabs([
        "1️⃣ Content Confusion",
        "2️⃣ Community Void", 
        "3️⃣ Conversion Catastrophe",
        "4️⃣ Collaboration Vacuum",
        "5️⃣ Campaign Abandonment",
        "6️⃣ £0 Budget Blindness",
        "7️⃣ Email List Void"
    ])
    
    # Issue 1: Content Confusion
    with issue_tabs[0]:
        st.subheader("Sin #1: The Content Confusion Crisis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **The Problem:**
            
            YouTube sends mixed signals:
            - 90% prayer content (50-300 views)
            - 10% music content (1,000-2,000 views)
            
            **Impact:**
            - Algorithm doesn't know who to recommend to
            - Subscribers came for music, see prayer → stop watching
            - Growth stalled at 0.47 subs/day
            - Can't monetize
            """)
        
        with col2:
            fig = go.Figure(data=[
                go.Pie(
                    labels=['Prayer Content', 'Music Content'],
                    values=[90, 10],
                    marker=dict(colors=['#D4A574', '#8B4789']),
                    textinfo='percent+label',
                    hole=0.4
                )
            ])
            fig.update_layout(
                title="YouTube Content Mix (Problem)",
                height=300,
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Music-First Hybrid (Recommended)</h4>
        <p><strong>Option A (Two-Channel Strategy):</strong></p>
        <ul>
        <li><strong>JohnGreat Music:</strong> Music videos, Shorts, performances</li>
        <li><strong>JohnGreat Ministry:</strong> Prayer sessions, devotionals</li>
        </ul>
        <p><strong>Option B (Integrated Worship):</strong></p>
        <ul>
        <li>70% music content</li>
        <li>30% short devotionals (5-10 min, not 1-3 hours)</li>
        <li>Clear separation in playlists</li>
        </ul>
        <p><strong>Week 1 Actions:</strong></p>
        <ol>
        <li>Create playlist: "JohnGreat Music Videos"</li>
        <li>Redesign 10 music video thumbnails</li>
        <li>Rewrite 10 titles (SEO-optimized)</li>
        <li>Pin comment on every music video: "Stream on Spotify → [link]"</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 2: Community Void
    with issue_tabs[1]:
        st.subheader("Sin #2: The Community Catastrophe")
        
        engagement_data = {
            'Platform': ['Instagram', 'Facebook', 'TikTok', 'Twitter/X'],
            'Following': [4, 0, 0, 1],
            'Community Status': ['Ghost', 'Dead', 'Invisible', 'Abandoned']
        }
        
        df_engagement = pd.DataFrame(engagement_data)
        
        fig = go.Figure(data=[
            go.Bar(
                x=df_engagement['Platform'],
                y=df_engagement['Following'],
                marker_color=['#dc3545', '#dc3545', '#dc3545', '#dc3545'],
                text=df_engagement['Following'],
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title="Zero Community Engagement (Following Count)",
            yaxis_title="Accounts Following",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: "30-30-30 Engagement Rule"</h4>
        <p><strong>Daily (30 min total):</strong></p>
        <ul>
        <li><strong>10 min:</strong> Comment on 5-10 gospel artist posts (genuine comments)</li>
        <li><strong>10 min:</strong> Respond to ALL comments on your content</li>
        <li><strong>10 min:</strong> Share/repost 2-3 gospel music posts to Stories</li>
        </ul>
        <p><strong>Week 1 Targets:</strong></p>
        <ol>
        <li>Follow 50 UK gospel artists on Instagram</li>
        <li>Comment on 10 posts/day for 7 days</li>
        <li>Join 5 Facebook gospel music groups</li>
        <li>Reply to every comment within 1 hour</li>
        </ol>
        <p><strong>Expected:</strong> 10-20 new followers, 2-3 collaboration opportunities</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 3: Conversion Catastrophe
    with issue_tabs[2]:
        st.subheader("Sin #3: The Conversion Catastrophe (0.23%)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Current Conversion", "0.23%", delta="-94.6% below industry", delta_color="inverse")
            st.metric("YouTube Subscribers", "849")
            st.metric("Spotify Monthly Listeners", "2")
        
        with col2:
            st.markdown("""
            **Industry Standard:**
            - Minimum: 5% conversion
            - Good: 10% conversion
            - Excellent: 15%+ conversion
            
            **What JohnGreat Should Have:**
            - 849 subs × 5% = **42 listeners** (minimum)
            - 849 subs × 10% = **85 listeners** (realistic)
            - 849 subs × 15% = **127 listeners** (good)
            
            **Current:** 2 listeners = **95% below minimum**
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Fix YouTube → Spotify Funnel</h4>
        <p><strong>Every YouTube Video MUST Have:</strong></p>
        <ol>
        <li><strong>Pinned Comment:</strong> "🎧 STREAM NOW → [Linktree link]"</li>
        <li><strong>Description Start:</strong> "Listen on your favorite platform:" with links</li>
        <li><strong>End Screen:</strong> Spotify/Apple Music links</li>
        <li><strong>Verbal CTA:</strong> "Make sure you stream this on Spotify"</li>
        </ol>
        <p><strong>Instagram Strategy:</strong></p>
        <ul>
        <li>Every Reel: "Full song on Spotify - link in bio"</li>
        <li>Story sticker: "Swipe up to stream" or "Link in bio"</li>
        <li>Feed posts: "Out now on all platforms 🎧"</li>
        </ul>
        <p><strong>Target (60 Days):</strong> 42 monthly listeners (10x improvement)</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 4: Collaboration Vacuum
    with issue_tabs[3]:
        st.subheader("Sin #4: The Collaboration Void")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Current State:**
            - 2 songs released
            - 1 collaboration (FaithFave) → **UNUSED**
            - Zero cross-promotion visible
            - Not connected to gospel community
            
            **Missed Opportunity:**
            - Access to FaithFave's audience
            - Cross-promotion potential
            - Playlist curator attention
            - Community credibility
            """)
        
        with col2:
            collaboration_data = {
                'Type': ['Featured Artist', 'Cross-Promotion', 'Joint Live', 'Playlist Exchange'],
                'Status': ['✅ Has (unused)', '❌ Missing', '❌ Missing', '❌ Missing'],
                'Potential Reach': ['100-500 listeners', '50-200 followers', '20-50 viewers', '50-100 streams']
            }
            
            df_collab = pd.DataFrame(collaboration_data)
            st.dataframe(df_collab, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Collaboration Activation Strategy</h4>
        <p><strong>Immediate Actions (Month 1):</strong></p>
        <ol>
        <li><strong>Reactivate FaithFave Collab:</strong>
           - Reach out: "Let's do joint Instagram Live about 'Made Up My Mind'"
           - Create collab content (behind-the-scenes, acoustic version)
           - Cross-promote on both artists' pages</li>
        <li><strong>Identify 5 New Targets:</strong>
           - UK gospel artists (500-5,000 followers)
           - Complementary sound
           - Active on social media</li>
        <li><strong>Collaboration Pitch Template:</strong>
           - "Hi [Artist], love your song [specific]. Would you be open to collaborating on a worship medley or joint acoustic session?"</li>
        </ol>
        <p><strong>Target (90 Days):</strong> 3 collaboration features secured</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 5: Campaign Abandonment
    with issue_tabs[4]:
        st.subheader("Sin #5: The Campaign Abandonment Pattern")
        
        abandonment_data = {
            'Platform': ['Twitter/X', 'Facebook', 'Instagram'],
            'Created': ['May 2025', 'June 2025', 'June 2025'],
            'Active Period': ['July 2025 (3 posts)', 'June-July 2025 (6 posts)', 'June-July 2025 (6 posts)'],
            'Silent Period': ['6 months', '5-6 months', '4-6 months'],
            'Status': ['Abandoned', 'Ghosted', 'Inconsistent']
        }
        
        df_abandonment = pd.DataFrame(abandonment_data)
        
        fig = go.Figure(data=[
            go.Scatter(
                x=['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
                y=[1, 3, 5, 1, 2, 1, 1, 1, 1],
                mode='lines+markers',
                name='Posting Frequency',
                line=dict(color='#dc3545', width=3),
                marker=dict(size=10)
            )
        ])
        
        fig.update_layout(
            title="Social Media Posting Pattern (Ghosting)",
            yaxis_title="Posts per Month",
            xaxis_title="Month (2025-2026)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Content Flywheel System</h4>
        <p><strong>One Pillar Asset → 15+ Content Pieces:</strong></p>
        <pre>
        1 Song Recording (1 hour)
          ↓
        ├─ 1 Music Video (3-5 min)
        ├─ 3 YouTube Shorts (15-30 sec clips)
        ├─ 3 TikTok videos (15-30 sec)
        ├─ 3 Instagram Reels (30-60 sec)
        ├─ 1 Instagram carousel (lyrics + photos)
        ├─ 1 Behind-the-scenes Reel
        ├─ 3 Quote graphics (lyrics)
        └─ 5-7 days of Instagram Stories
        </pre>
        <p><strong>Batch Creation Schedule (Monthly):</strong></p>
        <ul>
        <li><strong>Week 1:</strong> Record 2 songs or 1 music video shoot</li>
        <li><strong>Week 1:</strong> Edit into 15+ pieces</li>
        <li><strong>Week 2-4:</strong> Schedule everything using Later/Buffer</li>
        <li><strong>Daily (10 min):</strong> Respond to comments, engage</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 6: £0 Budget Blindness
    with issue_tabs[5]:
        st.subheader("Sin #6: The £0 Budget Blindness")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Ad Spend", "£0", delta="Confirmed via Facebook transparency")
        
        with col2:
            st.metric("Instagram Reach", "1,662 (30 days)", delta="-57.7% decline")
        
        with col3:
            st.metric("Estimated Organic Reach", "5-10% of followers", delta="Algorithm penalty")
        
        st.markdown("---")
        
        budget_scenarios = {
            'Scenario': ['£0 Budget', '£50/Month', '£100/Month', '£200/Month'],
            'Expected Followers/Month': ['5-15', '30-50', '50-100', '100-200'],
            'Expected Listeners/Month': ['2-5', '10-20', '20-40', '50-100'],
            'ROI': ['Slow organic', '10x better', '20x better', '40x better']
        }
        
        df_budget = pd.DataFrame(budget_scenarios)
        st.dataframe(df_budget, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Smart Budget Allocation</h4>
        <p><strong>Recommended Minimum: £50/Month</strong></p>
        <ul>
        <li><strong>£30:</strong> Instagram Reels ads (music video promo)</li>
        <li><strong>£20:</strong> Facebook ads (targeting gospel music groups)</li>
        </ul>
        <p><strong>Expected Results (£50/month):</strong></p>
        <ul>
        <li>1,500-2,500 targeted impressions</li>
        <li>30-50 new followers/month</li>
        <li>10-20 new Spotify listeners</li>
        <li><strong>10x better than current organic</strong></li>
        </ul>
        <p><strong>Strategic ROI (Non-Monetary):</strong></p>
        <ul>
        <li>500+ monthly listeners = Spotify algorithm engagement</li>
        <li>500 followers = Social proof (people follow active accounts)</li>
        <li>Playlist consideration (curators notice momentum)</li>
        <li>Foundation for music career</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Issue 7: Email List Void
    with issue_tabs[6]:
        st.subheader("Sin #7: The Email List Void")
        
        st.markdown("""
        <div class="risk-box">
        <h4>🚨 CATASTROPHIC RISK: ZERO OWNED AUDIENCE</h4>
        <p>JohnGreat is 100% dependent on social media platforms. If:</p>
        <ul>
        <li>Instagram algorithm changes → Reach drops 80% overnight</li>
        <li>TikTok bans account → Lose all followers</li>
        <li>Spotify changes algorithm → Streams drop</li>
        <li>Facebook deprioritizes musicians → Page dies</li>
        </ul>
        <p><strong>Result:</strong> Career OVER. Starting from zero again.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **With Email List (Even Just 100):**
            
            **New Song Release:**
            - Send email: "New song tomorrow - pre-save now"
            - 100 subscribers × 30% open = 30 people see it
            - 30 × 50% click = 15 pre-saves
            - 15 Day 1 streams = Triggers Spotify algorithm
            - **15x better than Instagram post alone**
            """)
        
        with col2:
            st.markdown("""
            **Industry Examples:**
            
            **Elevation Worship:**
            - 300,000+ email subscribers
            - Email drives album launches to #1
            
            **Maverick City Music:**
            - Email list for exclusive tour access
            - Sells out within hours
            
            **Kirk Franklin:**
            - Email list for tour announcements
            - Higher conversion than social media
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ Solution: Email List Foundation (Week 1)</h4>
        <p><strong>Lead Magnet Ideas:</strong></p>
        <ol>
        <li>"30-Day Worship Devotional" (Daily scripture + song recommendation)</li>
        <li>"Behind the Music: Making of 'Made Up My Mind'" (PDF/video)</li>
        <li>"Exclusive Acoustic Performance" (unreleased version)</li>
        </ol>
        <p><strong>Implementation (Week 1):</strong></p>
        <ol>
        <li>Sign up for Mailchimp (free up to 500 subscribers)</li>
        <li>Create lead magnet: "7-Day Worship Challenge" PDF (Canva, 30 min)</li>
        <li>Add to Linktree as #1 link: "🎁 FREE: 7-Day Worship Challenge"</li>
        <li>Promote in content:
            - Instagram bio: "Get my free worship guide - link in bio"
            - YouTube pinned comment: "📧 Join my email list"
            - End of videos: "Get free worship guide in description"</li>
        </ol>
        <p><strong>Target (90 Days):</strong> 100+ email subscribers</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# SECTION 5: 90-DAY ACTION PLAN
# ============================================
elif section == "90-Day Action Plan":
    st.header("V. 90-Day Action Plan")
    
    st.markdown("""
    <div class="success-box">
    <h3>🎯 Overall Strategy: "Foundation → Momentum → Scale"</h3>
    <p><strong>Month 1:</strong> Stop the bleeding (Fix foundations, establish consistent presence)</p>
    <p><strong>Month 2:</strong> Build momentum (Grow engaged community, increase streaming)</p>
    <p><strong>Month 3:</strong> Scale what works (Multiply successes, establish sustainable system)</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Month tabs
    month_tabs = st.tabs(["📅 Month 1: Foundation", "🚀 Month 2: Momentum", "⚡ Month 3: Scale"])
    
    # Month 1
    with month_tabs[0]:
        st.subheader("Month 1: Stop the Bleeding (Days 1-30)")
        
        weekly_tasks = {
            'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            'Focus': ['Emergency Fixes', 'Content & Engagement', 'Paid Promotion Launch', 'Optimization'],
            'Key Tasks': [
                'Fix YouTube, Instagram, TikTok, Email, Facebook, Twitter',
                'Batch create content, first email campaign, community engagement',
                'Launch ads (£50-100), playlist pitching, collaboration outreach',
                'Analytics review, content repurposing, month 2 planning'
            ],
            'Targets': [
                'All platforms reactivated, 5-10 new followers',
                '10-15 new followers, 5-10 email subs',
                '20-30 new followers, 10-15 new listeners',
                'Optimize based on data, plan month 2'
            ]
        }
        
        df_week1 = pd.DataFrame(weekly_tasks)
        st.dataframe(df_week1, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.subheader("Week 1: Emergency Fixes (Day-by-Day)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Day 1:** Content Audit & Strategy
            - Review all existing content
            - Create content calendar for 30 days
            - Set up scheduling tools
            
            **Day 2:** YouTube Emergency Optimization
            - Redesign 5 music video thumbnails
            - Rewrite 5 music video titles (SEO)
            - Add pinned comments to all videos
            
            **Day 3:** Instagram Reactivation
            - Update bio, Linktree
            - Create 7 Reels from existing footage
            - Follow 20 UK gospel artists
            """)
        
        with col2:
            st.markdown("""
            **Day 4:** TikTok Resurrection
            - Create 10 short clips from music videos
            - Follow 30 gospel artists on TikTok
            - Duet 3 popular gospel TikToks
            
            **Day 5:** Email List Setup
            - Sign up for Mailchimp (free)
            - Create "7-Day Worship Challenge" lead magnet
            - Add to Linktree as #1 link
            
            **Day 6:** Facebook Reactivation
            - Join 5 UK gospel music Facebook groups
            - Engage in groups
            - Share "No One Like You" with story
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>Month 1 Success Metrics</h4>
        <ul>
        <li><strong>Streaming:</strong> 2 → 10-15 monthly listeners (5-7x growth)</li>
        <li><strong>Instagram:</strong> 33 → 60-80 followers (2x growth)</li>
        <li><strong>TikTok:</strong> 1 → 20-50 followers (20-50x growth)</li>
        <li><strong>Email:</strong> 0 → 20-30 subscribers</li>
        <li><strong>Budget:</strong> £50-100 spent (if available)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Month 2
    with month_tabs[1]:
        st.subheader("Month 2: Build Momentum (Days 31-60)")
        
        st.markdown("""
        <div class="insight-box">
        <h4>💡 Month 2 Focus: Content System + Community</h4>
        <p>Build on Month 1 foundation, increase content output, grow engaged community</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Month 2 Timeline
        timeline_data = {
            'Week': ['Week 5', 'Week 6', 'Week 7', 'Week 8'],
            'Theme': ['Content System', 'Growth Sprints', 'Email & Fans', 'Optimization'],
            'Key Activities': [
                'Batch creation, collaboration launch, playlist pitching',
                'Instagram sprint, TikTok sprint, YouTube optimization',
                'Email campaigns, fan engagement, community deepening',
                'Content repurposing, paid ads round 2, month 3 planning'
            ],
            'Growth Targets': [
                '40-60 new followers, content system established',
                '30-50 new followers, platform-specific growth',
                '20-30 email subs, deeper fan connections',
                'Optimization based on data, prepare for scale'
            ]
        }
        
        df_month2 = pd.DataFrame(timeline_data)
        st.dataframe(df_month2, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Key Month 2 Initiatives:**
            
            1. **Content Flywheel:**
               - 1 pillar asset → 20+ content pieces
               - Batch creation day each month
               - Scheduling automation
            
            2. **First Collaboration Launch:**
               - Instagram Live worship session
               - TikTok duet chain
               - Cross-promotion
            
            3. **Playlist Pitching Campaign:**
               - Research 20 playlists
               - Send personalized pitches
               - Follow up with curators
            """)
        
        with col2:
            st.markdown("""
            **Month 2 Success Metrics:**
            
            - **Streaming:** 15 → 50+ monthly listeners (3x growth)
            - **Instagram:** 80 → 150+ followers (2x growth)
            - **TikTok:** 50 → 150+ followers (3x growth)
            - **Email:** 30 → 70+ subscribers (2x growth)
            - **Budget:** £100-150 spent (if available)
            - **Collaborations:** 1-2 secured
            - **Playlists:** 2-5 placements secured
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>💪 Platform Growth Sprints (Week 6)</h4>
        <p><strong>Instagram Sprint (3 days):</strong></p>
        <ul>
        <li>Reel every day + 5-10 Stories/day</li>
        <li>Engagement blitz: Follow 30, comment on 30 posts</li>
        <li>Expected: 15-25 new followers</li>
        </ul>
        <p><strong>TikTok Sprint (2 days):</strong></p>
        <ul>
        <li>Post 2 videos/day, duet 5-10 popular videos</li>
        <li>Engage heavily: Comment on 20, follow 20</li>
        <li>Expected: 20-50 new followers</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Month 3
    with month_tabs[2]:
        st.subheader("Month 3: Scale What Works (Days 61-90)")
        
        st.markdown("""
        <div class="insight-box">
        <h4>⚡ Month 3 Focus: Acceleration & Systemization</h4>
        <p>Multiply what works, establish sustainable system, achieve 500+ listener target</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Month 3 Goals Chart
        goals_data = {
            'Metric': ['Spotify Monthly Listeners', 'Instagram Followers', 'TikTok Followers', 'Email Subscribers'],
            'Start (Day 60)': [50, 150, 150, 70],
            'Target (Day 90)': [500, 300, 500, 100],
            'Growth': ['10x', '2x', '3x', '1.5x']
        }
        
        df_goals = pd.DataFrame(goals_data)
        st.dataframe(df_goals, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        st.subheader("Month 3 Strategy: The 10X Mindset")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Viral Content Strategy:**
            
            1. **Test 10 TikTok Variations:**
               - Testimony + worship hook
               - Trend hijacking
               - Relatable POV videos
               - Challenge participation
            
            2. **Instagram Reels Scale-Up:**
               - Use best-performing content for ads
               - Increase posting frequency
               - Engage with trending sounds
            """)
        
        with col2:
            st.markdown("""
            **Paid Ads Scale-Up (If Budget):**
            
            **£150-200 Budget:**
            - Campaign 1: Streaming focus (£80)
            - Campaign 2: Profile growth (£60)
            - Campaign 3: Retargeting (£40)
            
            **Expected Results:**
            - 100-200 new listeners
            - 120-200 new followers
            - 3,000-5,000 impressions
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>🎯 Final 10-Day Push (Days 80-90)</h4>
        <p><strong>If Behind Targets:</strong></p>
        <ol>
        <li><strong>Day 82:</strong> Email blast + Instagram Story series for streaming push</li>
        <li><strong>Day 83:</strong> Facebook group posts + WhatsApp broadcast</li>
        <li><strong>Day 84:</strong> Playlist curator outreach + Twitter push</li>
        <li><strong>Day 85:</strong> Final ad boost (if budget) + urgency campaign</li>
        </ol>
        <p><strong>Target:</strong> Close gaps to hit 500 monthly listeners</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.subheader("90-Day Complete Transformation")
        
        # Final growth chart
        days = [0, 30, 60, 90]
        listeners = [2, 15, 50, 500]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=days,
            y=listeners,
            mode='lines+markers',
            name='Monthly Listeners',
            line=dict(color='#8B4789', width=4),
            marker=dict(size=12),
            fill='tozeroy',
            fillcolor='rgba(139, 71, 137, 0.2)'
        ))
        
        fig.add_hrect(y0=500, y1=550, line_width=0, fillcolor="green", opacity=0.2, 
                     annotation_text="Target: 500+ listeners", annotation_position="top left")
        
        fig.update_layout(
            title="90-Day Spotify Listener Growth Trajectory",
            xaxis_title="Days",
            yaxis_title="Monthly Listeners",
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="success-box">
        <h4>🎉 90-Day Success Metrics</h4>
        <p><strong>Starting Point (Day 0):</strong></p>
        <ul>
        <li>2 Spotify monthly listeners</li>
        <li>33 Instagram followers</li>
        <li>1 TikTok follower</li>
        <li>0 email subscribers</li>
        <li>£0 ad spend</li>
        </ul>
        <p><strong>90-Day Target (Day 90):</strong></p>
        <ul>
        <li>500+ Spotify monthly listeners (250x growth)</li>
        <li>300+ Instagram followers (9x growth)</li>
        <li>500+ TikTok followers (500x growth)</li>
        <li>100+ email subscribers (from 0)</li>
        <li>Sustainable content system established</li>
        <li>2-3 collaborations secured</li>
        <li>5-10 playlist placements</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# SECTION 6: KPIs & TARGETS
# ============================================
elif section == "KPIs & Targets":
    st.header("VI. Key Performance Indicators & Targets")
    
    # Primary KPI
    st.markdown("""
    <div class="metric-card">
    <h2>PRIMARY KPI: Spotify Monthly Listeners</h2>
    <p><strong>Starting:</strong> 2 listeners | <strong>90-Day Target:</strong> 500+ listeners</p>
    <p><strong>Growth Required:</strong> 250x increase</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # KPI Dashboard
    st.subheader("📊 90-Day KPI Dashboard")
    
    kpi_tabs = st.tabs(["Streaming", "Social Media", "Email", "Engagement", "Financial"])
    
    # Streaming KPIs
    with kpi_tabs[0]:
        streaming_kpis = {
            'Metric': ['Spotify Monthly Listeners', 'Total Streams (90 days)', 'Playlist Placements', 'Algorithm Playlists', 'Listener Geography'],
            'Starting': ['2', '500-1,000', '0', 'None', 'Unknown'],
            'Target': ['500+', '15,000+', '5-10', 'Release Radar, Discover Weekly', 'UK, Nigeria, US'],
            'Weight': ['30%', '20%', '20%', '15%', '15%']
        }
        
        df_streaming = pd.DataFrame(streaming_kpis)
        st.dataframe(df_streaming, use_container_width=True, hide_index=True)
        
        # Streaming growth chart
        months = ['Start', 'Month 1', 'Month 2', 'Month 3']
        listeners = [2, 15, 50, 500]
        
        fig = go.Figure(data=[
            go.Bar(
                x=months,
                y=listeners,
                marker_color=['#dc3545', '#ffc107', '#17a2b8', '#28a745'],
                text=listeners,
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title="Spotify Listener Growth Targets",
            yaxis_title="Monthly Listeners",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Social Media KPIs
    with kpi_tabs[1]:
        social_kpis = {
            'Platform': ['Instagram', 'TikTok', 'YouTube', 'Facebook', 'Twitter/X', 'Total'],
            'Starting': ['33', '1', '849', '3', '0', '886'],
            'Target': ['300+', '500+', '1,000+', '100+', '100+', '2,000+'],
            'Growth': ['9x', '500x', '1.2x', '33x', '∞', '2.3x'],
            'Priority': ['High', 'High', 'Medium', 'Low', 'Medium', 'N/A']
        }
        
        df_social = pd.DataFrame(social_kpis)
        st.dataframe(df_social, use_container_width=True, hide_index=True)
        
        # Social media growth chart
        platforms = ['Instagram', 'TikTok', 'YouTube', 'Facebook']
        start = [33, 1, 849, 3]
        target = [300, 500, 1000, 100]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Starting',
            x=platforms,
            y=start,
            marker_color='#D4A574'
        ))
        
        fig.add_trace(go.Bar(
            name='90-Day Target',
            x=platforms,
            y=target,
            marker_color='#8B4789'
        ))
        
        fig.update_layout(
            title="Social Media Follower Growth Targets",
            barmode='group',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Email KPIs
    with kpi_tabs[2]:
        st.markdown("""
        <div class="insight-box">
        <h4>📧 Email List - The Most Important KPI</h4>
        <p><strong>Why:</strong> Owned audience = career insurance. Not subject to algorithm changes.</p>
        <p><strong>Industry Standard:</strong> 10-20% of social followers should be on email list.</p>
        </div>
        """, unsafe_allow_html=True)
        
        email_kpis = {
            'Metric': ['Total Subscribers', 'Open Rate', 'Click Rate', 'Conversion to Streams', 'Superfans Identified'],
            'Starting': ['0', 'N/A', 'N/A', 'N/A', '0'],
            'Target': ['100+', '30%+', '20%+', '10%+', '10-20'],
            'Industry Avg': ['Varies', '20-25%', '10-15%', '5-10%', '1-5%']
        }
        
        df_email = pd.DataFrame(email_kpis)
        st.dataframe(df_email, use_container_width=True, hide_index=True)
        
        # Email growth projection
        months = ['Start', 'Month 1', 'Month 2', 'Month 3']
        subscribers = [0, 30, 70, 100]
        
        fig = go.Figure(data=[
            go.Scatter(
                x=months,
                y=subscribers,
                mode='lines+markers',
                line=dict(color='#28a745', width=3),
                marker=dict(size=10),
                fill='tozeroy'
            )
        ])
        
        fig.update_layout(
            title="Email List Growth Projection",
            yaxis_title="Subscribers",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Engagement KPIs
    with kpi_tabs[3]:
        engagement_kpis = {
            'Metric': ['Instagram Engagement Rate', 'TikTok Avg Views', 'YouTube Avg Views', 'Email Open Rate', 'Community Activity'],
            'Starting': ['6-12%', '123', '142', 'N/A', 'None'],
            'Target': ['15%+', '1,000+', '500+', '30%+', 'Daily'],
            'Industry Good': ['5-10%', '500-1,000', 'Varies', '20-25%', '3-5x/week']
        }
        
        df_engagement = pd.DataFrame(engagement_kpis)
        st.dataframe(df_engagement, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>🎯 Engagement Quality Over Quantity</h4>
        <p><strong>Target Engagement Metrics:</strong></p>
        <ul>
        <li><strong>Instagram:</strong> 15%+ engagement rate (likes + comments ÷ followers)</li>
        <li><strong>TikTok:</strong> 10%+ engagement rate (likes + comments + shares ÷ views)</li>
        <li><strong>YouTube:</strong> 5%+ CTR (click-through rate on thumbnails)</li>
        <li><strong>Email:</strong> 30%+ open rate, 20%+ click rate</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Financial KPIs
    with kpi_tabs[4]:
        st.markdown("""
        <div class="insight-box">
        <h4>💰 Financial Realities (90-Day Perspective)</h4>
        <p><strong>Important:</strong> Financial ROI will be negative in first 90 days. This is NORMAL.</p>
        <p>Goal is STRATEGIC ROI (audience building, systems, foundation).</p>
        </div>
        """, unsafe_allow_html=True)
        
        financial_kpis = {
            'Metric': ['Total Investment', 'Streaming Revenue', 'ROI (Monetary)', 'Cost Per Listener', 'Strategic ROI'],
            'Budget £0': ['£0', '£5-10', 'N/A', '£0', 'Audience growth only'],
            'Budget £50/m': ['£150', '£15-25', '-83% to -87%', '£0.30-0.50', '10x faster growth'],
            'Budget £100/m': ['£300', '£20-35', '-89% to -93%', '£0.60-1.00', '20x faster growth']
        }
        
        df_financial = pd.DataFrame(financial_kpis)
        st.dataframe(df_financial, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>📈 Strategic ROI (What Really Matters)</h4>
        <p><strong>With £100/Month Budget:</strong></p>
        <ul>
        <li><strong>Investment:</strong> £300 over 3 months</li>
        <li><strong>Returns:</strong> £20-35 streaming revenue</li>
        <li><strong>Monetary ROI:</strong> -89% to -93% (Normal for early stage)</li>
        </ul>
        <p><strong>BUT Strategic ROI:</strong></p>
        <ul>
        <li>500+ monthly listeners = Spotify algorithm starts working</li>
        <li>2,000+ followers = Social proof for growth</li>
        <li>100+ email subscribers = Owned audience foundation</li>
        <li>Content system = Sustainable without burnout</li>
        <li>Career foundation = Can build from here</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Success Assessment
    st.subheader("📋 90-Day Success Assessment Framework")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #28a745 0%, #20c997 100%);">
        <h3>🎯 TARGET ACHIEVED</h3>
        <p><strong>500+ listeners</strong></p>
        <p>Ready for next phase</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #ffc107 0%, #fd7e14 100%);">
        <h3>📈 STRONG PROGRESS</h3>
        <p><strong>300-499 listeners</strong></p>
        <p>On track, refine strategy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);">
        <h3>🔄 NEEDS REVISION</h3>
        <p><strong>&lt; 300 listeners</strong></p>
        <p>Major strategy overhaul</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================
# SECTION 7: CONTENT STRATEGY
# ============================================
elif section == "Content Strategy":
    st.header("VII. Content Strategy & Flywheel System")
    
    st.markdown("""
    <div class="success-box">
    <h3>🎯 The Content Flywheel: One Pillar → 20+ Pieces</h3>
    <p>Create sustainable system where 1 hour of recording generates 2 weeks of content.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Content Flywheel Visualization
    st.subheader("📊 The Content Flywheel System")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        ```
        ONE PILLAR ASSET (1 hour recording)
                ↓
        ┌─────────────────────────────────┐
        │  VIDEO CONTENT (10 pieces)      │
        │  • 1 Full YouTube video         │
        │  • 3 YouTube Shorts             │
        │  • 3 Instagram Reels            │
        │  • 3 TikTok videos              │
        │                                 │
        │  AUDIO CONTENT (5 pieces)       │
        │  • 3 Audiogram clips            │
        │  • 1 Podcast snippet            │
        │  • 1 Behind-the-scenes audio    │
        │                                 │
        │  WRITTEN CONTENT (5 pieces)     │
        │  • 1 Blog post                  │
        │  • 3 Quote graphics             │
        │  • 1 Instagram carousel         │
        │                                 │
        │  EMAIL CONTENT (2 pieces)       │
        │  • 1 Email: Behind the scenes   │
        │  • 1 Email: Exclusive clip      │
        └─────────────────────────────────┘
                ↓
        TOTAL: 22 pieces from 1 hour
        ```
        """)
    
    st.markdown("---")
    
    # Content Pillars
    st.subheader("🎭 Content Pillars (Monthly Rotation)")
    
    pillars = st.tabs(["🎵 Music Content", "🎬 Behind-the-Scenes", "📖 Testimony/Story", "🤝 Engagement/Community"])
    
    with pillars[0]:
        st.markdown("""
        **Focus: 40% of content**
        
        **Content Ideas:**
        1. **Full song music videos** (YouTube)
        2. **Acoustic versions** (Instagram Reels/TikTok)
        3. **Piano-only instrumentals** (YouTube Shorts)
        4. **Lyric videos** (Instagram carousels)
        5. **Live performance clips** (all platforms)
        6. **Song meaning breakdowns** (YouTube/IGTV)
        7. **Cover songs** (with unique gospel twist)
        8. **Mashups/medleys** (trending worship songs)
        
        **Production Quality:**
        - Maintain professional standards
        - Outdoor cinematography (current strength)
        - Clear audio (invest in good microphone)
        - Subtitles/captions (accessibility + watch time)
        """)
    
    with pillars[1]:
        st.markdown("""
        **Focus: 25% of content**
        
        **Content Ideas:**
        1. **Studio session vlogs** (recording process)
        2. **Songwriting process** (how songs are born)
        3. **Morning routine** (as a worship artist)
        4. **Equipment tour** (keyboard, mic, setup)
        5. **Workspace setup** (where creativity happens)
        6. **Day in the life** (authentic, relatable)
        7. **Collaboration sessions** (with other artists)
        8. **Photo shoot BTS** (creating visual content)
        
        **Style:**
        - Raw, authentic, unpolished
        - Phone camera is FINE
        - Show mistakes and learning
        - Build connection through vulnerability
        """)
    
    with pillars[2]:
        st.markdown("""
        **Focus: 25% of content**
        
        **Content Ideas:**
        1. **Personal salvation story** (why you worship)
        2. **"Why I do music" testimony** (calling/purpose)
        3. **Season of struggle → God's faithfulness** (relatable)
        4. **Scripture that inspires music** (Bible connection)
        5. **Prayer moments** (raw, authentic worship)
        6. **Worship experience stories** (church, personal)
        7. **"God moment" of the week** (regular series)
        8. **Answered prayer shares** (testimony of God's work)
        
        **Key:**
        - Authenticity over production
        - Relatable struggles
        - Hope and redemption
        - Scripture integration
        """)
    
    with pillars[3]:
        st.markdown("""
        **Focus: 10% of content**
        
        **Content Ideas:**
        1. **Q&A sessions** (ask me anything)
        2. **Polls**: "Which song should I cover next?"
        3. **Challenges**: Duet challenges, worship challenges
        4. **Shoutouts to supporters** (community building)
        5. **"Finish the lyrics" games** (interactive)
        6. **Prayer request invitations** (ministry focus)
        7. **Testimony share invitations** (community sharing)
        8. **"Tag someone who needs this"** (shareable content)
        
        **Goal:**
        - Build community, not just audience
        - Encourage interaction
        - Create shareable moments
        - Foster connections between followers
        """)
    
    st.markdown("---")
    
    # Posting Schedule
    st.subheader("📅 Weekly Posting Schedule")
    
    schedule_data = {
        'Platform': ['Instagram', 'TikTok', 'YouTube', 'Email', 'Facebook', 'Twitter'],
        'Daily': ['1 Reel + 3-5 Stories', '1-2 videos', 'As needed', 'N/A', 'N/A', 'N/A'],
        'Weekly': ['7 Reels, 20+ Stories', '7-14 videos', '1-3 Shorts or 1 main video', '1 newsletter', '3-4 posts', 'Daily engagement'],
        'Time/Day': ['30 min', '20 min', '20 min', '15 min', '10 min', '10 min'],
        'Best Time': ['6-8pm UK', '12-2pm & 7-9pm', '2-4pm weekdays', 'Tuesday 10am', '7-9pm weekdays', 'Throughout day']
    }
    
    df_schedule = pd.DataFrame(schedule_data)
    st.dataframe(df_schedule, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Batch Creation System
    st.subheader("⚡ Batch Creation System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Monthly Batch Day (First Saturday):**
        
        **Morning (9am-12pm):**
        - Plan month's content calendar
        - Film/record pillar assets (2 songs, 1 testimony)
        - Take photos for graphics
        
        **Afternoon (1pm-4pm):**
        - Edit videos into 20+ pieces
        - Create graphics in Canva
        - Write captions/descriptions
        
        **Evening (5pm-6pm):**
        - Schedule everything using Later/Buffer
        - Set up email campaigns
        - Review and finalize
        """)
    
    with col2:
        st.markdown("""
        **Daily Maintenance (30-45 min total):**
        
        **Morning (15 min):**
        - Check scheduled posts went live
        - Respond to overnight comments
        - Engage with 5-10 other artists' posts
        
        **Evening (15-30 min):**
        - Post TikTok (if not scheduled)
        - Check analytics (what's working?)
        - Engage in Facebook groups
        - Plan tomorrow's engagement
        
        **Weekly (Sunday, 1 hour):**
        - Review weekly analytics
        - Adjust upcoming schedule if needed
        - Plan next batch creation session
        """)
    
    st.markdown("---")
    
    # Tools & Templates
    st.subheader("🛠️ Tools & Templates")
    
    tool_tabs = st.tabs(["Free Tools", "Paid Tools", "Templates"])
    
    with tool_tabs[0]:
        st.markdown("""
        **Content Creation:**
        - **CapCut** (video editing) - Mobile/Desktop
        - **Canva** (graphics) - Web/App
        - **InShot** (quick mobile edits)
        - **Adobe Express** (alternative to Canva)
        
        **Scheduling:**
        - **Later** (Instagram/Facebook) - Free tier: 30 posts
        - **Buffer** (Multi-platform) - Free tier: 10 posts
        - **TikTok** native scheduler
        - **YouTube** scheduled uploads
        
        **Analytics:**
        - **Spotify for Artists** (free)
        - **Instagram Insights** (free)
        - **TikTok Analytics** (free)
        - **YouTube Analytics** (free)
        
        **Email Marketing:**
        - **Mailchimp** (free up to 500 subscribers)
        - **ConvertKit** (free up to 300 subscribers)
        - **Sendinblue** (free up to 300 emails/day)
        """)
    
    with tool_tabs[1]:
        st.markdown("""
        **Optional but Valuable:**
        
        **Content Creation (£):**
        - **Adobe Creative Suite** (£50/month) - If serious about visuals
        - **Epidemic Sound** (£10/month) - Background music for content
        - **Artlist** (£15/month) - Music and sound effects
        
        **Growth & Analytics (£):**
        - **SubmitHub** (£10-30/campaign) - Playlist pitching platform
        - **Later Pro** (£15/month) - Advanced scheduling
        - **Chartmetric** (£40/month) - Deep music analytics
        - **Hypefury** (£20/month) - Twitter growth automation
        
        **Distribution (£):**
        - **DistroKid** (£20/year unlimited uploads)
        - **TuneCore** (£10-30/year per release)
        - **CD Baby** (one-time fee per release)
        """)
    
    with tool_tabs[2]:
        st.markdown("""
        **Content Templates (Canva):**
        
        **Instagram Reel Templates:**
        1. **Testimony Template:**
           - 0-3s: Hook (emotional face + text: "I was struggling with...")
           - 3-10s: Problem (B-roll + text explanation)
           - 10-20s: Turning point (worship moment + text: "Then God...")
           - 20-30s: Resolution (song climax + CTA: "Stream this song")
        
        2. **Worship Moment Template:**
           - 0-5s: Beautiful shot (piano, outdoor, emotional)
           - 5-25s: Song moment (best 20 seconds)
           - 25-30s: CTA ("Full song in bio")
        
        **Email Templates:**
        ```
        Subject: [Emotional hook/question]
        
        Hey [Name],
        
        [Personal story/update - 2-3 sentences]
        
        [Value/content - 2-3 sentences]
        
        [Call to action - 1 sentence]
        
        Blessings,
        John
        
        P.S. [Secondary CTA or personal note]
        ```
        """)

# ============================================
# SECTION 8: BUDGET SCENARIOS
# ============================================
elif section == "Budget Scenarios":
    st.header("VIII. Budget Scenarios & ROI Analysis")
    
    st.markdown("""
    <div class="insight-box">
    <h4>💰 Financial Reality Check</h4>
    <p><strong>Important:</strong> Monetary ROI will be negative in first 90 days. This is NORMAL for artist development.</p>
    <p>Focus on <strong>STRATEGIC ROI</strong> (audience building, systems, career foundation).</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Budget Scenario Tabs
    budget_tabs = st.tabs(["£0 Budget", "£50/Month", "£100/Month", "£200/Month"])
    
    # £0 Budget
    with budget_tabs[0]:
        st.subheader("Scenario A: £0 Budget (Organic Only)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Strategy:**
            - Community engagement focus
            - Collaboration over advertising
            - Time investment over money
            
            **Daily Time: 1-2 hours**
            - 30 min: Content creation (phone only)
            - 30 min: Community engagement
            - 30 min: Collaboration outreach
            - 30 min: Analytics & planning
            """)
        
        with col2:
            st.markdown("""
            **90-Day Expectations:**
            
            **Growth (Conservative):**
            - Spotify: 2 → 50-100 listeners
            - Instagram: 33 → 100-150 followers
            - TikTok: 1 → 100-200 followers
            - Email: 0 → 30-50 subscribers
            
            **Challenges:**
            - Slow growth (frustration risk)
            - Algorithm dependency
            - High time investment
            - Burnout potential
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>✅ £0 Budget Success Formula</h4>
        <p><strong>Focus Areas:</strong></p>
        <ol>
        <li><strong>Community First:</strong> Build genuine relationships with other gospel artists</li>
        <li><strong>Collaboration Heavy:</strong> Features on other artists' songs = access to their audience</li>
        <li><strong>Content Repurposing:</strong> Maximize every piece of content (1 → 10 pieces)</li>
        <li><strong>Platform Optimization:</strong> Perfect profile, SEO, CTAs (free but crucial)</li>
        <li><strong>Consistency Over Quality:</strong> Post daily even if not perfect</li>
        </ol>
        <p><strong>Timeline:</strong> 6-12 months to reach 500 listeners (realistic expectation)</p>
        </div>
        """, unsafe_allow_html=True)
    
    # £50/Month Budget
    with budget_tabs[1]:
        st.subheader("Scenario B: £50/Month Budget (Recommended Minimum)")
        
        # Budget Allocation
        budget_data = {
            'Platform': ['Instagram Reels Ads', 'Facebook Ads', 'Tools/Software', 'Total'],
            'Amount': ['£30', '£20', '£0 (free tools)', '£50'],
            'Purpose': ['Music video promotion', 'Gospel group targeting', 'Content creation', 'Monthly total'],
            'Expected Results': ['20-30 new followers, 10-15 listeners', '10-15 new followers, 5-10 listeners', 'Efficiency gains', '30-50 new followers, 15-25 listeners']
        }
        
        df_budget50 = pd.DataFrame(budget_data)
        st.dataframe(df_budget50, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **90-Day Investment: £150**
            
            **Expected Returns:**
            - **Followers:** 90-150 new (across platforms)
            - **Listeners:** 45-75 new (Spotify monthly)
            - **Email:** 45-60 new subscribers
            - **Streams:** 4,500-7,500 additional
            
            **Monetary ROI:**
            - Investment: £150
            - Revenue: £18-30 (streaming)
            - Net: -£120 to -£132
            - ROI: -80% to -88%
            """)
        
        with col2:
            st.markdown("""
            **Strategic ROI:**
            
            **What £150 Buys:**
            1. **Algorithm Attention:** 45-75 listeners = Spotify starts recommending
            2. **Social Proof:** 90-150 followers = people follow active accounts
            3. **Playlist Consideration:** Curators notice growing numbers
            4. **Momentum:** Growth begets growth
            5. **Time Efficiency:** Faster results = less burnout
            
            **Compared to £0:**
            - 3-5x faster growth
            - Higher morale (seeing results)
            - Better algorithm treatment
            - More collaboration opportunities
            """)
        
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Why £50/Month is Recommended Minimum</h4>
        <p>For emerging artists, £50/month is the <strong>"minimum viable investment"</strong> to:</p>
        <ul>
        <li>Overcome algorithm suppression (organic reach is 5-10% of followers)</li>
        <li>Get in front of targeted audience (gospel music fans in UK)</li>
        <li>Build social proof (people follow accounts that look active/popular)</li>
        <li>Maintain motivation (seeing growth encourages consistency)</li>
        </ul>
        <p><strong>Reality:</strong> Beautiful content with zero promotion = shouting into the void.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # £100/Month Budget
    with budget_tabs[2]:
        st.subheader("Scenario C: £100/Month Budget (Realistic Growth)")
        
        # Budget Allocation Pie Chart
        labels = ['Instagram Ads', 'TikTok Promote', 'YouTube Ads', 'Retargeting']
        values = [40, 30, 20, 10]
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            hole=0.4,
            marker=dict(colors=['#8B4789', '#D4A574', '#17a2b8', '#28a745'])
        )])
        
        fig.update_layout(
            title="£100/Month Budget Allocation",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        # Expected Results
        results_data = {
            'Metric': ['Impressions', 'Profile Visits', 'New Followers', 'New Listeners', 'Cost Per Result'],
            'Instagram (£40)': ['2,000-3,000', '80-120', '30-40', '15-20', '£1.00-1.33'],
            'TikTok (£30)': ['5,000-10,000', '150-250', '40-60', '20-30', '£0.50-0.75'],
            'YouTube (£20)': ['1,000-2,000', '30-50', '10-15', '5-10', '£2.00-4.00'],
            'Total (£100)': ['8,000-15,000', '260-420', '80-115', '40-60', '£0.87-1.25']
        }
        
        df_results100 = pd.DataFrame(results_data)
        st.dataframe(df_results100, use_container_width=True, hide_index=True)
        
        st.markdown("""
        <div class="action-box">
        <h4>📈 £100/Month 90-Day Projection</h4>
        <p><strong>Total Investment:</strong> £300</p>
        <p><strong>Expected 90-Day Results:</strong></p>
        <ul>
        <li><strong>Followers:</strong> 240-345 new (across platforms)</li>
        <li><strong>Listeners:</strong> 120-180 new (Spotify monthly)</li>
        <li><strong>Email Subscribers:</strong> 60-90 new</li>
        <li><strong>Additional Streams:</strong> 12,000-18,000</li>
        </ul>
        <p><strong>End of 90 Days:</strong></p>
        <ul>
        <li>Spotify: 120-180 monthly listeners</li>
        <li>Instagram: 270-380 followers</li>
        <li>TikTok: 240-350 followers</li>
        <li>Email: 60-90 subscribers</li>
        </ul>
        <p><strong>Verdict:</strong> Strong foundation for sustainable growth into Year 2.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # £200/Month Budget
    with budget_tabs[3]:
        st.subheader("Scenario D: £200/Month Budget (Aggressive Growth)")
        
        st.markdown("""
        <div class="success-box">
        <h4>⚡ Aggressive Growth Scenario</h4>
        <p>For artists ready to invest seriously in music career. Assumes:</p>
        <ul>
        <li>Music is primary focus (not hobby)</li>
        <li>Willing to invest before seeing returns</li>
        <li>Ready to treat music as business</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Monthly Breakdown
        monthly_allocation = {
            'Category': ['Paid Advertising', 'Content Production', 'Tools/Software', 'Playlist Pitching', 'Total'],
            'Amount': ['£120', '£50', '£20', '£10', '£200'],
            'Details': [
                'Instagram/TikTok/YouTube ads',
                'Better equipment, locations, collaborators',
                'Paid scheduling, analytics tools',
                'SubmitHub campaigns, curator outreach',
                'Monthly total investment'
            ]
        }
        
        df_monthly200 = pd.DataFrame(monthly_allocation)
        st.dataframe(df_monthly200, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # ROI Analysis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **90-Day Investment: £600**
            
            **Expected Returns:**
            - **Followers:** 500-750 new
            - **Listeners:** 250-375 new
            - **Email:** 125-180 subscribers
            - **Streams:** 25,000-37,500 additional
            
            **Monetary ROI:**
            - Investment: £600
            - Revenue: £100-150 (streaming)
            - Net: -£450 to -£500
            - ROI: -75% to -83%
            """)
        
        with col2:
            st.markdown("""
            **Strategic ROI (What Matters):**
            
            **End of 90 Days:**
            - Spotify: 250-375 monthly listeners
            - Instagram: 530-780 followers
            - TikTok: 500-750 followers
            - Email: 125-180 subscribers
            
            **Career Milestones Achieved:**
            1. Spotify algorithm fully engaged
            2. Social proof established
            3. Playlist curator attention
            4. Collaboration requests incoming
            5. Foundation for Year 2 growth
            
            **Year 2 Potential:**
            - 1,000-2,000 monthly listeners
            - Music income starts covering costs
            - Church booking opportunities
            - Label/management interest
            """)
        
        st.markdown("""
        <div class="action-box">
        <h4>🎯 When to Choose £200/Month Budget</h4>
        <p><strong>Choose this if:</strong></p>
        <ul>
        <li>You're committed to music career (not hobby)</li>
        <li>You have savings/income to invest</li>
        <li>You're ready to work the system (1-2 hours/day)</li>
        <li>You believe in your music's potential</li>
        <li>You want to accelerate timeline (500 listeners in 90 days possible)</li>
        </ul>
        <p><strong>Warning:</strong> Only invest what you can afford to lose. Music career building takes 2-3 years minimum.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Budget Comparison
    st.subheader("📊 Budget Scenario Comparison")
    
    comparison_data = {
        'Scenario': ['£0 (Organic)', '£50/Month', '£100/Month', '£200/Month'],
        '90-Day Cost': ['£0', '£150', '£300', '£600'],
        'Expected Listeners': ['50-100', '45-75', '120-180', '250-375'],
        'Expected Followers': ['100-200', '90-150', '240-345', '500-750'],
        'Time to 500 Listeners': ['6-12 months', '4-6 months', '3-4 months', '2-3 months'],
        'Best For': ['Hobby/Ministry', 'Emerging Artist', 'Serious Artist', 'Career Investment']
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>💡 Recommendation</h4>
    <p><strong>For JohnGreat:</strong> Start with <strong>£50-100/month</strong> for first 90 days.</p>
    <p><strong>Why:</strong></p>
    <ol>
    <li>Overcomes algorithm suppression (organic reach is dead for new accounts)</li>
    <li>Builds momentum faster (encourages consistency)</li>
    <li>Tests what works (which platforms/content convert best)</li>
    <li>Accelerates learning curve (paid analytics provide better data)</li>
    <li>Sets foundation for sustainable growth</li>
    </ol>
    <p><strong>Minimum:</strong> £50/month. <strong>Optimal:</strong> £100/month. <strong>Aggressive:</strong> £200/month.</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 9: EMAIL MARKETING
# ============================================
elif section == "Email Marketing":
    st.header("IX. Email Marketing Strategy")
    
    st.markdown("""
    <div class="risk-box">
    <h3>🚨 CRITICAL GAP: Zero Owned Audience</h3>
    <p>JohnGreat has <strong>ZERO email subscribers</strong> = 100% dependent on social media algorithms.</p>
    <p>This is the <strong>#1 priority</strong> to fix in Week 1.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Why Email Matters
    st.subheader("📧 Why Email is NON-NEGOTIABLE for Gospel Artists")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **The Algorithm Problem:**
        
        **Social Media Reach (2026):**
        - Instagram: 5-10% of followers
        - Facebook: 1-3% of followers
        - TikTok: Algorithm decides
        - YouTube: Subscribers don't see all videos
        
        **With 33 Instagram followers:**
        - 33 × 10% = 3-4 people see each post
        - This is NOT a sustainable growth strategy
        """)
    
    with col2:
        st.markdown("""
        **The Email Solution:**
        
        **Email Deliverability:**
        - 20-40% open rates (industry standard)
        - Direct to inbox (no algorithm)
        - YOU control communication
        
        **With 100 email subscribers:**
        - 100 × 30% = 30 people open email
        - 30 × 50% = 15 click to stream
        - 15 Day 1 streams = Algorithm triggers
        """)
    
    st.markdown("---")
    
    # Lead Magnet Strategy
    st.subheader("🎁 Lead Magnet Strategy (Week 1)")
    
    lead_magnet_tabs = st.tabs(["7-Day Worship Challenge", "Exclusive Acoustic", "Worship Guide", "Behind-the-Scenes"])
    
    with lead_magnet_tabs[0]:
        st.markdown("""
        **Option 1: 7-Day Worship Challenge (Recommended)**
        
        **What it is:**
        - 7-day email series
        - Daily scripture + worship song recommendation
        - Day 1-3: Old Testament worship
        - Day 4-7: New Testament worship
        
        **Implementation:**
        1. **Create in Canva (30 min):**
           - Design 7-page PDF
           - Each page: Scripture + reflection prompt + song suggestion
           - Branded with JohnGreat visuals
        
        2. **Set up in Mailchimp:**
           - Create opt-in form
           - Set up automated welcome sequence
           - Connect to Linktree
        
        3. **Promote:**
           - Link in bio: "🎁 FREE: 7-Day Worship Challenge"
           - YouTube pinned comments
           - Instagram Stories
           - End of videos
        
        **Expected:**
        - 10-20 signups first week (existing audience)
        - 20-40/month (with promotion)
        """)
    
    with lead_magnet_tabs[1]:
        st.markdown("""
        **Option 2: Exclusive Acoustic Performance**
        
        **What it is:**
        - Unreleased acoustic version of "No One Like You"
        - Video or audio download
        - Behind-the-scenes commentary
        
        **Implementation:**
        1. **Record (1 hour):**
           - Piano-only version
           - Raw, emotional take
           - Maybe different lyrics/arrangement
        
        2. **Produce:**
           - Simple video (phone is fine)
           - Good audio quality (crucial)
           - Upload to private YouTube/Vimeo
        
        3. **Gate it:**
           - Email required for access link
           - Automate delivery via Mailchimp
        
        **Strength:** High perceived value
        **Challenge:** Requires production effort
        """)
    
    with lead_magnet_tabs[2]:
        st.markdown("""
        **Option 3: Worship Guide for Believers**
        
        **What it is:**
        - "How to Create Personal Worship Space"
        - Tips for daily worship routine
        - Scripture references
        - JohnGreat song recommendations
        
        **Implementation:**
        1. **Create guide (2 hours):**
           - 5-10 page PDF
           - Practical, actionable tips
           - Personal testimony woven in
        
        2. **Design:**
           - Professional layout (Canva)
           - Photos of worship spaces
           - Scripture graphics
        
        3. **Positioning:**
           - Not just about music
           - About deepening relationship with God
           - Music as tool for worship
        
        **Target:** Serious Christians wanting deeper worship life
        """)
    
    with lead_magnet_tabs[3]:
        st.markdown("""
        **Option 4: Behind-the-Music Package**
        
        **What it is:**
        - "Making of Made Up My Mind"
        - Songwriting process
        - Recording studio footage
        - Unreleased demos
        
        **Implementation:**
        1. **Compile assets:**
           - Studio photos/videos
           - Voice notes of songwriting
           - Early demos
           - Lyrics evolution
        
        2. **Create package:**
           - PDF with story + photos
           - Private video playlist
           - Downloadable demo track
        
        3. **Storytelling:**
           - Emotional journey
           - God's inspiration
           - Collaborative process (FaithFave)
        
        **Strength:** Builds connection with existing fans
        """)
    
    st.markdown("---")
    
    # Email Sequence Strategy
    st.subheader("📨 Email Sequence Strategy")
    
    sequence_tabs = st.tabs(["Welcome Sequence", "Weekly Newsletter", "Song Launch", "Engagement"])
    
    with sequence_tabs[0]:
        st.markdown("""
        **Welcome Sequence (Automated - 3 emails)**
        
        **Email 1: Immediately after signup**
        ```
        Subject: Your [Lead Magnet] is here! 🙏
        
        Welcome [Name]!
        
        Thank you for joining the JohnGreat Worship Family!
        
        Here's your [Lead Magnet] as promised: [Download Link]
        
        I'm JohnGreat, a UK-based gospel worship artist, and I create music 
        to draw people closer to God through authentic worship.
        
        Here's my latest song if you haven't heard it yet: [Spotify Link]
        
        Blessings,
        John
        
        P.S. Reply to this email and let me know what you think - I read every response!
        ```
        
        **Email 2: 3 days later**
        ```
        Subject: The story behind "No One Like You"
        
        Hey [Name],
        
        I wanted to share something personal...
        
        [Story about why the song was written, personal struggle, God's faithfulness]
        
        If you haven't heard it yet: [Spotify Link]
        
        John
        ```
        
        **Email 3: 7 days later**
        ```
        Subject: What's next? (+ exclusive update)
        
        [Name], you've been on my list for a week now!
        
        I'm grateful you're here.
        
        Here's what's coming:
        - New music in [timeframe]
        - [Upcoming project/collaboration]
        - Exclusive content just for email family
        
        Stay tuned!
        
        John
        ```
        """)
    
    with sequence_tabs[1]:
        st.markdown("""
        **Weekly Newsletter Format**
        
        **Schedule:** Every Tuesday 10am
        **Goal:** Consistent touchpoint, not salesy
        
        **Template:**
        ```
        Subject: [Emotional hook/question]
        
        Hey [Name],
        
        [Personal update - 2-3 sentences]
        What God is teaching me, current season, etc.
        
        [Value/content - 2-3 sentences]
        Scripture insight, worship tip, music recommendation.
        
        [This week's worship moment]
        Link to new Reel/TikTok/YouTube video.
        
        [Call to action - 1 sentence]
        Stream my latest, share with friend, pray for request.
        
        Blessings,
        John
        
        P.S. [Secondary CTA or personal note]
        ```
        
        **Content Rotation:**
        - Week 1: Personal testimony/update
        - Week 2: Scripture + worship insight
        - Week 3: Behind-the-scenes music update
        - Week 4: Community spotlight (fan testimonies)
        """)
    
    with sequence_tabs[2]:
        st.markdown("""
        **Song Launch Sequence**
        
        **Pre-Launch (2 weeks before):**
        ```
        Subject: Something special is coming...
        
        [Teaser without giving away details]
        [Build anticipation]
        [Ask for prayer for release]
        ```
        
        **Pre-Save Campaign (1 week before):**
        ```
        Subject: Be the first to hear my new song
        
        [Story behind song]
        [Why it matters]
        [Pre-save link] ← MOST IMPORTANT
        ```
        
        **Launch Day (12am):**
        ```
        Subject: IT'S HERE! [Song Name]
        
        [Celebration!]
        [Full story]
        [ALL streaming links]
        [Ask to share with one person]
        ```
        
        **Day 2 (Follow-up):**
        ```
        Subject: Thank you! + Behind the scenes
        
        [Gratitude]
        [Behind-the-scenes content]
        [Ask for playlist adds]
        ```
        
        **Week 2 (Sustain momentum):**
        ```
        Subject: We're almost at [goal] streams!
        
        [Progress update]
        [Ask for one more stream/share]
        [What's next teaser]
        ```
        """)
    
    with sequence_tabs[3]:
        st.markdown("""
        **Engagement & Community Building**
        
        **Survey Email (Quarterly):**
        ```
        Subject: I need your help
        
        [Ask for feedback on music]
        [What do you want to hear next?]
        [Prayer requests?]
        ```
        
        **Testimony Collection:**
        ```
        Subject: Has my music ministered to you?
        
        [Ask for testimonies]
        [Will share (with permission)]
        [Builds social proof]
        ```
        
        **Exclusive Content:**
        ```
        Subject: Just for you: [Exclusive Content]
        
        [Acoustic version]
        [Unreleased song snippet]
        [Early access to something]
        ```
        
        **Re-engagement (If opens drop):**
        ```
        Subject: I've missed you
        
        [Haven't heard from you]
        [Still creating music]
        [Ask if want to stay subscribed]
        ```
        """)
    
    st.markdown("---")
    
    # Implementation Timeline
    st.subheader("⏰ Email List Implementation Timeline")
    
    timeline_data = {
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Month 2', 'Month 3'],
        'Action': [
            'Set up Mailchimp, create lead magnet, add to Linktree',
            'Promote in content, launch welcome sequence',
            'First weekly newsletter, analyze open rates',
            'Segment list (new vs engaged), optimize',
            'Launch survey, collect testimonials',
            '100+ subscribers, plan song launch sequence'
        ],
        'Target': ['10-20 subs', '20-30 subs', '30-40 subs', '40-50 subs', '50-70 subs', '70-100+ subs']
    }
    
    df_email_timeline = pd.DataFrame(timeline_data)
    st.dataframe(df_email_timeline, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>🎯 Why Email Changes Everything</h4>
    <p><strong>Current Reality (Without Email):</strong></p>
    <ul>
    <li>New song drops → Post to Instagram → 3-4 people see it → Maybe 1 streams</li>
    <li>Algorithm doesn't notice → No further promotion → Song dies</li>
    </ul>
    <p><strong>New Reality (With 100 Email Subscribers):</strong></p>
    <ul>
    <li>New song drops → Email 100 people → 30 open → 15 click to stream</li>
    <li>15 Day 1 streams → Spotify algorithm notices → Adds to Release Radar</li>
    <li>Release Radar exposure → 50-100 more streams → Discover Weekly inclusion</li>
    <li>Discover Weekly → 200-500 streams → Sustainable growth begins</li>
    </ul>
    <p><strong>Email is the trigger that starts the flywheel.</strong></p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# SECTION 10: QUICK WINS
# ============================================
elif section == "Quick Wins":
    st.header("X. Quick Wins (Week 1 Implementation)")
    
    st.markdown("""
    <div class="action-box">
    <h3>🚀 7-Day Transformation Plan</h3>
    <p>Implement these quick wins in Week 1 to see IMMEDIATE improvement.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Day-by-Day Quick Wins
    day_tabs = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"])
    
    # Day 1
    with day_tabs[0]:
        st.subheader("📊 Day 1: Content Audit & Strategy Session (2 hours)")
        
        st.markdown("""
        **Morning (1 hour):**
        
        1. **Content Audit:**
           - List all existing content (YouTube, Instagram, TikTok)
           - Identify top 5 best-performing posts (save for repurposing)
           - Identify worst-performing (learn what not to do)
        
        2. **Competitor Analysis:**
           - Find 3 similar UK gospel artists
           - Analyze their content strategy
           - Note what's working for them
        
        **Afternoon (1 hour):**
        
        3. **Content Calendar Creation:**
           - Plan 30 days of content (use template below)
           - Mix: Music (40%), BTS (25%), Testimony (25%), Engagement (10%)
        
        4. **Tool Setup:**
           - Create Canva account (free)
           - Download CapCut (free)
           - Set up Later/Buffer free account
        """)
        
        # Content Calendar Template
        st.markdown("**Weekly Content Calendar Template:**")
        calendar_data = {
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            'Instagram': ['Reel: Worship moment', 'Reel: Behind scenes', 'Reel: Testimony', 'Reel: Scripture', 'Reel: Music video clip', 'Reel: Q&A', 'Story only'],
            'TikTok': ['Trending sound', 'POV video', 'Duet challenge', 'Raw worship', 'Song snippet', 'Testimony', 'Rest day'],
            'YouTube': ['Shorts: Piano clip', 'N/A', 'Shorts: Lyrics', 'N/A', 'Shorts: BTS', 'N/A', 'Potential main video']
        }
        
        df_calendar = pd.DataFrame(calendar_data)
        st.dataframe(df_calendar, use_container_width=True, hide_index=True)
    
    # Day 2
    with day_tabs[1]:
        st.subheader("🎬 Day 2: YouTube Emergency Optimization (2 hours)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Before & After Examples:**
            
            **Title Optimization:**
            ❌ "Episode #12"
            ✅ "Gospel Worship Song About Overcoming Fear | JohnGreat"
            
            **Thumbnail Optimization:**
            ❌ Auto-generated screenshot
            ✅ Emotion-led face + bold text + contrasting colors
            
            **Description Optimization:**
            ❌ No links or minimal text
            ✅ Streaming links FIRST, then story, then timestamps
            """)
        
        with col2:
            st.markdown("""
            **Action Items (Checklist):**
            
            ✅ Redesign 5 music video thumbnails (Canva)
            ✅ Rewrite 5 music video titles (SEO keywords)
            ✅ Add pinned comment to all music videos:
               "🎧 STREAM ON SPOTIFY → [Linktree link]"
            ✅ Update video descriptions:
               1. Streaming links (Spotify, Apple Music, etc.)
               2. Story behind song
               3. Timestamps (if applicable)
               4. Social media links
            ✅ Add end screens to music videos:
               - Subscribe button
               - Spotify link
               - Next recommended video
            """)
        
        st.markdown("""
        <div class="insight-box">
        <h4>💡 YouTube SEO Keywords for Gospel Music</h4>
        <ul>
        <li>"UK gospel worship"</li>
        <li>"Nigerian gospel music"</li>
        <li>"Christian worship songs"</li>
        <li>"Piano worship"</li>
        <li>"New gospel music 2026"</li>
        <li>"Overcoming fear worship song"</li>
        <li>"God's faithfulness worship"</li>
        </ul>
        <p>Include these in titles, descriptions, and tags.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Day 3
    with day_tabs[2]:
        st.subheader("📸 Day 3: Instagram Reactivation (1.5 hours)")
        
        st.markdown("""
        **Profile Optimization (15 min):**
        
        **Bio Template:**
        ```
        JohnGreat
        UK Gospel Worship Artist 🎹 🇬🇧🇳🇬
        Bringing worship that moves hearts
        New Music: "No One Like You" ⬇️
        ```
        
        **Action Items:**
        ✅ Update bio (use template above)
        ✅ Update profile picture (high-res, professional)
        ✅ Update Linktree (lead magnet first, then music)
        ✅ Create Instagram Highlights:
           - "Music" (song releases)
           - "Live" (saved Live sessions)
           - "Worship" (moments)
           - "Testimony" (stories)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Content Creation (1 hour):**
        
        **Create 7 Reels from Existing Footage:**
        1. **Reel 1:** 30-sec clip from "No One Like You" music video
           - Hook: Emotional moment
           - Caption: "When you realize there's NO ONE like God"
           - CTA: "Full song in bio"
        
        2. **Reel 2:** Piano performance snippet
           - Hook: Beautiful outdoor shot
           - Caption: "Sunday worship moment 🎹"
           - Trending audio (gospel/worship)
        
        3. **Reel 3:** Testimony moment
           - Hook: "I was going through..."
           - B-roll of walking/thinking
           - Resolution: "Then this song came on"
        
        4. **Reel 4-7:** Similar variations
        
        **Schedule:** 1 Reel/day for next 7 days (use Later free tier)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Community Engagement (15 min):**
        
        **Immediate Actions:**
        ✅ Follow 20 UK gospel artists
        ✅ Comment on 10 gospel music posts (genuine, meaningful)
        ✅ Like 50 gospel music posts
        ✅ Save 10 posts to engage with later
        
        **Engagement Template:**
        ```
        Not: "Great post!"
        Yes: "This really blessed me today, especially when you sang [specific part]. Thank you for using your gift!"
        ```
        """)
    
    # Day 4
    with day_tabs[3]:
        st.subheader("🎵 Day 4: TikTok Resurrection (1 hour)")
        
        st.markdown("""
        **Profile Optimization (10 min):**
        
        **Bio Template:**
        ```
        JohnGreat | UK Gospel Artist
        Worship that moves hearts 🎹
        New: "No One Like You"
        Jesus is everything ✝️
        ```
        
        **Action Items:**
        ✅ Update bio
        ✅ Update profile picture (sync with Instagram)
        ✅ Add Spotify link (if 1,000+ followers, otherwise Linktree)
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Content Creation (30 min):**
        
        **Create 10 TikTok Variations:**
        
        **Formula 1: Testimony Hook (15-30 sec)**
        ```
        0-3s: "I was going through [struggle]..."
        3-10s: B-roll showing struggle
        10-20s: "Then this song came on..." + emotional music moment
        20-30s: CTA: "Full song in bio"
        ```
        
        **Formula 2: POV Videos**
        ```
        Text: POV: You finally surrender to God
        Video: Emotional worship moment
        Audio: Trending worship sound OR your song
        ```
        
        **Formula 3: Worship Challenge**
        ```
        Duet a popular worship TikTok
        Add your harmony/version
        Tag original creator
        ```
        
        **Post 1 today, schedule 2-3/week**
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Community Engagement (20 min):**
        
        **Immediate Actions:**
        ✅ Follow 30 gospel artists on TikTok
        ✅ Duet 3 popular gospel TikToks
        ✅ Comment on 20 gospel videos
        ✅ Like 50 videos
        
        **Goal:** Get on gospel music TikTok's radar
        """)
    
    # Day 5
    with day_tabs[4]:
        st.subheader("📧 Day 5: Email List Setup (1 hour)")
        
        st.markdown("""
        **Platform Setup (20 min):**
        
        **Choose Platform:**
        - **Mailchimp:** Free up to 500 subscribers (recommended)
        - **ConvertKit:** Free up to 300 subscribers
        - **Sendinblue:** Free up to 300 emails/day
        
        **Action Items:**
        ✅ Sign up for chosen platform
        ✅ Create sign-up form
        ✅ Design form to match brand
        ✅ Set up automated welcome sequence
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Lead Magnet Creation (30 min):**
        
        **"7-Day Worship Challenge" PDF:**
        
        **Canva Creation:**
        1. Open Canva, search "ebook" template
        2. Choose simple, professional design
        3. Create 7 pages:
           - Cover: "7-Day Worship Challenge"
           - Day 1: Scripture + reflection + JohnGreat song recommendation
           - Day 2-7: Same format
           - Back: Thank you + social media links
        
        **Content:**
        - Each day: One scripture about worship
        - Reflection question/prompt
        - Recommended worship song (include JohnGreat songs)
        - Action step (pray, journal, listen)
        
        **Save as PDF**
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Integration (10 min):**
        
        **Linktree Update:**
        ```
        CURRENT:
        1. Made Up My Mind links
        2. YouTube
        3. Instagram
        4. X
        5. TikTok
        
        NEW (Week 1):
        1. 🎁 FREE: 7-Day Worship Challenge (Email capture)
        2. 🆕 Stream "No One Like You" (All platforms)
        3. 🎵 Stream "Made Up My Mind"
        4. 📱 Instagram
        5. 📱 YouTube
        6. 📱 TikTok
        ```
        
        **Promotion Setup:**
        ✅ Instagram bio: "Get my free worship guide ⬇️"
        ✅ YouTube pinned comment template
        ✅ Email signature (if sending emails)
        """)
    
    # Day 6
    with day_tabs[5]:
        st.subheader("📘 Day 6: Facebook Reactivation (45 min)")
        
        st.markdown("""
        **Group Strategy (30 min):**
        
        **Join These Groups (Search and join):**
        1. Gospel Music Lovers (500K+ members)
        2. UK Christian Music (200K+ members)
        3. African Gospel Music Worldwide (300K+ members)
        4. Gospel Music Artists Network (50K+ members)
        5. Worship Leaders & Musicians (100K+ members)
        
        **Group Engagement Rules:**
        - Read group rules first
        - Don't spam (instant ban risk)
        - Engage genuinely before posting
        - Provide value, not just promotion
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Content & Engagement (15 min):**
        
        **Initial Post Template:**
        ```
        Hi Gospel Music Family! 👋
        
        I'm JohnGreat, a UK-based worship artist, and I just released 
        "No One Like You" - a worship song about God's unmatched faithfulness.
        
        I'd love your honest feedback from fellow gospel music lovers!
        
        Stream here: [Linktree]
        
        And if it blesses you, I'd be grateful if you'd share it with 
        someone who needs encouragement today.
        
        Thank you for supporting independent gospel music!
        
        Blessings,
        John
        ```
        
        **Engagement Plan:**
        ✅ Post to 2 groups (where allowed)
        ✅ Comment on 10 posts in groups (genuine engagement)
        ✅ Like 20 posts
        ✅ Share 1-2 posts to page timeline
        """)
    
    # Day 7
    with day_tabs[6]:
        st.subheader("🐦 Day 7: Twitter/X Revival (30 min)")
        
        st.markdown("""
        **Profile Optimization (10 min):**
        
        **Bio Template:**
        ```
        JohnGreat | UK Gospel Worship Artist
        🎹 Piano-driven worship
        🇬🇧🇳🇬 UK-based, Nigerian heritage
        New: "No One Like You"
        Jesus is everything ✝️
        ```
        
        **Action Items:**
        ✅ Update bio
        ✅ Update header image (Canva template)
        ✅ Update profile picture (sync with Instagram)
        ✅ Pin introduction tweet
        """)
        
        st.markdown("---")
        
        st.markdown("""
        **Content & Networking (20 min):**
        
        **Introduction Tweet:**
        ```
        Hi Twitter gospel fam! 👋
        
        I'm JohnGreat, a UK gospel worship artist. 
        Been quiet here but ready to connect with the 
        gospel music community.
        
        My latest: "No One Like You" - bringing worship 
        from the UK to the world 🎹🇬🇧
        
        Would love to connect with other UK gospel artists!
        
        #GospelMusic #UKGospel #WorshipMusic
        ```
        
        **Engagement Plan:**
        ✅ Follow 50 people:
           - 20 UK gospel artists
           - 10 playlist curators
           - 10 gospel music blogs
           - 10 worship leaders
        
        ✅ Comment on 10 tweets:
           - #GospelMusic posts
           - #WorshipWednesday
           - Other artists' announcements
        
        ✅ Like 30 tweets
        
        **Daily Maintenance (5 min/day going forward):**
        - Check notifications
        - Reply to mentions
        - Engage with 5 gospel tweets
        """)
    
    st.markdown("---")
    
    # Week 1 Success Metrics
    st.subheader("📈 Week 1 Success Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Platforms Reactivated", "6/6", help="YouTube, Instagram, TikTok, Facebook, Twitter, Email")
    
    with col2:
        st.metric("Content Created", "20+ pieces", help="7 Reels, 10 TikToks, optimized YouTube")
    
    with col3:
        st.metric("Community Engagement", "150+ actions", help="Follows, comments, likes")
    
    with col4:
        st.metric("Expected New Followers", "10-20", help="Across all platforms")
    
    st.markdown("---")
    
    # Tools Checklist
    st.subheader("🛠️ Week 1 Tools Checklist")
    
    tools_data = {
        'Tool': ['Canva', 'CapCut', 'Mailchimp', 'Later/Buffer', 'Linktree', 'Spotify for Artists'],
        'Purpose': ['Graphics/design', 'Video editing', 'Email marketing', 'Scheduling', 'Link management', 'Analytics'],
        'Status': ['Free account created', 'App downloaded', 'Account set up', 'Free account created', 'Optimized', 'Claimed profile'],
        'Time': ['30 min', '15 min', '20 min', '15 min', '10 min', '15 min']
    }
    
    df_tools = pd.DataFrame(tools_data)
    st.dataframe(df_tools, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>🎉 Week 1 Transformation Complete!</h4>
    <p><strong>After Week 1, JohnGreat will have:</strong></p>
    <ul>
    <li>✅ All platforms optimized and reactivated</li>
    <li>✅ 30 days of content planned and partially created</li>
    <li>✅ Email list infrastructure ready</li>
    <li>✅ YouTube conversion pathways fixed</li>
    <li>✅ Community engagement system established</li>
    <li>✅ Tools and systems in place</li>
    </ul>
    <p><strong>From here:</strong> Month 1 focuses on consistency, Month 2 on momentum, Month 3 on scale.</p>
    <p><strong>The foundation is now built. Growth begins.</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("**Strategic Audit & Growth Plan** • Prepared by Oluwatosin Adejumo • © 2026")
st.markdown("*For internal use only • Confidential • Version 1.0*")