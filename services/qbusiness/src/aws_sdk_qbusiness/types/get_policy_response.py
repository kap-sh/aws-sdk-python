"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPolicyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.string


class GetPolicyResponse(TypedDict):
    policy: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The JSON representation of the permission policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    return out
