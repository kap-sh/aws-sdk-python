"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PolicyAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.object_identifier
    import aws_sdk_clouddirectory.types.policy_type


class PolicyAttachment(TypedDict):
    policy_id: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The ID of <code>PolicyAttachment</code>.</p>"""
    object_identifier: NotRequired[
        "aws_sdk_clouddirectory.types.object_identifier.ObjectIdentifier"
    ]
    """<p>The <code>ObjectIdentifier</code> that is associated with <code>PolicyAttachment</code>.</p>"""
    policy_type: NotRequired["aws_sdk_clouddirectory.types.policy_type.PolicyType"]
    """<p>The type of policy that can be associated with <code>PolicyAttachment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyAttachment) -> dict:
    out: dict = {}
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "object_identifier" in value:
        out["ObjectIdentifier"] = value["object_identifier"]
    if "policy_type" in value:
        out["PolicyType"] = value["policy_type"]
    return out


def deserialize_json(data: dict) -> PolicyAttachment:
    out: PolicyAttachment = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    if "ObjectIdentifier" in data:
        out["object_identifier"] = data["ObjectIdentifier"]
    if "PolicyType" in data:
        out["policy_type"] = data["PolicyType"]
    return out
