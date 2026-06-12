"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

LicenseRecommendationFilterName: TypeAlias = Literal[
    "Finding",
    "FindingReasonCode",
    "LicenseName",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Finding",
        "FindingReasonCode",
        "LicenseName",
    )
)


def serialize_aws_json_1_0(value: LicenseRecommendationFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseRecommendationFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LicenseRecommendationFilterName value: {data!r}"
        )
    return cast(LicenseRecommendationFilterName, data)
