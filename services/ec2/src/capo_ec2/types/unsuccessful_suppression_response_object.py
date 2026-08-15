"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulSuppressionResponseObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class UnsuccessfulSuppressionResponseObject(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    suppress_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time when suppression was attempted.</p>"""
    resume_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time when health checks would have resumed.</p>"""
    reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason the suppression failed.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulSuppressionResponseObject,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "suppress_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["suppress_at"], pairs, f"{key_prefix}SuppressAt"
        )
    if "resume_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["resume_at"], pairs, f"{key_prefix}ResumeAt"
        )
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))


def deserialize_ec2_query(el: Element) -> UnsuccessfulSuppressionResponseObject:
    out: UnsuccessfulSuppressionResponseObject = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_suppress_at = el.find("suppressAt")
    if child_suppress_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["suppress_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_suppress_at
        )
    child_resume_at = el.find("resumeAt")
    if child_resume_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["resume_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_resume_at
        )
    child_reason = el.find("reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
