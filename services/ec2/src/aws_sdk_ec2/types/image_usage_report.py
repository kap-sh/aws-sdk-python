"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReport``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_usage_report_id
    import aws_sdk_ec2.types.image_usage_report_state
    import aws_sdk_ec2.types.image_usage_report_state_reason
    import aws_sdk_ec2.types.image_usage_resource_type_list
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.user_id_list


class ImageUsageReport(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image that was specified when the report was created.</p>"""
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    resource_types: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_list.ImageUsageResourceTypeList"
    ]
    """<p>The resource types that were specified when the report was created.</p>"""
    account_ids: NotRequired["aws_sdk_ec2.types.user_id_list.UserIdList"]
    """<p>The IDs of the Amazon Web Services accounts that were specified when the report was created.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_state.ImageUsageReportState"
    ]
    """<p>The current state of the report. Possible values:</p> <ul> <li> <p> <code>available</code> - The report is available to view.</p> </li> <li> <p> <code>pending</code> - The report is being created and not available to view.</p> </li> <li> <p> <code>error</code> - The report could not be created.</p> </li> </ul>"""
    state_reason: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_state_reason.ImageUsageReportStateReason"
    ]
    """<p>Provides additional details when the report is in an <code>error</code> state.</p>"""
    creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the report was created.</p>"""
    expiration_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when Amazon EC2 will delete the report (30 days after the report was created).</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the report.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageReport, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "report_id" in value:
        pairs.append((f"{prefix}.ReportId", str(value["report_id"])))
    if "resource_types" in value:
        import aws_sdk_ec2.types.image_usage_resource_type_list

        aws_sdk_ec2.types.image_usage_resource_type_list.serialize_ec2_query(
            value["resource_types"], pairs, f"{prefix}.ResourceTypeSet"
        )
    if "account_ids" in value:
        import aws_sdk_ec2.types.user_id_list

        aws_sdk_ec2.types.user_id_list.serialize_ec2_query(
            value["account_ids"], pairs, f"{prefix}.AccountIdSet"
        )
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "state_reason" in value:
        pairs.append((f"{prefix}.StateReason", str(value["state_reason"])))
    if "creation_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{prefix}.CreationTime"
        )
    if "expiration_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["expiration_time"], pairs, f"{prefix}.ExpirationTime"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageReport:
    out: ImageUsageReport = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_report_id = el.find("ReportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    if el.find("ResourceTypeSet") is not None:
        import aws_sdk_ec2.types.image_usage_resource_type_list

        out["resource_types"] = (
            aws_sdk_ec2.types.image_usage_resource_type_list.deserialize_ec2_query(
                el, "ResourceTypeSet"
            )
        )
    if el.find("AccountIdSet") is not None:
        import aws_sdk_ec2.types.user_id_list

        out["account_ids"] = aws_sdk_ec2.types.user_id_list.deserialize_ec2_query(
            el, "AccountIdSet"
        )
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_creation_time = el.find("CreationTime")
    if child_creation_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["creation_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_time
            )
        )
    child_expiration_time = el.find("ExpirationTime")
    if child_expiration_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["expiration_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_expiration_time
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
