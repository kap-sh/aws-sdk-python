"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryStatus``."""

from typing import Literal, TypeAlias, cast

"""Status of DataAutomationLibrary"""
DataAutomationLibraryStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAutomationLibraryStatus:
    return cast(DataAutomationLibraryStatus, data)
