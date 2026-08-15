"""Generated from Smithy shape ``com.amazonaws.ec2#AttachImageWatermarkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.image_watermark_name_request


class AttachImageWatermarkRequest(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    watermark_name: NotRequired[
        "capo_ec2.types.image_watermark_name_request.ImageWatermarkNameRequest"
    ]
    """<p>The name for the watermark. Combined with the caller's account ID to form the <code>WatermarkKey</code> (<code>accountId:watermarkName</code>).</p> <p>Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachImageWatermarkRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "watermark_name" in value:
        pairs.append((f"{key_prefix}WatermarkName", str(value["watermark_name"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AttachImageWatermarkRequest:
    out: AttachImageWatermarkRequest = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_watermark_name = el.find("WatermarkName")
    if child_watermark_name is not None:
        out["watermark_name"] = str(child_watermark_name.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
