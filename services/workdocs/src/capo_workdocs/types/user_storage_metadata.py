"""Generated from Smithy shape ``com.amazonaws.workdocs#UserStorageMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.size_type
    import capo_workdocs.types.storage_rule_type


class UserStorageMetadata(TypedDict, closed=True):
    storage_utilized_in_bytes: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The amount of storage used, in bytes.</p>"""
    storage_rule: NotRequired["capo_workdocs.types.storage_rule_type.StorageRuleType"]
    """<p>The storage for a user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserStorageMetadata) -> dict:
    out: dict = {}
    if "storage_utilized_in_bytes" in value:
        out["StorageUtilizedInBytes"] = value["storage_utilized_in_bytes"]
    if "storage_rule" in value:
        import capo_workdocs.types.storage_rule_type

        out["StorageRule"] = capo_workdocs.types.storage_rule_type.serialize_json(
            value["storage_rule"]
        )
    return out


def deserialize_json(data: dict) -> UserStorageMetadata:
    out: UserStorageMetadata = {}  # type: ignore[typeddict-item]
    if "StorageUtilizedInBytes" in data:
        out["storage_utilized_in_bytes"] = data["StorageUtilizedInBytes"]
    if "StorageRule" in data:
        import capo_workdocs.types.storage_rule_type

        out["storage_rule"] = capo_workdocs.types.storage_rule_type.deserialize_json(
            data["StorageRule"]
        )
    return out
