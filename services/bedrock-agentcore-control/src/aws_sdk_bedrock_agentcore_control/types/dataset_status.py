"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

"""<p> Dataset lifecycle and operation status. </p>"""
DatasetStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "CREATE_FAILED",
    "UPDATE_FAILED",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "ACTIVE",
        "CREATE_FAILED",
        "UPDATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_json(value: DatasetStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetStatus value: {data!r}")
    return cast(DatasetStatus, data)
