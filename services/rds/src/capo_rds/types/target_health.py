"""Generated from Smithy shape ``com.amazonaws.rds#TargetHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.target_health_reason
    import capo_rds.types.target_state


class TargetHealth(TypedDict, closed=True):
    state: NotRequired["capo_rds.types.target_state.TargetState"]
    """<p>The current state of the connection health lifecycle for the RDS Proxy target. The following is a typical lifecycle example for the states of an RDS Proxy target:</p> <p> <code>registering</code> &gt; <code>unavailable</code> &gt; <code>available</code> &gt; <code>unavailable</code> &gt; <code>available</code> </p>"""
    reason: NotRequired["capo_rds.types.target_health_reason.TargetHealthReason"]
    """<p>The reason for the current health <code>State</code> of the RDS Proxy target.</p>"""
    description: NotRequired["capo_rds.types.string.String"]
    """<p>A description of the health of the RDS Proxy target. If the <code>State</code> is <code>AVAILABLE</code>, a description is not included.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetHealth, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "state" in value:
        import capo_rds.types.target_state

        capo_rds.types.target_state.serialize_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "reason" in value:
        import capo_rds.types.target_health_reason

        capo_rds.types.target_health_reason.serialize_query(
            value["reason"], pairs, f"{key_prefix}Reason"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_query(el: Element) -> TargetHealth:
    out: TargetHealth = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import capo_rds.types.target_state

        out["state"] = capo_rds.types.target_state.deserialize_query(child_state)
    child_reason = el.find("Reason")
    if child_reason is not None:
        import capo_rds.types.target_health_reason

        out["reason"] = capo_rds.types.target_health_reason.deserialize_query(
            child_reason
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
