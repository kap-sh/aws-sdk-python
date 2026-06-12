"""Generated from Smithy shape ``com.amazonaws.m2#GetEnvironmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.arn
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.capacity_value
    import aws_sdk_m2.types.engine_type
    import aws_sdk_m2.types.engine_version
    import aws_sdk_m2.types.entity_description
    import aws_sdk_m2.types.entity_name
    import aws_sdk_m2.types.environment_lifecycle
    import aws_sdk_m2.types.high_availability_config
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.network_type
    import aws_sdk_m2.types.pending_maintenance
    import aws_sdk_m2.types.storage_configuration_list
    import aws_sdk_m2.types.string20
    import aws_sdk_m2.types.string50
    import aws_sdk_m2.types.string50_list
    import aws_sdk_m2.types.tag_map
    import aws_sdk_m2.types.timestamp


class GetEnvironmentResponse(TypedDict):
    name: "aws_sdk_m2.types.entity_name.EntityName"
    """<p>The name of the runtime environment. Must be unique within the account.</p>"""
    description: NotRequired["aws_sdk_m2.types.entity_description.EntityDescription"]
    """<p>The description of the runtime environment.</p>"""
    environment_arn: "aws_sdk_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the runtime environment.</p>"""
    environment_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the runtime environment.</p>"""
    instance_type: "aws_sdk_m2.types.string20.String20"
    """<p>The type of instance underlying the runtime environment.</p>"""
    status: "aws_sdk_m2.types.environment_lifecycle.EnvironmentLifecycle"
    """<p>The status of the runtime environment. If the Amazon Web Services Mainframe Modernization environment is missing a connection to the customer owned dependent resource, the status will be <code>Unhealthy</code>.</p>"""
    engine_type: "aws_sdk_m2.types.engine_type.EngineType"
    """<p>The target platform for the runtime environment.</p>"""
    engine_version: "aws_sdk_m2.types.engine_version.EngineVersion"
    """<p>The version of the runtime engine.</p>"""
    vpc_id: "aws_sdk_m2.types.string50.String50"
    """<p>The unique identifier for the VPC used with this runtime environment.</p>"""
    subnet_ids: "aws_sdk_m2.types.string50_list.String50List"
    """<p>The unique identifiers of the subnets assigned to this runtime environment.</p>"""
    security_group_ids: "aws_sdk_m2.types.string50_list.String50List"
    """<p>The unique identifiers of the security groups assigned to this runtime environment.</p>"""
    creation_time: "aws_sdk_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the runtime environment was created.</p>"""
    storage_configurations: NotRequired[
        "aws_sdk_m2.types.storage_configuration_list.StorageConfigurationList"
    ]
    """<p>The storage configurations defined for the runtime environment.</p>"""
    tags: NotRequired["aws_sdk_m2.types.tag_map.TagMap"]
    """<p>The tags defined for this runtime environment.</p>"""
    high_availability_config: NotRequired[
        "aws_sdk_m2.types.high_availability_config.HighAvailabilityConfig"
    ]
    """<p>The desired capacity of the high availability configuration for the runtime environment.</p>"""
    publicly_accessible: "aws_sdk_m2.types.boolean.Boolean"
    """<p>Whether applications running in this runtime environment are publicly accessible. </p>"""
    actual_capacity: NotRequired["aws_sdk_m2.types.capacity_value.CapacityValue"]
    """<p>The number of instances included in the runtime environment. A standalone runtime environment has a maximum of one instance. Currently, a high availability runtime environment has a maximum of two instances. </p>"""
    load_balancer_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the load balancer used with the runtime environment.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    preferred_maintenance_window: NotRequired["aws_sdk_m2.types.string50.String50"]
    """<p>The maintenance window for the runtime environment. If you don't provide a value for the maintenance window, the service assigns a random value.</p>"""
    pending_maintenance: NotRequired[
        "aws_sdk_m2.types.pending_maintenance.PendingMaintenance"
    ]
    """<p>Indicates the pending maintenance scheduled on this environment.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The identifier of a customer managed key.</p>"""
    network_type: NotRequired["aws_sdk_m2.types.network_type.NetworkType"]
    """<p>The network type supported by the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["environmentArn"] = value["environment_arn"]
    out["environmentId"] = value["environment_id"]
    out["instanceType"] = value["instance_type"]
    out["status"] = value["status"]
    out["engineType"] = value["engine_type"]
    out["engineVersion"] = value["engine_version"]
    out["vpcId"] = value["vpc_id"]
    import aws_sdk_m2.types.string50_list

    out["subnetIds"] = aws_sdk_m2.types.string50_list.serialize_json(
        value["subnet_ids"]
    )
    import aws_sdk_m2.types.string50_list

    out["securityGroupIds"] = aws_sdk_m2.types.string50_list.serialize_json(
        value["security_group_ids"]
    )
    import aws_sdk_m2.types.timestamp

    out["creationTime"] = aws_sdk_m2.types.timestamp.serialize_json(
        value["creation_time"]
    )
    if "storage_configurations" in value:
        import aws_sdk_m2.types.storage_configuration_list

        out["storageConfigurations"] = (
            aws_sdk_m2.types.storage_configuration_list.serialize_json(
                value["storage_configurations"]
            )
        )
    if "tags" in value:
        import aws_sdk_m2.types.tag_map

        out["tags"] = aws_sdk_m2.types.tag_map.serialize_json(value["tags"])
    if "high_availability_config" in value:
        import aws_sdk_m2.types.high_availability_config

        out["highAvailabilityConfig"] = (
            aws_sdk_m2.types.high_availability_config.serialize_json(
                value["high_availability_config"]
            )
        )
    out["publiclyAccessible"] = value.get("publicly_accessible", False)
    if "actual_capacity" in value:
        out["actualCapacity"] = value["actual_capacity"]
    if "load_balancer_arn" in value:
        out["loadBalancerArn"] = value["load_balancer_arn"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "pending_maintenance" in value:
        import aws_sdk_m2.types.pending_maintenance

        out["pendingMaintenance"] = aws_sdk_m2.types.pending_maintenance.serialize_json(
            value["pending_maintenance"]
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    return out


def deserialize_json(data: dict) -> GetEnvironmentResponse:
    out: GetEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetEnvironmentResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    else:
        raise DeserializationError("GetEnvironmentResponse.environment_arn required")
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("GetEnvironmentResponse.environment_id required")
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    else:
        raise DeserializationError("GetEnvironmentResponse.instance_type required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetEnvironmentResponse.status required")
    if "engineType" in data:
        out["engine_type"] = data["engineType"]
    else:
        raise DeserializationError("GetEnvironmentResponse.engine_type required")
    if "engineVersion" in data:
        out["engine_version"] = data["engineVersion"]
    else:
        raise DeserializationError("GetEnvironmentResponse.engine_version required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("GetEnvironmentResponse.vpc_id required")
    if "subnetIds" in data:
        import aws_sdk_m2.types.string50_list

        out["subnet_ids"] = aws_sdk_m2.types.string50_list.deserialize_json(
            data["subnetIds"]
        )
    else:
        raise DeserializationError("GetEnvironmentResponse.subnet_ids required")
    if "securityGroupIds" in data:
        import aws_sdk_m2.types.string50_list

        out["security_group_ids"] = aws_sdk_m2.types.string50_list.deserialize_json(
            data["securityGroupIds"]
        )
    else:
        raise DeserializationError("GetEnvironmentResponse.security_group_ids required")
    if "creationTime" in data:
        import aws_sdk_m2.types.timestamp

        out["creation_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("GetEnvironmentResponse.creation_time required")
    if "storageConfigurations" in data:
        import aws_sdk_m2.types.storage_configuration_list

        out["storage_configurations"] = (
            aws_sdk_m2.types.storage_configuration_list.deserialize_json(
                data["storageConfigurations"]
            )
        )
    if "tags" in data:
        import aws_sdk_m2.types.tag_map

        out["tags"] = aws_sdk_m2.types.tag_map.deserialize_json(data["tags"])
    if "highAvailabilityConfig" in data:
        import aws_sdk_m2.types.high_availability_config

        out["high_availability_config"] = (
            aws_sdk_m2.types.high_availability_config.deserialize_json(
                data["highAvailabilityConfig"]
            )
        )
    if "publiclyAccessible" in data:
        out["publicly_accessible"] = data["publiclyAccessible"]
    else:
        out["publicly_accessible"] = False
    if "actualCapacity" in data:
        out["actual_capacity"] = data["actualCapacity"]
    if "loadBalancerArn" in data:
        out["load_balancer_arn"] = data["loadBalancerArn"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "preferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if "pendingMaintenance" in data:
        import aws_sdk_m2.types.pending_maintenance

        out["pending_maintenance"] = (
            aws_sdk_m2.types.pending_maintenance.deserialize_json(
                data["pendingMaintenance"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "networkType" in data:
        out["network_type"] = data["networkType"]
    return out
