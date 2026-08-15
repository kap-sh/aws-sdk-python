"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_detail_set
    import capo_ec2.types.application_status_enum
    import capo_ec2.types.millisecond_date_time


class ApplicationStatus(TypedDict, closed=True):
    status: NotRequired["capo_ec2.types.application_status_enum.ApplicationStatusEnum"]
    """<p>The current instance-level application status. This status is derived from application status checks with <code>Aggregation</code> set to <code>included</code>. Possible values:</p> <ul> <li> <p> <code>ok</code> – All included checks passed.</p> </li> <li> <p> <code>impaired</code> – At least one included check failed.</p> </li> <li> <p> <code>initializing</code> – At least one included check is initializing, and no included check is impaired.</p> </li> <li> <p> <code>insufficient-data</code> – At least one included check has insufficient data, and no included check is impaired or initializing.</p> </li> <li> <p> <code>not-applicable</code> – No checks with <code>Aggregation</code> set to <code>included</code> apply to the instance.</p> </li> <li> <p> <code>suppressed</code> – Application status reporting is suppressed for the instance.</p> </li> </ul> <p>Checks with <code>Aggregation</code> set to <code>excluded</code> do not affect this value.</p>"""
    status_time_stamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time of the last status update.</p>"""
    status_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the current status started.</p>"""
    resume_at: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time when application status reporting resumes after suppression.</p>"""
    details: NotRequired[
        "capo_ec2.types.application_status_detail_set.ApplicationStatusDetailSet"
    ]
    """<p>Details about the application status checks for the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ec2.types.application_status_enum

        capo_ec2.types.application_status_enum.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "status_time_stamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["status_time_stamp"], pairs, f"{key_prefix}StatusTimeStamp"
        )
    if "status_since" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["status_since"], pairs, f"{key_prefix}StatusSince"
        )
    if "resume_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["resume_at"], pairs, f"{key_prefix}ResumeAt"
        )
    if "details" in value:
        import capo_ec2.types.application_status_detail_set

        capo_ec2.types.application_status_detail_set.serialize_ec2_query(
            value["details"], pairs, f"{key_prefix}DetailSet"
        )


def deserialize_ec2_query(el: Element) -> ApplicationStatus:
    out: ApplicationStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.application_status_enum

        out["status"] = capo_ec2.types.application_status_enum.deserialize_ec2_query(
            child_status
        )
    child_status_time_stamp = el.find("statusTimeStamp")
    if child_status_time_stamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["status_time_stamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_status_time_stamp
            )
        )
    child_status_since = el.find("statusSince")
    if child_status_since is not None:
        import capo_ec2.types.millisecond_date_time

        out["status_since"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_status_since
            )
        )
    child_resume_at = el.find("resumeAt")
    if child_resume_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["resume_at"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_resume_at
        )
    child_details = el.find("detailSet")
    if child_details is not None:
        import capo_ec2.types.application_status_detail_set

        out["details"] = (
            capo_ec2.types.application_status_detail_set.deserialize_ec2_query(
                child_details
            )
        )
    return out
