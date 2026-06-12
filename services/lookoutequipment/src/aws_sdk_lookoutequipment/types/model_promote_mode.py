"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ModelPromoteMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

ModelPromoteMode: TypeAlias = Literal[
    "MANAGED",
    "MANUAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "MANUAL",
    )
)


def serialize_aws_json_1_0(value: ModelPromoteMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ModelPromoteMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPromoteMode value: {data!r}")
    return cast(ModelPromoteMode, data)
