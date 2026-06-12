"""Generated from Smithy shape ``com.amazonaws.route53resolver#Validation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

Validation: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
        "USE_LOCAL_RESOURCE_SETTING",
    )
)


def serialize_aws_json_1_1(value: Validation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Validation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Validation value: {data!r}")
    return cast(Validation, data)
