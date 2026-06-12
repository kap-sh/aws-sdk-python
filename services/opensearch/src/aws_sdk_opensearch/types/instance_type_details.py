"""Generated from Smithy shape ``com.amazonaws.opensearch#InstanceTypeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.availability_zone_list
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.instance_role_list
    import aws_sdk_opensearch.types.open_search_partition_instance_type


class InstanceTypeDetails(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>The instance type.</p>"""
    encryption_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether encryption at rest and node-to-node encryption are supported for the instance type.</p>"""
    cognito_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether Amazon Cognito access is supported for the instance type.</p>"""
    app_logs_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether logging is supported for the instance type.</p>"""
    advanced_security_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether fine-grained access control is supported for the instance type.</p>"""
    warm_enabled: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether UltraWarm is supported for the instance type.</p>"""
    instance_role: NotRequired[
        "aws_sdk_opensearch.types.instance_role_list.InstanceRoleList"
    ]
    """<p>Whether the instance acts as a data node, a dedicated master node, or an UltraWarm node.</p>"""
    availability_zones: NotRequired[
        "aws_sdk_opensearch.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The supported Availability Zones for the instance type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeDetails) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["InstanceType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    if "encryption_enabled" in value:
        out["EncryptionEnabled"] = value["encryption_enabled"]
    if "cognito_enabled" in value:
        out["CognitoEnabled"] = value["cognito_enabled"]
    if "app_logs_enabled" in value:
        out["AppLogsEnabled"] = value["app_logs_enabled"]
    if "advanced_security_enabled" in value:
        out["AdvancedSecurityEnabled"] = value["advanced_security_enabled"]
    if "warm_enabled" in value:
        out["WarmEnabled"] = value["warm_enabled"]
    if "instance_role" in value:
        import aws_sdk_opensearch.types.instance_role_list

        out["InstanceRole"] = (
            aws_sdk_opensearch.types.instance_role_list.serialize_json(
                value["instance_role"]
            )
        )
    if "availability_zones" in value:
        import aws_sdk_opensearch.types.availability_zone_list

        out["AvailabilityZones"] = (
            aws_sdk_opensearch.types.availability_zone_list.serialize_json(
                value["availability_zones"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceTypeDetails:
    out: InstanceTypeDetails = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["instance_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
        )
    if "EncryptionEnabled" in data:
        out["encryption_enabled"] = data["EncryptionEnabled"]
    if "CognitoEnabled" in data:
        out["cognito_enabled"] = data["CognitoEnabled"]
    if "AppLogsEnabled" in data:
        out["app_logs_enabled"] = data["AppLogsEnabled"]
    if "AdvancedSecurityEnabled" in data:
        out["advanced_security_enabled"] = data["AdvancedSecurityEnabled"]
    if "WarmEnabled" in data:
        out["warm_enabled"] = data["WarmEnabled"]
    if "InstanceRole" in data:
        import aws_sdk_opensearch.types.instance_role_list

        out["instance_role"] = (
            aws_sdk_opensearch.types.instance_role_list.deserialize_json(
                data["InstanceRole"]
            )
        )
    if "AvailabilityZones" in data:
        import aws_sdk_opensearch.types.availability_zone_list

        out["availability_zones"] = (
            aws_sdk_opensearch.types.availability_zone_list.deserialize_json(
                data["AvailabilityZones"]
            )
        )
    return out
