"""Generated from Smithy shape ``com.amazonaws.elasticache#RegionalConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.resharding_configuration_list
    import aws_sdk_elasticache.types.string


class RegionalConfiguration(TypedDict):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the secondary cluster</p>"""
    replication_group_region: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The Amazon region where the cluster is stored</p>"""
    resharding_configuration: NotRequired[
        "aws_sdk_elasticache.types.resharding_configuration_list.ReshardingConfigurationList"
    ]
    """<p>A list of <code>PreferredAvailabilityZones</code> objects that specifies the configuration of a node group in the resharded cluster. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RegionalConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "replication_group_region" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupRegion", str(value["replication_group_region"]))
        )
    if "resharding_configuration" in value:
        import aws_sdk_elasticache.types.resharding_configuration_list

        aws_sdk_elasticache.types.resharding_configuration_list.serialize_query(
            value["resharding_configuration"],
            pairs,
            f"{prefix}.ReshardingConfiguration",
        )


def deserialize_query(el: Element) -> RegionalConfiguration:
    out: RegionalConfiguration = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_replication_group_region = el.find("ReplicationGroupRegion")
    if child_replication_group_region is not None:
        out["replication_group_region"] = str(child_replication_group_region.text or "")
    child_resharding_configuration = el.find("ReshardingConfiguration")
    if child_resharding_configuration is not None:
        import aws_sdk_elasticache.types.resharding_configuration_list

        out["resharding_configuration"] = (
            aws_sdk_elasticache.types.resharding_configuration_list.deserialize_query(
                child_resharding_configuration
            )
        )
    return out
