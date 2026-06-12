"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseFindingReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseFindingReasonCode: TypeAlias = Literal[
    "InvalidCloudWatchApplicationInsightsSetup",
    "CloudWatchApplicationInsightsError",
    "LicenseOverprovisioned",
    "Optimized",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InvalidCloudWatchApplicationInsightsSetup",
        "CloudWatchApplicationInsightsError",
        "LicenseOverprovisioned",
        "Optimized",
    )
)


def serialize_aws_json_1_0(value: LicenseFindingReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseFindingReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LicenseFindingReasonCode value: {data!r}")
    return cast(LicenseFindingReasonCode, data)
