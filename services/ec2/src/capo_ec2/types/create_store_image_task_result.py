"""Generated from Smithy shape ``com.amazonaws.ec2#CreateStoreImageTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class CreateStoreImageTaskResult(TypedDict, closed=True):
    object_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the stored AMI object in the S3 bucket.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateStoreImageTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "object_key" in value:
        pairs.append((f"{prefix}.ObjectKey", str(value["object_key"])))


def deserialize_ec2_query(el: Element) -> CreateStoreImageTaskResult:
    out: CreateStoreImageTaskResult = {}  # type: ignore[typeddict-item]
    child_object_key = el.find("ObjectKey")
    if child_object_key is not None:
        out["object_key"] = str(child_object_key.text or "")
    return out
