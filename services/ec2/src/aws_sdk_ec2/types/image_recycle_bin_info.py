"""Generated from Smithy shape ``com.amazonaws.ec2#ImageRecycleBinInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class ImageRecycleBinInfo(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the AMI.</p>"""
    recycle_bin_enter_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI is to be permanently deleted from the Recycle Bin.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageRecycleBinInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "recycle_bin_enter_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_enter_time"], pairs, f"{prefix}.RecycleBinEnterTime"
        )
    if "recycle_bin_exit_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_exit_time"], pairs, f"{prefix}.RecycleBinExitTime"
        )


def deserialize_ec2_query(el: Element) -> ImageRecycleBinInfo:
    out: ImageRecycleBinInfo = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_recycle_bin_enter_time = el.find("RecycleBinEnterTime")
    if child_recycle_bin_enter_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["recycle_bin_enter_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_enter_time
            )
        )
    child_recycle_bin_exit_time = el.find("RecycleBinExitTime")
    if child_recycle_bin_exit_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["recycle_bin_exit_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_exit_time
            )
        )
    return out
