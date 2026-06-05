"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRestoreImageTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class CreateRestoreImageTaskResult(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The AMI ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRestoreImageTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "image_id" in value:
        pairs.append((f"{prefix}.ImageId", str(value["image_id"])))


def deserialize_ec2_query(el: Element) -> CreateRestoreImageTaskResult:
    out: CreateRestoreImageTaskResult = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    return out
