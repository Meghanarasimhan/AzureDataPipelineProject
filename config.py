class OlympicConfig:
    """Configuration for Olympic data pipeline"""
    MEDAL_EFFICIENCY_HIGH = 0.30
    MEDAL_EFFICIENCY_MEDIUM = 0.15
    SPECIALIZATION_THRESHOLD = 25.0
    HIGH_RISK_THRESHOLD = 50.0
    FOCUSED_STRATEGY_THRESHOLD = 30.0
    TOP_N_RESULTS = 15
    CACHE_DATAFRAMES = True

# Global instance
config = OlympicConfig()