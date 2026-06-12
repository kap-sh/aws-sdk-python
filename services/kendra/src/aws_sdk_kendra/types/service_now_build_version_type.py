"""Generated from Smithy shape ``com.amazonaws.kendra#ServiceNowBuildVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ServiceNowBuildVersionType: TypeAlias = Literal[
    "LONDON",
    "OTHERS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LONDON",
        "OTHERS",
    )
)


def serialize_aws_json_1_1(value: ServiceNowBuildVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceNowBuildVersionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceNowBuildVersionType value: {data!r}"
        )
    return cast(ServiceNowBuildVersionType, data)
