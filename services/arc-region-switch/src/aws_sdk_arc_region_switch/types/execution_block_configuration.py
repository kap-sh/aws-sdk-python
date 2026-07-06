"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionBlockConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.arc_routing_control_configuration
    import aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration
    import aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration
    import aws_sdk_arc_region_switch.types.custom_action_lambda_configuration
    import aws_sdk_arc_region_switch.types.document_db_configuration
    import aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration
    import aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration
    import aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration
    import aws_sdk_arc_region_switch.types.execution_approval_configuration
    import aws_sdk_arc_region_switch.types.global_aurora_configuration
    import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration
    import aws_sdk_arc_region_switch.types.neptune_global_database_configuration
    import aws_sdk_arc_region_switch.types.parallel_execution_block_configuration
    import aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration
    import aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration
    import aws_sdk_arc_region_switch.types.region_switch_plan_configuration
    import aws_sdk_arc_region_switch.types.route53_health_check_configuration


class _ExecutionBlockConfiguration_customActionLambdaConfig(TypedDict, closed=True):
    customActionLambdaConfig: "aws_sdk_arc_region_switch.types.custom_action_lambda_configuration.CustomActionLambdaConfiguration"


class _ExecutionBlockConfiguration_ec2AsgCapacityIncreaseConfig(TypedDict, closed=True):
    ec2AsgCapacityIncreaseConfig: "aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration.Ec2AsgCapacityIncreaseConfiguration"


class _ExecutionBlockConfiguration_executionApprovalConfig(TypedDict, closed=True):
    executionApprovalConfig: "aws_sdk_arc_region_switch.types.execution_approval_configuration.ExecutionApprovalConfiguration"


class _ExecutionBlockConfiguration_arcRoutingControlConfig(TypedDict, closed=True):
    arcRoutingControlConfig: "aws_sdk_arc_region_switch.types.arc_routing_control_configuration.ArcRoutingControlConfiguration"


class _ExecutionBlockConfiguration_globalAuroraConfig(TypedDict, closed=True):
    globalAuroraConfig: "aws_sdk_arc_region_switch.types.global_aurora_configuration.GlobalAuroraConfiguration"


class _ExecutionBlockConfiguration_parallelConfig(TypedDict, closed=True):
    parallelConfig: "aws_sdk_arc_region_switch.types.parallel_execution_block_configuration.ParallelExecutionBlockConfiguration"


class _ExecutionBlockConfiguration_regionSwitchPlanConfig(TypedDict, closed=True):
    regionSwitchPlanConfig: "aws_sdk_arc_region_switch.types.region_switch_plan_configuration.RegionSwitchPlanConfiguration"


class _ExecutionBlockConfiguration_ecsCapacityIncreaseConfig(TypedDict, closed=True):
    ecsCapacityIncreaseConfig: "aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration.EcsCapacityIncreaseConfiguration"


class _ExecutionBlockConfiguration_eksResourceScalingConfig(TypedDict, closed=True):
    eksResourceScalingConfig: "aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration.EksResourceScalingConfiguration"


class _ExecutionBlockConfiguration_route53HealthCheckConfig(TypedDict, closed=True):
    route53HealthCheckConfig: "aws_sdk_arc_region_switch.types.route53_health_check_configuration.Route53HealthCheckConfiguration"


class _ExecutionBlockConfiguration_documentDbConfig(TypedDict, closed=True):
    documentDbConfig: "aws_sdk_arc_region_switch.types.document_db_configuration.DocumentDbConfiguration"


class _ExecutionBlockConfiguration_rdsPromoteReadReplicaConfig(TypedDict, closed=True):
    rdsPromoteReadReplicaConfig: "aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration.RdsPromoteReadReplicaConfiguration"


class _ExecutionBlockConfiguration_rdsCreateCrossRegionReadReplicaConfig(
    TypedDict, closed=True
):
    rdsCreateCrossRegionReadReplicaConfig: "aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration.RdsCreateCrossRegionReplicaConfiguration"


class _ExecutionBlockConfiguration_lambdaEventSourceMappingConfig(
    TypedDict, closed=True
):
    lambdaEventSourceMappingConfig: "aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration.LambdaEventSourceMappingConfiguration"


