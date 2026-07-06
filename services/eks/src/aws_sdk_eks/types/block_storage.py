"""Generated from Smithy shape ``com.amazonaws.eks#BlockStorage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boxed_boolean


class BlockStorage(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockStorage) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> BlockStorage:
    out: BlockStorage = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
