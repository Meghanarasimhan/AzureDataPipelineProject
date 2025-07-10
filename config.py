class OlympicConfig:
    """Configuration for Olympic data pipeline"""
    MEDAL_EFFICIENCY_HIGH = 0.30
    MEDAL_EFFICIENCY_MEDIUM = 0.15
    SPECIALIZATION_THRESHOLD = 25.0
    FEMALE_DOMINATED_THRESHOLD = 70.0    # >70% female = female dominated
    MALE_DOMINATED_THRESHOLD = 70.0      # >70% male = male dominated  
    BALANCED_SPORT_MIN = 40.0            # 40-60% = balanced
    BALANCED_SPORT_MAX = 60.0
    LARGE_SPORT_TOP_N = 10               # Top 10 sports = "large sports"
    MEDIUM_SPORT_TOP_N = 20  
    HIGH_RISK_THRESHOLD = 50.0
    FOCUSED_STRATEGY_THRESHOLD = 30.0
    TOP_N_RESULTS = 15
    CACHE_DATAFRAMES = True

# Global instance
config = OlympicConfig()