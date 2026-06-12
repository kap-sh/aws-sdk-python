"""Generated from Smithy shape ``com.amazonaws.configservice#ChronologicalOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ChronologicalOrder: TypeAlias = Literal[
    "Reverse",
    "Forward",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Reverse",
        "Forward",
    )
)


def serialize_aws_json_1_1(value: ChronologicalOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChronologicalOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChronologicalOrder value: {data!r}")
    return cast(ChronologicalOrder, data)
