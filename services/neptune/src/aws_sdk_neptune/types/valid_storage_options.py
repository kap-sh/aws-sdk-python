"""Generated from Smithy shape ``com.amazonaws.neptune#ValidStorageOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.double_range_list
    import aws_sdk_neptune.types.range_list
    import aws_sdk_neptune.types.string


class ValidStorageOptions(TypedDict, closed=True):
    storage_type: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>"""
    storage_size: NotRequired["aws_sdk_neptune.types.range_list.RangeList"]
    """<p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>"""
    provisioned_iops: NotRequired["aws_sdk_neptune.types.range_list.RangeList"]
    """<p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>"""
    iops_to_storage_ratio: NotRequired[
        "aws_sdk_neptune.types.double_range_list.DoubleRangeList"
    ]
    """<p>Not applicable. In Neptune the storage type is managed at the DB Cluster level.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidStorageOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "storage_type" in value:
        pairs.append((f"{prefix}.StorageType", str(value["storage_type"])))
    if "storage_size" in value:
        import aws_sdk_neptune.types.range_list

        aws_sdk_neptune.types.range_list.serialize_query(
            value["storage_size"], pairs, f"{prefix}.StorageSize"
        )
    if "provisioned_iops" in value:
        import aws_sdk_neptune.types.range_list

        aws_sdk_neptune.types.range_list.serialize_query(
            value["provisioned_iops"], pairs, f"{prefix}.ProvisionedIops"
        )
    if "iops_to_storage_ratio" in value:
        import aws_sdk_neptune.types.double_range_list

        aws_sdk_neptune.types.double_range_list.serialize_query(
            value["iops_to_storage_ratio"], pairs, f"{prefix}.IopsToStorageRatio"
        )


def deserialize_query(el: Element) -> ValidStorageOptions:
    out: ValidStorageOptions = {}  # type: ignore[typeddict-item]
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_storage_size = el.find("StorageSize")
    if child_storage_size is not None:
        import aws_sdk_neptune.types.range_list

        out["storage_size"] = aws_sdk_neptune.types.range_list.deserialize_query(
            child_storage_size
        )
    child_provisioned_iops = el.find("ProvisionedIops")
    if child_provisioned_iops is not None:
        import aws_sdk_neptune.types.range_list

        out["provisioned_iops"] = aws_sdk_neptune.types.range_list.deserialize_query(
            child_provisioned_iops
        )
    child_iops_to_storage_ratio = el.find("IopsToStorageRatio")
    if child_iops_to_storage_ratio is not None:
        import aws_sdk_neptune.types.double_range_list

        out["iops_to_storage_ratio"] = (
            aws_sdk_neptune.types.double_range_list.deserialize_query(
                child_iops_to_storage_ratio
            )
        )
    return out
