"""Generated from Smithy shape ``com.amazonaws.batch#EksEmptyDir``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.quantity
    import aws_sdk_batch.types.string


class EksEmptyDir(TypedDict):
    medium: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The medium to store the volume. The default value is an empty string, which uses the storage of the node.</p> <dl> <dt>\"\"</dt> <dd> <p> <b>(Default)</b> Use the disk storage of the node.</p> </dd> <dt>\"Memory\"</dt> <dd> <p>Use the <code>tmpfs</code> volume that's backed by the RAM of the node. Contents of the volume are lost when the node reboots, and any storage on the volume counts against the container's memory limit.</p> </dd> </dl>"""
    size_limit: NotRequired["aws_sdk_batch.types.quantity.Quantity"]
    """<p>The maximum size of the volume. By default, there's no maximum size defined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksEmptyDir) -> dict:
    out: dict = {}
    if "medium" in value:
        out["medium"] = value["medium"]
    if "size_limit" in value:
        out["sizeLimit"] = value["size_limit"]
    return out


def deserialize_json(data: dict) -> EksEmptyDir:
    out: EksEmptyDir = {}  # type: ignore[typeddict-item]
    if "medium" in data:
        out["medium"] = data["medium"]
    if "sizeLimit" in data:
        out["size_limit"] = data["sizeLimit"]
    return out
