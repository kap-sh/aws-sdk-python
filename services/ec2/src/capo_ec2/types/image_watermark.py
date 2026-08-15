"""Generated from Smithy shape ``com.amazonaws.ec2#ImageWatermark``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class ImageWatermark(TypedDict, closed=True):
    watermark_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The watermark identifier, in <code>accountId:watermarkName</code> format (for example, <code>123456789012:approvedAmi</code>). The <code>accountId</code> portion is the Amazon Web Services account ID of the watermark creator. The <code>watermarkName</code> portion is customer-provided.</p>"""
    source_image_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region where the watermark was originally attached.</p>"""
    source_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI to which the watermark was originally attached.</p>"""
    source_image_creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The creation date of the source AMI, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>.<i>ssssss</i>+<i>HH</i>:<i>MM</i>.</p>"""
    watermark_creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time the watermark was attached to the AMI, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>.<i>ssssss</i>+<i>HH</i>:<i>MM</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageWatermark, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "watermark_key" in value:
        pairs.append((f"{key_prefix}WatermarkKey", str(value["watermark_key"])))
    if "source_image_region" in value:
        pairs.append(
            (f"{key_prefix}SourceImageRegion", str(value["source_image_region"]))
        )
    if "source_image_id" in value:
        pairs.append((f"{key_prefix}SourceImageId", str(value["source_image_id"])))
    if "source_image_creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["source_image_creation_time"],
            pairs,
            f"{key_prefix}SourceImageCreationTime",
        )
    if "watermark_creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["watermark_creation_time"],
            pairs,
            f"{key_prefix}WatermarkCreationTime",
        )


def deserialize_ec2_query(el: Element) -> ImageWatermark:
    out: ImageWatermark = {}  # type: ignore[typeddict-item]
    child_watermark_key = el.find("watermarkKey")
    if child_watermark_key is not None:
        out["watermark_key"] = str(child_watermark_key.text or "")
    child_source_image_region = el.find("sourceImageRegion")
    if child_source_image_region is not None:
        out["source_image_region"] = str(child_source_image_region.text or "")
    child_source_image_id = el.find("sourceImageId")
    if child_source_image_id is not None:
        out["source_image_id"] = str(child_source_image_id.text or "")
    child_source_image_creation_time = el.find("sourceImageCreationTime")
    if child_source_image_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["source_image_creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_source_image_creation_time
            )
        )
    child_watermark_creation_time = el.find("watermarkCreationTime")
    if child_watermark_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["watermark_creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_watermark_creation_time
            )
        )
    return out
