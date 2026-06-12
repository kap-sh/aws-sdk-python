"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLambdaFunctionField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ExportableLambdaFunctionField: TypeAlias = Literal[
    "AccountId",
    "FunctionArn",
    "FunctionVersion",
    "Finding",
    "FindingReasonCodes",
    "NumberOfInvocations",
    "UtilizationMetricsDurationMaximum",
    "UtilizationMetricsDurationAverage",
    "UtilizationMetricsMemoryMaximum",
    "UtilizationMetricsMemoryAverage",
    "LookbackPeriodInDays",
    "CurrentConfigurationMemorySize",
    "CurrentConfigurationTimeout",
    "CurrentCostTotal",
    "CurrentCostAverage",
    "RecommendationOptionsConfigurationMemorySize",
    "RecommendationOptionsCostLow",
    "RecommendationOptionsCostHigh",
    "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
    "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
    "LastRefreshTimestamp",
    "CurrentPerformanceRisk",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "Tags",
    "EffectiveRecommendationPreferencesSavingsEstimationMode",
    "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
    "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccountId",
        "FunctionArn",
        "FunctionVersion",
        "Finding",
        "FindingReasonCodes",
        "NumberOfInvocations",
        "UtilizationMetricsDurationMaximum",
        "UtilizationMetricsDurationAverage",
        "UtilizationMetricsMemoryMaximum",
        "UtilizationMetricsMemoryAverage",
        "LookbackPeriodInDays",
        "CurrentConfigurationMemorySize",
        "CurrentConfigurationTimeout",
        "CurrentCostTotal",
        "CurrentCostAverage",
        "RecommendationOptionsConfigurationMemorySize",
        "RecommendationOptionsCostLow",
        "RecommendationOptionsCostHigh",
        "RecommendationOptionsProjectedUtilizationMetricsDurationLowerBound",
        "RecommendationOptionsProjectedUtilizationMetricsDurationUpperBound",
        "RecommendationOptionsProjectedUtilizationMetricsDurationExpected",
        "LastRefreshTimestamp",
        "CurrentPerformanceRisk",
        "RecommendationOptionsSavingsOpportunityPercentage",
        "RecommendationOptionsEstimatedMonthlySavingsCurrency",
        "RecommendationOptionsEstimatedMonthlySavingsValue",
        "Tags",
        "EffectiveRecommendationPreferencesSavingsEstimationMode",
        "RecommendationOptionsSavingsOpportunityAfterDiscountsPercentage",
        "RecommendationOptionsEstimatedMonthlySavingsCurrencyAfterDiscounts",
        "RecommendationOptionsEstimatedMonthlySavingsValueAfterDiscounts",
    )
)


def serialize_aws_json_1_0(value: ExportableLambdaFunctionField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableLambdaFunctionField:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ExportableLambdaFunctionField value: {data!r}"
        )
    return cast(ExportableLambdaFunctionField, data)
