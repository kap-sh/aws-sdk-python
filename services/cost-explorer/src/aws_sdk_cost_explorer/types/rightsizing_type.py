"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

RightsizingType: TypeAlias = Literal[
    "TERMINATE",
    "MODIFY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERMINATE",
        "MODIFY",
    )
)


def serialize_aws_json_1_1(value: RightsizingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RightsizingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RightsizingType value: {data!r}")
    return cast(RightsizingType, data)
