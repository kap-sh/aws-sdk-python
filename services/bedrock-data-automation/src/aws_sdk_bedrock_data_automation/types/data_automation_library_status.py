"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Status of DataAutomationLibrary"""
DataAutomationLibraryStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: DataAutomationLibraryStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationLibraryStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataAutomationLibraryStatus value: {data!r}"
        )
    return cast(DataAutomationLibraryStatus, data)
