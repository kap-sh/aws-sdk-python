"""Generated from Smithy shape ``com.amazonaws.appconfig#GetExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.identifier
    import capo_appconfig.types.integer


class GetExtensionRequest(TypedDict, closed=True):
    extension_identifier: "capo_appconfig.types.identifier.Identifier"
    """<p>The name, the ID, or the Amazon Resource Name (ARN) of the extension.</p>"""
    version_number: NotRequired["capo_appconfig.types.integer.Integer"]
    """<p>The extension version number. If no version number was defined, AppConfig uses the highest version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExtensionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExtensionRequest:
    out: GetExtensionRequest = {}  # type: ignore[typeddict-item]
    return out
