"""Generated from Smithy shape ``com.amazonaws.ec2#ImageUsageReportEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_usage_report_id
    import aws_sdk_ec2.types.image_usage_resource_type_name
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageUsageReportEntry(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_ec2.types.image_usage_resource_type_name.ImageUsageResourceTypeName"
    ]
    """<p>The type of resource (<code>ec2:Instance</code> or <code>ec2:LaunchTemplate</code>).</p>"""
    report_id: NotRequired["aws_sdk_ec2.types.image_usage_report_id.ImageUsageReportId"]
    """<p>The ID of the report.</p>"""
    usage_count: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of times resources of this type reference this image in the account.</p>"""
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that uses the image.</p>"""
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the image.</p>"""
    report_creation_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the report creation was initiated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageUsageReportEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "report_id" in value:
        pairs.append((f"{prefix}.ReportId", str(value["report_id"])))
    if "usage_count" in value:
        pairs.append((f"{prefix}.UsageCount", str(value["usage_count"])))
    if "account_id" in value:
        pairs.append((f"{prefix}.AccountId", str(value["account_id"])))
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "report_creation_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["report_creation_time"], pairs, f"{prefix}.ReportCreationTime"
        )


def deserialize_ec2_query(el: Element) -> ImageUsageReportEntry:
    out: ImageUsageReportEntry = {}  # type: ignore[typeddict-item]
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_report_id = el.find("ReportId")
    if child_report_id is not None:
        out["report_id"] = str(child_report_id.text or "")
    child_usage_count = el.find("UsageCount")
    if child_usage_count is not None:
        out["usage_count"] = int(child_usage_count.text or "")
    child_account_id = el.find("AccountId")
    if child_account_id is not None:
        out["account_id"] = str(child_account_id.text or "")
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_report_creation_time = el.find("ReportCreationTime")
    if child_report_creation_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["report_creation_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_report_creation_time
            )
        )
    return out
