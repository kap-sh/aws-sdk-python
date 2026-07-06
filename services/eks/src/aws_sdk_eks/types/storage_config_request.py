"""Generated from Smithy shape ``com.amazonaws.eks#StorageConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.block_storage


class StorageConfigRequest(TypedDict, closed=True):
    block_storage: NotRequired["aws_sdk_eks.types.block_storage.BlockStorage"]
    """<p>Request to configure EBS Block Storage settings for your EKS Auto Mode cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfigRequest) -> dict:
    out: dict = {}
    if "block_storage" in value:
        import aws_sdk_eks.types.block_storage

        out["blockStorage"] = aws_sdk_eks.types.block_storage.serialize_json(
            value["block_storage"]
        )
    return out


def deserialize_json(data: dict) -> StorageConfigRequest:
    out: StorageConfigRequest = {}  # type: ignore[typeddict-item]
    if "blockStorage" in data:
        import aws_sdk_eks.types.block_storage

        out["block_storage"] = aws_sdk_eks.types.block_storage.deserialize_json(
            data["blockStorage"]
        )
    return out
