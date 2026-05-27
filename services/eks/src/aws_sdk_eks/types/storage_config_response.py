"""Generated from Smithy shape ``com.amazonaws.eks#StorageConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.block_storage


class StorageConfigResponse(TypedDict):
    block_storage: NotRequired["aws_sdk_eks.types.block_storage.BlockStorage"]
    """<p>Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigResponse) -> dict:
    out: dict = {}
    if "block_storage" in value:
        import aws_sdk_eks.types.block_storage

        out["blockStorage"] = aws_sdk_eks.types.block_storage.serialize_json(
            value["block_storage"]
        )
    return out


def deserialize_json(data: dict) -> StorageConfigResponse:
    out: StorageConfigResponse = {}  # type: ignore[typeddict-item]
    if "blockStorage" in data:
        import aws_sdk_eks.types.block_storage

        out["block_storage"] = aws_sdk_eks.types.block_storage.deserialize_json(
            data["blockStorage"]
        )
    return out
