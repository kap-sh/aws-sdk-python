"""Generated from Smithy shape ``com.amazonaws.qbusiness#BrowserExtensionList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.browser_extension

BrowserExtensionList: TypeAlias = list["aws_sdk_qbusiness.types.browser_extension.BrowserExtension"]


# --- restJson1 ser/de ---
def serialize_json(value: BrowserExtensionList) -> list:
    return list(value)


def deserialize_json(data: list) -> BrowserExtensionList:
    return list(data)