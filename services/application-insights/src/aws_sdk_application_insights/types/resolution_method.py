"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ResolutionMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

ResolutionMethod: TypeAlias = Literal[
    "MANUAL",
    "AUTOMATIC",
    "UNRESOLVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANUAL",
        "AUTOMATIC",
        "UNRESOLVED",
    )
)


def serialize_aws_json_1_1(value: ResolutionMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResolutionMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolutionMethod value: {data!r}")
    return cast(ResolutionMethod, data)
