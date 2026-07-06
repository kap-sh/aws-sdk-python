"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.identifier
    import aws_sdk_appconfig.types.integer


class DeleteExtensionRequest(TypedDict, closed=True):
    extension_identifier: "aws_sdk_appconfig.types.identifier.Identifier"
    """<p>The name, ID, or Amazon Resource Name (ARN) of the extension you want to delete.</p>"""
    version_number: NotRequired["aws_sdk_appconfig.types.integer.Integer"]
    """<p>A specific version of an extension to delete. If omitted, the highest version is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExtensionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExtensionRequest:
    out: DeleteExtensionRequest = {}  # type: ignore[typeddict-item]
    return out
