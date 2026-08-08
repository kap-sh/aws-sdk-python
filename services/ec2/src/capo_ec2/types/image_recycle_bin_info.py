"""Generated from Smithy shape ``com.amazonaws.ec2#ImageRecycleBinInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class ImageRecycleBinInfo(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the AMI.</p>"""
    recycle_bin_enter_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the AMI is to be permanently deleted from the Recycle Bin.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageRecycleBinInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "recycle_bin_enter_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_enter_time"], pairs, f"{key_prefix}RecycleBinEnterTime"
        )
    if "recycle_bin_exit_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_exit_time"], pairs, f"{key_prefix}RecycleBinExitTime"
        )


def deserialize_ec2_query(el: Element) -> ImageRecycleBinInfo:
    out: ImageRecycleBinInfo = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("imageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_recycle_bin_enter_time = el.find("recycleBinEnterTime")
    if child_recycle_bin_enter_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_enter_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_enter_time
            )
        )
    child_recycle_bin_exit_time = el.find("recycleBinExitTime")
    if child_recycle_bin_exit_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_exit_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_exit_time
            )
        )
    return out
