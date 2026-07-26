"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ScalingParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.partition_instance_type
    import capo_cloudsearch.types.u_int_value


class ScalingParameters(TypedDict, closed=True):
    desired_instance_type: NotRequired[
        "capo_cloudsearch.types.partition_instance_type.PartitionInstanceType"
    ]
    """<p>The instance type that you want to preconfigure for your domain. For example, <code>search.m1.small</code>.</p>"""
    desired_replication_count: "capo_cloudsearch.types.u_int_value.UIntValue"
    """<p>The number of replicas you want to preconfigure for each index partition.</p>"""
    desired_partition_count: "capo_cloudsearch.types.u_int_value.UIntValue"
    """<p>The number of partitions you want to preconfigure for your domain. Only valid when you select <code>m2.2xlarge</code> as the desired instance type.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScalingParameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "desired_instance_type" in value:
        import capo_cloudsearch.types.partition_instance_type

        capo_cloudsearch.types.partition_instance_type.serialize_query(
            value["desired_instance_type"], pairs, f"{prefix}.DesiredInstanceType"
        )
    pairs.append(
        (
            f"{prefix}.DesiredReplicationCount",
            str(value.get("desired_replication_count", 0)),
        )
    )
    pairs.append(
        (
            f"{prefix}.DesiredPartitionCount",
            str(value.get("desired_partition_count", 0)),
        )
    )


def deserialize_query(el: Element) -> ScalingParameters:
    out: ScalingParameters = {}  # type: ignore[typeddict-item]
    child_desired_instance_type = el.find("DesiredInstanceType")
    if child_desired_instance_type is not None:
        import capo_cloudsearch.types.partition_instance_type

        out["desired_instance_type"] = (
            capo_cloudsearch.types.partition_instance_type.deserialize_query(
                child_desired_instance_type
            )
        )
    child_desired_replication_count = el.find("DesiredReplicationCount")
    if child_desired_replication_count is not None:
        out["desired_replication_count"] = int(
            child_desired_replication_count.text or ""
        )
    else:
        out["desired_replication_count"] = 0
    child_desired_partition_count = el.find("DesiredPartitionCount")
    if child_desired_partition_count is not None:
        out["desired_partition_count"] = int(child_desired_partition_count.text or "")
    else:
        out["desired_partition_count"] = 0
    return out
