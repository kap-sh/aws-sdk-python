"""Generated from Smithy shape ``com.amazonaws.eks#License``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class License(TypedDict):
    id: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>An id associated with an EKS Anywhere subscription license.</p>"""
    token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>An optional license token that can be used for extended support verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: License) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "token" in value:
        out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> License:
    out: License = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "token" in data:
        out["token"] = data["token"]
    return out
