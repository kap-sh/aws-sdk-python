"""Generated from Smithy shape ``com.amazonaws.dsql#GetClusterOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dsql.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_dsql.types.cluster_arn
    import aws_sdk_dsql.types.cluster_creation_time
    import aws_sdk_dsql.types.cluster_id
    import aws_sdk_dsql.types.cluster_status
    import aws_sdk_dsql.types.deletion_protection_enabled
    import aws_sdk_dsql.types.encryption_details
    import aws_sdk_dsql.types.endpoint
    import aws_sdk_dsql.types.multi_region_properties
    import aws_sdk_dsql.types.tag_map

class GetClusterOutput(TypedDict):
    identifier: "aws_sdk_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the retrieved cluster.</p>"""
    arn: "aws_sdk_dsql.types.cluster_arn.ClusterArn"
    """<p>The ARN of the retrieved cluster.</p>"""
    status: "aws_sdk_dsql.types.cluster_status.ClusterStatus"
    """<p>The status of the retrieved cluster.</p>"""
    creation_time: "aws_sdk_dsql.types.cluster_creation_time.ClusterCreationTime"
    """<p>The time of when the cluster was created.</p>"""
    deletion_protection_enabled: "aws_sdk_dsql.types.deletion_protection_enabled.DeletionProtectionEnabled"
    """<p>Whether deletion protection is enabled in this cluster.</p>"""
    multi_region_properties: NotRequired["aws_sdk_dsql.types.multi_region_properties.MultiRegionProperties"]
    """<p>Returns the current multi-Region cluster configuration, including witness region and linked cluster information.</p>"""
    tags: NotRequired["aws_sdk_dsql.types.tag_map.TagMap"]
    encryption_details: NotRequired["aws_sdk_dsql.types.encryption_details.EncryptionDetails"]
    """<p>The current encryption configuration details for the cluster.</p>"""
    endpoint: NotRequired["aws_sdk_dsql.types.endpoint.Endpoint"]
    """<p>The connection endpoint for the cluster.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetClusterOutput) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["arn"] = value["arn"]
    import aws_sdk_dsql.types.cluster_status
    out["status"] = aws_sdk_dsql.types.cluster_status.serialize_json(value["status"])
    import aws_sdk_dsql.types.cluster_creation_time
    out["creationTime"] = aws_sdk_dsql.types.cluster_creation_time.serialize_json(value["creation_time"])
    out["deletionProtectionEnabled"] = value["deletion_protection_enabled"]
    if "multi_region_properties" in value:
        import aws_sdk_dsql.types.multi_region_properties
        out["multiRegionProperties"] = aws_sdk_dsql.types.multi_region_properties.serialize_json(value["multi_region_properties"])
    if "tags" in value:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.serialize_json(value["tags"])
    if "encryption_details" in value:
        import aws_sdk_dsql.types.encryption_details
        out["encryptionDetails"] = aws_sdk_dsql.types.encryption_details.serialize_json(value["encryption_details"])
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> GetClusterOutput:
    out: GetClusterOutput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("GetClusterOutput.identifier required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetClusterOutput.arn required")
    if "status" in data:
        import aws_sdk_dsql.types.cluster_status
        out["status"] = aws_sdk_dsql.types.cluster_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("GetClusterOutput.status required")
    if "creationTime" in data:
        import aws_sdk_dsql.types.cluster_creation_time
        out["creation_time"] = aws_sdk_dsql.types.cluster_creation_time.deserialize_json(data["creationTime"])
    else:
        raise DeserializationError("GetClusterOutput.creation_time required")
    if "deletionProtectionEnabled" in data:
        out["deletion_protection_enabled"] = data["deletionProtectionEnabled"]
    else:
        raise DeserializationError("GetClusterOutput.deletion_protection_enabled required")
    if "multiRegionProperties" in data:
        import aws_sdk_dsql.types.multi_region_properties
        out["multi_region_properties"] = aws_sdk_dsql.types.multi_region_properties.deserialize_json(data["multiRegionProperties"])
    if "tags" in data:
        import aws_sdk_dsql.types.tag_map
        out["tags"] = aws_sdk_dsql.types.tag_map.deserialize_json(data["tags"])
    if "encryptionDetails" in data:
        import aws_sdk_dsql.types.encryption_details
        out["encryption_details"] = aws_sdk_dsql.types.encryption_details.deserialize_json(data["encryptionDetails"])
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    return out