"""Generated from Smithy shape ``com.amazonaws.rds#CustomDBEngineVersionAMI``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class CustomDBEngineVersionAMI(TypedDict, closed=True):
    image_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A value that indicates the ID of the AMI.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A value that indicates the status of a custom engine version (CEV).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CustomDBEngineVersionAMI, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> CustomDBEngineVersionAMI:
    out: CustomDBEngineVersionAMI = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
