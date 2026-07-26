"""Generated from Smithy shape ``com.amazonaws.greengrassv2#CancelDeploymentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.non_empty_string


class CancelDeploymentResponse(TypedDict, closed=True):
    message: NotRequired["capo_greengrassv2.types.non_empty_string.NonEmptyString"]
    """<p>A message that communicates if the cancel was successful.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelDeploymentResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> CancelDeploymentResponse:
    out: CancelDeploymentResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
