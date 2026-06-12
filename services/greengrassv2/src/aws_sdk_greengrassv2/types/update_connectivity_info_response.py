"""Generated from Smithy shape ``com.amazonaws.greengrassv2#UpdateConnectivityInfoResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class UpdateConnectivityInfoResponse(TypedDict):
    version: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The new version of the connectivity information for the core device.</p>"""
    message: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>A message about the connectivity information update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityInfoResponse) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateConnectivityInfoResponse:
    out: UpdateConnectivityInfoResponse = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
