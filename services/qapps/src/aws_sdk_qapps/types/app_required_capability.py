"""Generated from Smithy shape ``com.amazonaws.qapps#AppRequiredCapability``."""

from typing import Literal, TypeAlias, cast

AppRequiredCapability: TypeAlias = Literal[
    "FileUpload",
    "CreatorMode",
    "RetrievalMode",
    "PluginMode",
]


# --- restJson1 ser/de ---
def serialize_json(value: AppRequiredCapability) -> str:
    return value


def deserialize_json(data: str) -> AppRequiredCapability:
    return cast(AppRequiredCapability, data)
