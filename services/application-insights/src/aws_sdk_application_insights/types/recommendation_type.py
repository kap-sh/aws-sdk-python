"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

RecommendationType: TypeAlias = Literal[
    "INFRA_ONLY",
    "WORKLOAD_ONLY",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFRA_ONLY",
        "WORKLOAD_ONLY",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: RecommendationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationType value: {data!r}")
    return cast(RecommendationType, data)
