"""Generated from Smithy shape ``com.amazonaws.ec2#ImageWatermarkFilterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string


class ImageWatermarkFilterResponse(TypedDict, closed=True):
    watermark_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The <code>accountId:name</code> of the watermark. Supports wildcards (<code>*</code>, <code>?</code>).</p>"""
    source_image_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region where the watermark was originally created. Supports wildcards (<code>*</code>, <code>?</code>).</p>"""
    maximum_days_since_source_image_created: NotRequired[
        "capo_ec2.types.integer.Integer"
    ]
    """<p>The maximum number of days that have elapsed since the source image was created.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""
    maximum_days_since_watermark_created: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of days that have elapsed since the watermark was attached to the image.</p> <p>Constraints: Minimum value of 0. Maximum value of 2147483647.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImageWatermarkFilterResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "watermark_key" in value:
        pairs.append((f"{key_prefix}WatermarkKey", str(value["watermark_key"])))
    if "source_image_region" in value:
        pairs.append(
            (f"{key_prefix}SourceImageRegion", str(value["source_image_region"]))
        )
    if "maximum_days_since_source_image_created" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumDaysSinceSourceImageCreated",
                str(value["maximum_days_since_source_image_created"]),
            )
        )
    if "maximum_days_since_watermark_created" in value:
        pairs.append(
            (
                f"{key_prefix}MaximumDaysSinceWatermarkCreated",
                str(value["maximum_days_since_watermark_created"]),
            )
        )


def deserialize_ec2_query(el: Element) -> ImageWatermarkFilterResponse:
    out: ImageWatermarkFilterResponse = {}  # type: ignore[typeddict-item]
    child_watermark_key = el.find("watermarkKey")
    if child_watermark_key is not None:
        out["watermark_key"] = str(child_watermark_key.text or "")
    child_source_image_region = el.find("sourceImageRegion")
    if child_source_image_region is not None:
        out["source_image_region"] = str(child_source_image_region.text or "")
    child_maximum_days_since_source_image_created = el.find(
        "maximumDaysSinceSourceImageCreated"
    )
    if child_maximum_days_since_source_image_created is not None:
        out["maximum_days_since_source_image_created"] = int(
            child_maximum_days_since_source_image_created.text or ""
        )
    child_maximum_days_since_watermark_created = el.find(
        "maximumDaysSinceWatermarkCreated"
    )
    if child_maximum_days_since_watermark_created is not None:
        out["maximum_days_since_watermark_created"] = int(
            child_maximum_days_since_watermark_created.text or ""
        )
    return out
