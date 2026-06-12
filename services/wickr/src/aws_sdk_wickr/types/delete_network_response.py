"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteNetworkResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string


class DeleteNetworkResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating that the network deletion has been initiated successfully.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteNetworkResponse:
    out: DeleteNetworkResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
