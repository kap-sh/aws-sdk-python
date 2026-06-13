"""Generated from Smithy shape ``com.amazonaws.bedrock#DataRetentionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

"""<p>The data retention mode for the account. Valid values are:</p> <ul> <li> <p> <code>default</code> – The standard data handling for the model applies.</p> </li> <li> <p> <code>none</code> – Zero data retention.</p> </li> <li> <p> <code>provider_data_share</code> – Data may be shared with the model provider.</p> </li> <li> <p> <code>inherit</code> – No data retention mode is set at this scope.</p> </li> </ul>"""
DataRetentionMode: TypeAlias = Literal[
    "default",
    "none",
    "provider_data_share",
    "inherit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "none",
        "provider_data_share",
        "inherit",
    )
)


def serialize_json(value: DataRetentionMode) -> str:
    return value


def deserialize_json(data: str) -> DataRetentionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataRetentionMode value: {data!r}")
    return cast(DataRetentionMode, data)
