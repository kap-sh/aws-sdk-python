"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainClusterConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsOpenSearchServiceDomainClusterConfigDetails(TypedDict):
    instance_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of data nodes to use in the OpenSearch domain.</p>"""
    warm_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether UltraWarm is enabled.</p>"""
    warm_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of UltraWarm instances.</p>"""
    dedicated_master_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to use a dedicated master node for the OpenSearch domain. A dedicated master node performs cluster management tasks, but does not hold data or respond to data upload requests.</p>"""
    zone_awareness_config: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details.AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails"
    ]
    """<p>Configuration options for zone awareness. Provided if <code>ZoneAwarenessEnabled</code> is <code>true</code>.</p>"""
    dedicated_master_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of instances to use for the master node. If this attribute is specified, then <code>DedicatedMasterEnabled</code> must be <code>true</code>.</p>"""
    instance_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The instance type for your data nodes.</p> <p>For a list of valid values, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-instance-types.html\">Supported instance types in Amazon OpenSearch Service</a> in the <i>Amazon OpenSearch Service Developer Guide</i>.</p>"""
    warm_type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of UltraWarm instance.</p>"""
    zone_awareness_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to enable zone awareness for the OpenSearch domain. When zone awareness is enabled, OpenSearch Service allocates the cluster's nodes and replica index shards across Availability Zones (AZs) in the same Region. This prevents data loss and minimizes downtime if a node or data center fails.</p>"""
    dedicated_master_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The hardware configuration of the computer that hosts the dedicated master node.</p> <p>If this attribute is specified, then <code>DedicatedMasterEnabled</code> must be <code>true</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsOpenSearchServiceDomainClusterConfigDetails) -> dict:
    out: dict = {}
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "warm_enabled" in value:
        out["WarmEnabled"] = value["warm_enabled"]
    if "warm_count" in value:
        out["WarmCount"] = value["warm_count"]
    if "dedicated_master_enabled" in value:
        out["DedicatedMasterEnabled"] = value["dedicated_master_enabled"]
    if "zone_awareness_config" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details

        out["ZoneAwarenessConfig"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details.serialize_json(
                value["zone_awareness_config"]
            )
        )
    if "dedicated_master_count" in value:
        out["DedicatedMasterCount"] = value["dedicated_master_count"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "warm_type" in value:
        out["WarmType"] = value["warm_type"]
    if "zone_awareness_enabled" in value:
        out["ZoneAwarenessEnabled"] = value["zone_awareness_enabled"]
    if "dedicated_master_type" in value:
        out["DedicatedMasterType"] = value["dedicated_master_type"]
    return out


def deserialize_json(data: dict) -> AwsOpenSearchServiceDomainClusterConfigDetails:
    out: AwsOpenSearchServiceDomainClusterConfigDetails = {}  # type: ignore[typeddict-item]
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "WarmEnabled" in data:
        out["warm_enabled"] = data["WarmEnabled"]
    if "WarmCount" in data:
        out["warm_count"] = data["WarmCount"]
    if "DedicatedMasterEnabled" in data:
        out["dedicated_master_enabled"] = data["DedicatedMasterEnabled"]
    if "ZoneAwarenessConfig" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details

        out["zone_awareness_config"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_cluster_config_zone_awareness_config_details.deserialize_json(
                data["ZoneAwarenessConfig"]
            )
        )
    if "DedicatedMasterCount" in data:
        out["dedicated_master_count"] = data["DedicatedMasterCount"]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "WarmType" in data:
        out["warm_type"] = data["WarmType"]
    if "ZoneAwarenessEnabled" in data:
        out["zone_awareness_enabled"] = data["ZoneAwarenessEnabled"]
    if "DedicatedMasterType" in data:
        out["dedicated_master_type"] = data["DedicatedMasterType"]
    return out
