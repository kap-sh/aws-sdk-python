"""Generated from Smithy shape ``com.amazonaws.schemas#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.synthesized_json__string


class PutResourcePolicyRequest(TypedDict, closed=True):
    policy: NotRequired[
        "aws_sdk_schemas.types.synthesized_json__string.SynthesizedJson__string"
    ]
    """<p>The resource-based policy.</p>"""
    registry_name: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The name of the registry.</p>"""
    revision_id: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The revision ID of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    return out
