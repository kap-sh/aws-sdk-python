"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableECSServiceField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ExportableECSServiceField: TypeAlias = Literal[
    "AccountId",
    "ServiceArn",
    "LookbackPeriodInDays",
    "LastRefreshTimestamp",
    "LaunchType",
    "CurrentPerformanceRisk",
    "CurrentServiceConfigurationMemory",
    "CurrentServiceConfigurationCpu",
    "CurrentServiceConfigurationTaskDefinitionArn",
    "CurrentServiceConfigurationAutoScalingConfiguration",
    "CurrentServiceContainerConfigurations",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsMemoryMaximum",
    "Finding",
    "FindingReasonCodes",
    "RecommendationOptionsMemory",
    "RecommendationOptionsCpu",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "RecommendationOptionsContainerRecommendations",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "Tags",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    "EffectiveRecommendationPreferencesLookBackPeriod",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccountId",
        "ServiceArn",
        "LookbackPeriodInDays",
        "LastRefreshTimestamp",
        "LaunchType",
        "CurrentPerformanceRisk",
        "CurrentServiceConfigurationMemory",
        "CurrentServiceConfigurationCpu",
        "CurrentServiceConfigurationTaskDefinitionArn",
        "CurrentServiceConfigurationAutoScalingConfiguration",
        "CurrentServiceContainerConfigurations",
        "UtilizationMetricsCpuMaximum",
        "UtilizationMetricsMemoryMaximum",
        "Finding",
        "FindingReasonCodes",
        "RecommendationOptionsMemory",
        "RecommendationOptionsCpu",
        "RecommendationOptionsSavingsOpportunityPercentage",
        "RecommendationOptionsEstimatedMonthlySavingsCurrency",
        "RecommendationOptionsEstimatedMonthlySavingsValue",
        "RecommendationOptionsContainerRecommendations",
        "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
        "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
        "Tags",
        "EffectiveRecommendationPreferencesSavingsEstimationMode",
        "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
        "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
        "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
        "EffectiveRecommendationPreferencesLookBackPeriod",
    )
)


def serialize_aws_json_1_0(value: ExportableECSServiceField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableECSServiceField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportableECSServiceField value: {data!r}")
    return cast(ExportableECSServiceField, data)
