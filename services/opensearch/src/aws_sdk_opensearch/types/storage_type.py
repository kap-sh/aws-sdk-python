"""Generated from Smithy shape ``com.amazonaws.opensearch#StorageType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.storage_sub_type_name
    import aws_sdk_opensearch.types.storage_type_limit_list
    import aws_sdk_opensearch.types.storage_type_name


class StorageType(TypedDict):
    storage_type_name: NotRequired[
        "aws_sdk_opensearch.types.storage_type_name.StorageTypeName"
    ]
    """<p>The name of the storage type.</p>"""
    storage_sub_type_name: NotRequired[
        "aws_sdk_opensearch.types.storage_sub_type_name.StorageSubTypeName"
    ]
    """<p>The storage sub-type, such as <code>gp3</code> or <code>io1</code>.</p>"""
    storage_type_limits: NotRequired[
        "aws_sdk_opensearch.types.storage_type_limit_list.StorageTypeLimitList"
    ]
    """<p>Limits that are applicable for the given storage type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StorageType) -> dict:
    out: dict = {}
    if "storage_type_name" in value:
        out["StorageTypeName"] = value["storage_type_name"]
    if "storage_sub_type_name" in value:
        out["StorageSubTypeName"] = value["storage_sub_type_name"]
    if "storage_type_limits" in value:
        import aws_sdk_opensearch.types.storage_type_limit_list

        out["StorageTypeLimits"] = (
            aws_sdk_opensearch.types.storage_type_limit_list.serialize_json(
                value["storage_type_limits"]
            )
        )
    return out


def deserialize_json(data: dict) -> StorageType:
    out: StorageType = {}  # type: ignore[typeddict-item]
    if "StorageTypeName" in data:
        out["storage_type_name"] = data["StorageTypeName"]
    if "StorageSubTypeName" in data:
        out["storage_sub_type_name"] = data["StorageSubTypeName"]
    if "StorageTypeLimits" in data:
        import aws_sdk_opensearch.types.storage_type_limit_list

        out["storage_type_limits"] = (
            aws_sdk_opensearch.types.storage_type_limit_list.deserialize_json(
                data["StorageTypeLimits"]
            )
        )
    return out
