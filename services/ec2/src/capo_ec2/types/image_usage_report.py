"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.image_id
    import capo_ec2.types.image_usage_report_id
    import capo_ec2.types.image_usage_report_state
    import capo_ec2.types.image_usage_report_state_reason
    import capo_ec2.types.image_usage_resource_type_list
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.tag_list
    import capo_ec2.types.user_id_list


class ImageUsageReport(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the image that was specified when the report was created.</p>"""
    report_id: NotRequired["capo_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    resource_types: NotRequired[
        "capo_ec2.types.image_usage_resource_type_list.ImageUsageResourceTypeList"
    ]
    """<p>The resource types that were specified when the report was created.</p>"""
    account_ids: NotRequired["capo_ec2.types.user_id_list.UserIdList"]
    """<p>The IDs of the Amazon Web Services accounts that were specified when the report was created.</p>"""
    state: NotRequired["capo_ec2.types.image_usage_report_state.ImageUsageReportState"]
    """<p>The current state of the report. Possible values:</p> <ul> <li> <p> <code>available</code> - The report is available to view.</p> </li> <li> <p> <code>pending</code> - The report is being created and not available to view.</p> </li> <li> <p> <code>error</code> - The report could not be created.</p> </li> </ul>"""
    state_reason: NotRequired[
        "capo_ec2.types.image_usage_report_state_reason.ImageUsageReportStateReason"
    ]
    """<p>Provides additional details when the report is in an <code>error</code> state.</p>"""
    creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the report was created.</p>"""
    expiration_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when Amazon EC2 will delete the report (30 days after the report was created).</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the report.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageReport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "report_id" in value:
        pairs.append((f"{key_prefix}ReportId", str(value["report_id"])))
    if "resource_types" in value:
        import capo_ec2.types.image_usage_resource_type_list

        capo_ec2.types.image_usage_resource_type_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{key_prefix}ResourceTypeSet"
        )
    if "account_ids" in value:
        import capo_ec2.types.user_id_list

        capo_ec2.types.user_id_list.serialize_ec2_query(
            value["account_ids"], pairs, f"{key_prefix}AccountIdSet"
        )
    if "state" in value:
        pairs.append((f"{key_prefix}State", str(value["state"])))
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "expiration_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["expiration_time"], pairs, f"{key_prefix}ExpirationTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageReport:
    out: ImageUsageReport = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_report_id = el.find("reportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    child_resource_types = el.find("resourceTypeSet")
    if child_resource_types is not None:
        import capo_ec2.types.image_usage_resource_type_list

        out["resource_types"] = (
            capo_ec2.types.image_usage_resource_type_list.deserialize_ec2_query(
                child_resource_types
            )
        )
    child_account_ids = el.find("accountIdSet")
    if child_account_ids is not None:
        import capo_ec2.types.user_id_list

        out["account_ids"] = capo_ec2.types.user_id_list.deserialize_ec2_query(
            child_account_ids
        )
    child_state = el.find("state")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_state_reason = el.find("stateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_time
            )
        )
    child_expiration_time = el.find("expirationTime")
    if child_expiration_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["expiration_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_expiration_time
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
