"""Generated from Smithy shape ``com.amazonaws.auditmanager#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_auditmanager.types.audit_manager_arn.AuditManagerArn"
    """<p> The Amazon Resource Name (ARN) of the specified resource. </p>"""
    tag_keys: "capo_auditmanager.types.tag_key_list.TagKeyList"
    """<p> The name or key of the tag. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