class _ExecutionBlockConfiguration_auroraServerlessScalingConfig(
    TypedDict, closed=True
):
    auroraServerlessScalingConfig: "aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration.AuroraServerlessScalingConfiguration"


class _ExecutionBlockConfiguration_auroraProvisionedScalingConfig(
    TypedDict, closed=True
):
    auroraProvisionedScalingConfig: "aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration.AuroraProvisionedScalingConfiguration"


class _ExecutionBlockConfiguration_neptuneGlobalDatabaseConfig(TypedDict, closed=True):
    neptuneGlobalDatabaseConfig: "aws_sdk_arc_region_switch.types.neptune_global_database_configuration.NeptuneGlobalDatabaseConfiguration"


ExecutionBlockConfiguration: TypeAlias = (
    _ExecutionBlockConfiguration_customActionLambdaConfig
    | _ExecutionBlockConfiguration_ec2AsgCapacityIncreaseConfig
    | _ExecutionBlockConfiguration_executionApprovalConfig
    | _ExecutionBlockConfiguration_arcRoutingControlConfig
    | _ExecutionBlockConfiguration_globalAuroraConfig
    | _ExecutionBlockConfiguration_parallelConfig
    | _ExecutionBlockConfiguration_regionSwitchPlanConfig
    | _ExecutionBlockConfiguration_ecsCapacityIncreaseConfig
    | _ExecutionBlockConfiguration_eksResourceScalingConfig
    | _ExecutionBlockConfiguration_route53HealthCheckConfig
    | _ExecutionBlockConfiguration_documentDbConfig
    | _ExecutionBlockConfiguration_rdsPromoteReadReplicaConfig
    | _ExecutionBlockConfiguration_rdsCreateCrossRegionReadReplicaConfig
    | _ExecutionBlockConfiguration_lambdaEventSourceMappingConfig
    | _ExecutionBlockConfiguration_auroraServerlessScalingConfig
    | _ExecutionBlockConfiguration_auroraProvisionedScalingConfig
    | _ExecutionBlockConfiguration_neptuneGlobalDatabaseConfig
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionBlockConfiguration) -> dict:
    if "customActionLambdaConfig" in value:
        import aws_sdk_arc_region_switch.types.custom_action_lambda_configuration

        return {
            "customActionLambdaConfig": aws_sdk_arc_region_switch.types.custom_action_lambda_configuration.serialize_aws_json_1_0(
                value["customActionLambdaConfig"]
            )
        }
    elif "ec2AsgCapacityIncreaseConfig" in value:
        import aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration

        return {
            "ec2AsgCapacityIncreaseConfig": aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration.serialize_aws_json_1_0(
                value["ec2AsgCapacityIncreaseConfig"]
            )
        }
    elif "executionApprovalConfig" in value:
        import aws_sdk_arc_region_switch.types.execution_approval_configuration

        return {
            "executionApprovalConfig": aws_sdk_arc_region_switch.types.execution_approval_configuration.serialize_aws_json_1_0(
                value["executionApprovalConfig"]
            )
        }
    elif "arcRoutingControlConfig" in value:
        import aws_sdk_arc_region_switch.types.arc_routing_control_configuration

        return {
            "arcRoutingControlConfig": aws_sdk_arc_region_switch.types.arc_routing_control_configuration.serialize_aws_json_1_0(
                value["arcRoutingControlConfig"]
            )
        }
    elif "globalAuroraConfig" in value:
        import aws_sdk_arc_region_switch.types.global_aurora_configuration

        return {
            "globalAuroraConfig": aws_sdk_arc_region_switch.types.global_aurora_configuration.serialize_aws_json_1_0(
                value["globalAuroraConfig"]
            )
        }
    elif "parallelConfig" in value:
        import aws_sdk_arc_region_switch.types.parallel_execution_block_configuration

        return {
            "parallelConfig": aws_sdk_arc_region_switch.types.parallel_execution_block_configuration.serialize_aws_json_1_0(
                value["parallelConfig"]
            )
        }
    elif "regionSwitchPlanConfig" in value:
        import aws_sdk_arc_region_switch.types.region_switch_plan_configuration

        return {
            "regionSwitchPlanConfig": aws_sdk_arc_region_switch.types.region_switch_plan_configuration.serialize_aws_json_1_0(
                value["regionSwitchPlanConfig"]
            )
        }
    elif "ecsCapacityIncreaseConfig" in value:
        import aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration

        return {
            "ecsCapacityIncreaseConfig": aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration.serialize_aws_json_1_0(
                value["ecsCapacityIncreaseConfig"]
            )
        }
    elif "eksResourceScalingConfig" in value:
        import aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration

        return {
            "eksResourceScalingConfig": aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration.serialize_aws_json_1_0(
                value["eksResourceScalingConfig"]
            )
        }
    elif "route53HealthCheckConfig" in value:
        import aws_sdk_arc_region_switch.types.route53_health_check_configuration

        return {
            "route53HealthCheckConfig": aws_sdk_arc_region_switch.types.route53_health_check_configuration.serialize_aws_json_1_0(
                value["route53HealthCheckConfig"]
            )
        }
    elif "documentDbConfig" in value:
        import aws_sdk_arc_region_switch.types.document_db_configuration

        return {
            "documentDbConfig": aws_sdk_arc_region_switch.types.document_db_configuration.serialize_aws_json_1_0(
                value["documentDbConfig"]
            )
        }
    elif "rdsPromoteReadReplicaConfig" in value:
        import aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration

        return {
            "rdsPromoteReadReplicaConfig": aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration.serialize_aws_json_1_0(
                value["rdsPromoteReadReplicaConfig"]
            )
        }
    elif "rdsCreateCrossRegionReadReplicaConfig" in value:
        import aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration

        return {
            "rdsCreateCrossRegionReadReplicaConfig": aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration.serialize_aws_json_1_0(
                value["rdsCreateCrossRegionReadReplicaConfig"]
            )
        }
    elif "lambdaEventSourceMappingConfig" in value:
        import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration

        return {
            "lambdaEventSourceMappingConfig": aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration.serialize_aws_json_1_0(
                value["lambdaEventSourceMappingConfig"]
            )
        }
    elif "auroraServerlessScalingConfig" in value:
        import aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration

        return {
            "auroraServerlessScalingConfig": aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration.serialize_aws_json_1_0(
                value["auroraServerlessScalingConfig"]
            )
        }
    elif "auroraProvisionedScalingConfig" in value:
        import aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration

        return {
            "auroraProvisionedScalingConfig": aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration.serialize_aws_json_1_0(
                value["auroraProvisionedScalingConfig"]
            )
        }
    elif "neptuneGlobalDatabaseConfig" in value:
        import aws_sdk_arc_region_switch.types.neptune_global_database_configuration

        return {
            "neptuneGlobalDatabaseConfig": aws_sdk_arc_region_switch.types.neptune_global_database_configuration.serialize_aws_json_1_0(
                value["neptuneGlobalDatabaseConfig"]
            )
        }
    else:
        raise SerializationError("ExecutionBlockConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ExecutionBlockConfiguration:
    if "customActionLambdaConfig" in data:
        import aws_sdk_arc_region_switch.types.custom_action_lambda_configuration

        return {
            "customActionLambdaConfig": aws_sdk_arc_region_switch.types.custom_action_lambda_configuration.deserialize_aws_json_1_0(
                data["customActionLambdaConfig"]
            )
        }
    elif "ec2AsgCapacityIncreaseConfig" in data:
        import aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration

        return {
            "ec2AsgCapacityIncreaseConfig": aws_sdk_arc_region_switch.types.ec2_asg_capacity_increase_configuration.deserialize_aws_json_1_0(
                data["ec2AsgCapacityIncreaseConfig"]
            )
        }
    elif "executionApprovalConfig" in data:
        import aws_sdk_arc_region_switch.types.execution_approval_configuration

        return {
            "executionApprovalConfig": aws_sdk_arc_region_switch.types.execution_approval_configuration.deserialize_aws_json_1_0(
                data["executionApprovalConfig"]
            )
        }
    elif "arcRoutingControlConfig" in data:
        import aws_sdk_arc_region_switch.types.arc_routing_control_configuration

        return {
            "arcRoutingControlConfig": aws_sdk_arc_region_switch.types.arc_routing_control_configuration.deserialize_aws_json_1_0(
                data["arcRoutingControlConfig"]
            )
        }
    elif "globalAuroraConfig" in data:
        import aws_sdk_arc_region_switch.types.global_aurora_configuration

        return {
            "globalAuroraConfig": aws_sdk_arc_region_switch.types.global_aurora_configuration.deserialize_aws_json_1_0(
                data["globalAuroraConfig"]
            )
        }
    elif "parallelConfig" in data:
        import aws_sdk_arc_region_switch.types.parallel_execution_block_configuration

        return {
            "parallelConfig": aws_sdk_arc_region_switch.types.parallel_execution_block_configuration.deserialize_aws_json_1_0(
                data["parallelConfig"]
            )
        }
    elif "regionSwitchPlanConfig" in data:
        import aws_sdk_arc_region_switch.types.region_switch_plan_configuration

        return {
            "regionSwitchPlanConfig": aws_sdk_arc_region_switch.types.region_switch_plan_configuration.deserialize_aws_json_1_0(
                data["regionSwitchPlanConfig"]
            )
        }
    elif "ecsCapacityIncreaseConfig" in data:
        import aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration

        return {
            "ecsCapacityIncreaseConfig": aws_sdk_arc_region_switch.types.ecs_capacity_increase_configuration.deserialize_aws_json_1_0(
                data["ecsCapacityIncreaseConfig"]
            )
        }
    elif "eksResourceScalingConfig" in data:
        import aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration

        return {
            "eksResourceScalingConfig": aws_sdk_arc_region_switch.types.eks_resource_scaling_configuration.deserialize_aws_json_1_0(
                data["eksResourceScalingConfig"]
            )
        }
    elif "route53HealthCheckConfig" in data:
        import aws_sdk_arc_region_switch.types.route53_health_check_configuration

        return {
            "route53HealthCheckConfig": aws_sdk_arc_region_switch.types.route53_health_check_configuration.deserialize_aws_json_1_0(
                data["route53HealthCheckConfig"]
            )
        }
    elif "documentDbConfig" in data:
        import aws_sdk_arc_region_switch.types.document_db_configuration

        return {
            "documentDbConfig": aws_sdk_arc_region_switch.types.document_db_configuration.deserialize_aws_json_1_0(
                data["documentDbConfig"]
            )
        }
    elif "rdsPromoteReadReplicaConfig" in data:
        import aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration

        return {
            "rdsPromoteReadReplicaConfig": aws_sdk_arc_region_switch.types.rds_promote_read_replica_configuration.deserialize_aws_json_1_0(
                data["rdsPromoteReadReplicaConfig"]
            )
        }
    elif "rdsCreateCrossRegionReadReplicaConfig" in data:
        import aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration

        return {
            "rdsCreateCrossRegionReadReplicaConfig": aws_sdk_arc_region_switch.types.rds_create_cross_region_replica_configuration.deserialize_aws_json_1_0(
                data["rdsCreateCrossRegionReadReplicaConfig"]
            )
        }
    elif "lambdaEventSourceMappingConfig" in data:
        import aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration

        return {
            "lambdaEventSourceMappingConfig": aws_sdk_arc_region_switch.types.lambda_event_source_mapping_configuration.deserialize_aws_json_1_0(
                data["lambdaEventSourceMappingConfig"]
            )
        }
    elif "auroraServerlessScalingConfig" in data:
        import aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration

        return {
            "auroraServerlessScalingConfig": aws_sdk_arc_region_switch.types.aurora_serverless_scaling_configuration.deserialize_aws_json_1_0(
                data["auroraServerlessScalingConfig"]
            )
        }
    elif "auroraProvisionedScalingConfig" in data:
        import aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration

        return {
            "auroraProvisionedScalingConfig": aws_sdk_arc_region_switch.types.aurora_provisioned_scaling_configuration.deserialize_aws_json_1_0(
                data["auroraProvisionedScalingConfig"]
            )
        }
    elif "neptuneGlobalDatabaseConfig" in data:
        import aws_sdk_arc_region_switch.types.neptune_global_database_configuration

        return {
            "neptuneGlobalDatabaseConfig": aws_sdk_arc_region_switch.types.neptune_global_database_configuration.deserialize_aws_json_1_0(
                data["neptuneGlobalDatabaseConfig"]
            )
        }
    else:
        raise DeserializationError(
            "ExecutionBlockConfiguration: no recognized variant key"
        )
