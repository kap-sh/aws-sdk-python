"""Generated from Smithy shape ``com.amazonaws.rds#TargetHealth``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.target_health_reason
    import aws_sdk_rds.types.target_state


class TargetHealth(TypedDict):
    state: NotRequired["aws_sdk_rds.types.target_state.TargetState"]
    """<p>The current state of the connection health lifecycle for the RDS Proxy target. The following is a typical lifecycle example for the states of an RDS Proxy target:</p> <p> <code>registering</code> &gt; <code>unavailable</code> &gt; <code>available</code> &gt; <code>unavailable</code> &gt; <code>available</code> </p>"""
    reason: NotRequired["aws_sdk_rds.types.target_health_reason.TargetHealthReason"]
    """<p>The reason for the current health <code>State</code> of the RDS Proxy target.</p>"""
    description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A description of the health of the RDS Proxy target. If the <code>State</code> is <code>AVAILABLE</code>, a description is not included.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_rds.types.target_state

        aws_sdk_rds.types.target_state.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "reason" in value:
        import aws_sdk_rds.types.target_health_reason

        aws_sdk_rds.types.target_health_reason.serialize_query(
            value["reason"], pairs, f"{prefix}.Reason"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> TargetHealth:
    out: TargetHealth = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_rds.types.target_state

        out["state"] = aws_sdk_rds.types.target_state.deserialize_query(child_state)
    child_reason = el.find("Reason")
    if child_reason is not None:
        import aws_sdk_rds.types.target_health_reason

        out["reason"] = aws_sdk_rds.types.target_health_reason.deserialize_query(
            child_reason
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
