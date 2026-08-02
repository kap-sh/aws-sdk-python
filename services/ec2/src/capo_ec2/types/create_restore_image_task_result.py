"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRestoreImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CreateRestoreImageTaskResult(TypedDict, closed=True):
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The AMI ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateRestoreImageTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))


def deserialize_ec2_query(el: Element) -> CreateRestoreImageTaskResult:
    out: CreateRestoreImageTaskResult = {}  # type: ignore[typeddict-item]
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    return out
