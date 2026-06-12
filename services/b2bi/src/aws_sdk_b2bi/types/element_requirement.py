"""Generated from Smithy shape ``com.amazonaws.b2bi#ElementRequirement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

ElementRequirement: TypeAlias = Literal[
    "OPTIONAL",
    "MANDATORY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPTIONAL",
        "MANDATORY",
    )
)


def serialize_aws_json_1_0(value: ElementRequirement) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ElementRequirement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ElementRequirement value: {data!r}")
    return cast(ElementRequirement, data)
