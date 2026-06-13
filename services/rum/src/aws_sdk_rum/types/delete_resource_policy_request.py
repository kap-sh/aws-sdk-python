"""Generated from Smithy shape ``com.amazonaws.rum#DeleteResourcePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rum.types.app_monitor_name
    import aws_sdk_rum.types.policy_revision_id


class DeleteResourcePolicyRequest(TypedDict):
    name: "aws_sdk_rum.types.app_monitor_name.AppMonitorName"
    """<p>The app monitor that you want to remove the resource policy from.</p>"""
    policy_revision_id: NotRequired[
        "aws_sdk_rum.types.policy_revision_id.PolicyRevisionId"
    ]
    """<p>Specifies a specific policy revision to delete. Provide a <code>PolicyRevisionId</code> to ensure an atomic delete operation. If the revision ID that you provide doesn't match the latest policy revision ID, the request will be rejected with an <code>InvalidPolicyRevisionIdException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourcePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteResourcePolicyRequest:
    out: DeleteResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
