"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleScreenshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class GetConsoleScreenshotResult(TypedDict, closed=True):
    image_data: NotRequired["capo_ec2.types.string.String"]
    """<p>The data that comprises the image.</p>"""
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetConsoleScreenshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_data" in value:
        pairs.append((f"{key_prefix}ImageData", str(value["image_data"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))


def deserialize_ec2_query(el: Element) -> GetConsoleScreenshotResult:
    out: GetConsoleScreenshotResult = {}  # type: ignore[typeddict-item]
    child_image_data = el.find("ImageData")
    if child_image_data is not None:
        out["image_data"] = str(child_image_data.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    return out
