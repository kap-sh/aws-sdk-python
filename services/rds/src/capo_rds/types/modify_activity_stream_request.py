"""Generated from Smithy shape ``com.amazonaws.rds#ModifyActivityStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.audit_policy_state
    import capo_rds.types.string


class ModifyActivityStreamRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the RDS for Oracle or Microsoft SQL Server DB instance. For example, <code>arn:aws:rds:us-east-1:12345667890:db:my-orcl-db</code>.</p>"""
    audit_policy_state: NotRequired[
        "capo_rds.types.audit_policy_state.AuditPolicyState"
    ]
    """<p>The audit policy state. When a policy is unlocked, it is read/write. When it is locked, it is read-only. You can edit your audit policy only when the activity stream is unlocked or stopped.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyActivityStreamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "audit_policy_state" in value:
        import capo_rds.types.audit_policy_state

        capo_rds.types.audit_policy_state.serialize_query(
            value["audit_policy_state"], pairs, f"{key_prefix}AuditPolicyState"
        )


def deserialize_query(el: Element) -> ModifyActivityStreamRequest:
    out: ModifyActivityStreamRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_audit_policy_state = el.find("AuditPolicyState")
    if child_audit_policy_state is not None:
        import capo_rds.types.audit_policy_state

        out["audit_policy_state"] = capo_rds.types.audit_policy_state.deserialize_query(
            child_audit_policy_state
        )
    return out
