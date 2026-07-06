"""Generated from Smithy shape ``com.amazonaws.workdocs#StorageRuleType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.positive_size_type
    import aws_sdk_workdocs.types.storage_type


class StorageRuleType(TypedDict, closed=True):
    storage_allocated_in_bytes: NotRequired[
        "aws_sdk_workdocs.types.positive_size_type.PositiveSizeType"
    ]
    """<p>The amount of storage allocated, in bytes.</p>"""
    storage_type: NotRequired["aws_sdk_workdocs.types.storage_type.StorageType"]
    """<p>The type of storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageRuleType) -> dict:
    out: dict = {}
    if "storage_allocated_in_bytes" in value:
        out["StorageAllocatedInBytes"] = value["storage_allocated_in_bytes"]
    if "storage_type" in value:
        import aws_sdk_workdocs.types.storage_type

        out["StorageType"] = aws_sdk_workdocs.types.storage_type.serialize_json(
            value["storage_type"]
        )
    return out


def deserialize_json(data: dict) -> StorageRuleType:
    out: StorageRuleType = {}  # type: ignore[typeddict-item]
    if "StorageAllocatedInBytes" in data:
        out["storage_allocated_in_bytes"] = data["StorageAllocatedInBytes"]
    if "StorageType" in data:
        import aws_sdk_workdocs.types.storage_type

        out["storage_type"] = aws_sdk_workdocs.types.storage_type.deserialize_json(
            data["StorageType"]
        )
    return out
