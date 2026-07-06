"""Generated from Smithy shape ``com.amazonaws.greengrass#UpdateConnectivityInfoResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class UpdateConnectivityInfoResponse(TypedDict, closed=True):
    message: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A message about the connectivity info update request."""
    version: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The new version of the connectivity info."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectivityInfoResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> UpdateConnectivityInfoResponse:
    out: UpdateConnectivityInfoResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "Version" in data:
        out["version"] = data["Version"]
    return out
