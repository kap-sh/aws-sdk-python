"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLicenseField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ExportableLicenseField: TypeAlias = Literal[
    "AccountId",
    "ResourceArn",
    "LookbackPeriodInDays",
    "LastRefreshTimestamp",
    "Finding",
    "FindingReasonCodes",
    "CurrentLicenseConfigurationNumberOfCores",
    "CurrentLicenseConfigurationInstanceType",
    "CurrentLicenseConfigurationOperatingSystem",
    "CurrentLicenseConfigurationLicenseName",
    "CurrentLicenseConfigurationLicenseEdition",
    "CurrentLicenseConfigurationLicenseModel",
    "CurrentLicenseConfigurationLicenseVersion",
    "CurrentLicenseConfigurationMetricsSource",
    "RecommendationOptionsOperatingSystem",
    "RecommendationOptionsLicenseEdition",
    "RecommendationOptionsLicenseModel",
    "RecommendationOptionsSavingsOpportunityPercentage",
    "RecommendationOptionsEstimatedMonthlySavingsCurrency",
    "RecommendationOptionsEstimatedMonthlySavingsValue",
    "Tags",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccountId",
        "ResourceArn",
        "LookbackPeriodInDays",
        "LastRefreshTimestamp",
        "Finding",
        "FindingReasonCodes",
        "CurrentLicenseConfigurationNumberOfCores",
        "CurrentLicenseConfigurationInstanceType",
        "CurrentLicenseConfigurationOperatingSystem",
        "CurrentLicenseConfigurationLicenseName",
        "CurrentLicenseConfigurationLicenseEdition",
        "CurrentLicenseConfigurationLicenseModel",
        "CurrentLicenseConfigurationLicenseVersion",
        "CurrentLicenseConfigurationMetricsSource",
        "RecommendationOptionsOperatingSystem",
        "RecommendationOptionsLicenseEdition",
        "RecommendationOptionsLicenseModel",
        "RecommendationOptionsSavingsOpportunityPercentage",
        "RecommendationOptionsEstimatedMonthlySavingsCurrency",
        "RecommendationOptionsEstimatedMonthlySavingsValue",
        "Tags",
    )
)


def serialize_aws_json_1_0(value: ExportableLicenseField) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportableLicenseField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportableLicenseField value: {data!r}")
    return cast(ExportableLicenseField, data)
