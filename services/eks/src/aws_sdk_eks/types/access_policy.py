"""Generated from Smithy shape ``com.amazonaws.eks#AccessPolicy``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class AccessPolicy(TypedDict):
    name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the access policy.</p>"""
    arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of the access policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessPolicy) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> AccessPolicy:
    out: AccessPolicy = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
