"""Generated from Smithy shape ``com.amazonaws.rds#ValidStorageOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.double_range_list
    import aws_sdk_rds.types.range_list
    import aws_sdk_rds.types.string


class ValidStorageOptions(TypedDict):
    storage_type: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The valid storage types for your DB instance. For example: gp2, gp3, io1, io2.</p>"""
    storage_size: NotRequired["aws_sdk_rds.types.range_list.RangeList"]
    """<p>The valid range of storage in gibibytes (GiB). For example, 100 to 16,384.</p>"""
    provisioned_iops: NotRequired["aws_sdk_rds.types.range_list.RangeList"]
    """<p>The valid range of provisioned IOPS. For example, 1000-256,000.</p>"""
    iops_to_storage_ratio: NotRequired[
        "aws_sdk_rds.types.double_range_list.DoubleRangeList"
    ]
    """<p>The valid range of Provisioned IOPS to gibibytes of storage multiplier. For example, 3-10, which means that provisioned IOPS can be between 3 and 10 times storage.</p>"""
    provisioned_storage_throughput: NotRequired[
        "aws_sdk_rds.types.range_list.RangeList"
    ]
    """<p>The valid range of provisioned storage throughput. For example, 500-4,000 mebibytes per second (MiBps).</p>"""
    storage_throughput_to_iops_ratio: NotRequired[
        "aws_sdk_rds.types.double_range_list.DoubleRangeList"
    ]
    """<p>The valid range of storage throughput to provisioned IOPS ratios. For example, 0-0.25.</p>"""
    supports_storage_autoscaling: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether or not Amazon RDS can automatically scale storage for DB instances that use the new instance class.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidStorageOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "storage_type" in value:
        pairs.append((f"{prefix}.StorageType", str(value["storage_type"])))
    if "storage_size" in value:
        import aws_sdk_rds.types.range_list

        aws_sdk_rds.types.range_list.serialize_query(
            value["storage_size"], pairs, f"{prefix}.StorageSize"
        )
    if "provisioned_iops" in value:
        import aws_sdk_rds.types.range_list

        aws_sdk_rds.types.range_list.serialize_query(
            value["provisioned_iops"], pairs, f"{prefix}.ProvisionedIops"
        )
    if "iops_to_storage_ratio" in value:
        import aws_sdk_rds.types.double_range_list

        aws_sdk_rds.types.double_range_list.serialize_query(
            value["iops_to_storage_ratio"], pairs, f"{prefix}.IopsToStorageRatio"
        )
    if "provisioned_storage_throughput" in value:
        import aws_sdk_rds.types.range_list

        aws_sdk_rds.types.range_list.serialize_query(
            value["provisioned_storage_throughput"],
            pairs,
            f"{prefix}.ProvisionedStorageThroughput",
        )
    if "storage_throughput_to_iops_ratio" in value:
        import aws_sdk_rds.types.double_range_list

        aws_sdk_rds.types.double_range_list.serialize_query(
            value["storage_throughput_to_iops_ratio"],
            pairs,
            f"{prefix}.StorageThroughputToIopsRatio",
        )
    if "supports_storage_autoscaling" in value:
        pairs.append(
            (
                f"{prefix}.SupportsStorageAutoscaling",
                "true" if value["supports_storage_autoscaling"] else "false",
            )
        )


def deserialize_query(el: Element) -> ValidStorageOptions:
    out: ValidStorageOptions = {}  # type: ignore[typeddict-item]
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_storage_size = el.find("StorageSize")
    if child_storage_size is not None:
        import aws_sdk_rds.types.range_list

        out["storage_size"] = aws_sdk_rds.types.range_list.deserialize_query(
            child_storage_size
        )
    child_provisioned_iops = el.find("ProvisionedIops")
    if child_provisioned_iops is not None:
        import aws_sdk_rds.types.range_list

        out["provisioned_iops"] = aws_sdk_rds.types.range_list.deserialize_query(
            child_provisioned_iops
        )
    child_iops_to_storage_ratio = el.find("IopsToStorageRatio")
    if child_iops_to_storage_ratio is not None:
        import aws_sdk_rds.types.double_range_list

        out["iops_to_storage_ratio"] = (
            aws_sdk_rds.types.double_range_list.deserialize_query(
                child_iops_to_storage_ratio
            )
        )
    child_provisioned_storage_throughput = el.find("ProvisionedStorageThroughput")
    if child_provisioned_storage_throughput is not None:
        import aws_sdk_rds.types.range_list

        out["provisioned_storage_throughput"] = (
            aws_sdk_rds.types.range_list.deserialize_query(
                child_provisioned_storage_throughput
            )
        )
    child_storage_throughput_to_iops_ratio = el.find("StorageThroughputToIopsRatio")
    if child_storage_throughput_to_iops_ratio is not None:
        import aws_sdk_rds.types.double_range_list

        out["storage_throughput_to_iops_ratio"] = (
            aws_sdk_rds.types.double_range_list.deserialize_query(
                child_storage_throughput_to_iops_ratio
            )
        )
    child_supports_storage_autoscaling = el.find("SupportsStorageAutoscaling")
    if child_supports_storage_autoscaling is not None:
        out["supports_storage_autoscaling"] = (
            child_supports_storage_autoscaling.text or ""
        ).lower() == "true"
    return out
