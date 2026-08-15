"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.aggregation_status_enum
    import capo_ec2.types.application_status_check_enum
    import capo_ec2.types.application_status_check_id
    import capo_ec2.types.application_status_reason
    import capo_ec2.types.millisecond_date_time


class ApplicationStatusDetail(TypedDict, closed=True):
    application_status_check_id: NotRequired[
        "capo_ec2.types.application_status_check_id.ApplicationStatusCheckId"
    ]
    """<p>The ID of the application status check.</p>"""
    check_update_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the check was last updated.</p>"""
    aggregation: NotRequired[
        "capo_ec2.types.aggregation_status_enum.AggregationStatusEnum"
    ]
    """<p>The aggregation setting for the application status check. When set to <code>included</code>, the result of this check contributes to the instance-level application status. When set to <code>excluded</code>, the check runs independently and does not affect the instance-level status.</p>"""
    status: NotRequired[
        "capo_ec2.types.application_status_check_enum.ApplicationStatusCheckEnum"
    ]
    """<p>The status of the individual application status check. Possible values:</p> <ul> <li> <p> <code>passed</code> – The check reached its success threshold.</p> </li> <li> <p> <code>failed</code> – The check reached its failure threshold.</p> </li> <li> <p> <code>initializing</code> – The check is initializing or has not reached a success or failure threshold.</p> </li> <li> <p> <code>insufficient-data</code> – The check does not have enough data to determine a result.</p> </li> <li> <p> <code>not-applicable</code> – The check does not apply to the instance.</p> </li> </ul> <p>This value reflects the check result and is not affected by aggregation or suppression.</p>"""
    status_time_stamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time of the last status update for this check.</p>"""
    status_since: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the current status started for this check.</p>"""
    reason: NotRequired[
        "capo_ec2.types.application_status_reason.ApplicationStatusReason"
    ]
    """<p>The reason for the current status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatusDetail, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check_id" in value:
        pairs.append(
            (
                f"{key_prefix}ApplicationStatusCheckId",
                str(value["application_status_check_id"]),
            )
        )
    if "check_update_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["check_update_time"], pairs, f"{key_prefix}CheckUpdateTime"
        )
    if "aggregation" in value:
        import capo_ec2.types.aggregation_status_enum

        capo_ec2.types.aggregation_status_enum.serialize_ec2_query(
            value["aggregation"], pairs, f"{key_prefix}Aggregation"
        )
    if "status" in value:
        import capo_ec2.types.application_status_check_enum

        capo_ec2.types.application_status_check_enum.serialize_ec2_query(
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
    if "reason" in value:
        import capo_ec2.types.application_status_reason

        capo_ec2.types.application_status_reason.serialize_ec2_query(
            value["reason"], pairs, f"{key_prefix}Reason"
        )


def deserialize_ec2_query(el: Element) -> ApplicationStatusDetail:
    out: ApplicationStatusDetail = {}  # type: ignore[typeddict-item]
    child_application_status_check_id = el.find("applicationStatusCheckId")
    if child_application_status_check_id is not None:
        out["application_status_check_id"] = str(
            child_application_status_check_id.text or ""
        )
    child_check_update_time = el.find("checkUpdateTime")
    if child_check_update_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["check_update_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_check_update_time
            )
        )
    child_aggregation = el.find("aggregation")
    if child_aggregation is not None:
        import capo_ec2.types.aggregation_status_enum

        out["aggregation"] = (
            capo_ec2.types.aggregation_status_enum.deserialize_ec2_query(
                child_aggregation
            )
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.application_status_check_enum

        out["status"] = (
            capo_ec2.types.application_status_check_enum.deserialize_ec2_query(
                child_status
            )
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
    child_reason = el.find("reason")
    if child_reason is not None:
        import capo_ec2.types.application_status_reason

        out["reason"] = capo_ec2.types.application_status_reason.deserialize_ec2_query(
            child_reason
        )
    return out
