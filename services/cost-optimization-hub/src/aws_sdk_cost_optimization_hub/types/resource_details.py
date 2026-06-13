"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cost_optimization_hub.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage
    import aws_sdk_cost_optimization_hub.types.compute_savings_plans
    import aws_sdk_cost_optimization_hub.types.document_db_cluster
    import aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity
    import aws_sdk_cost_optimization_hub.types.dynamo_db_table
    import aws_sdk_cost_optimization_hub.types.ebs_volume
    import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group
    import aws_sdk_cost_optimization_hub.types.ec2_instance
    import aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans
    import aws_sdk_cost_optimization_hub.types.ec2_reserved_instances
    import aws_sdk_cost_optimization_hub.types.ecs_service
    import aws_sdk_cost_optimization_hub.types.elasti_cache_cluster
    import aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances
    import aws_sdk_cost_optimization_hub.types.lambda_function
    import aws_sdk_cost_optimization_hub.types.memory_db_cluster
    import aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances
    import aws_sdk_cost_optimization_hub.types.nat_gateway
    import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances
    import aws_sdk_cost_optimization_hub.types.rds_db_instance
    import aws_sdk_cost_optimization_hub.types.rds_db_instance_storage
    import aws_sdk_cost_optimization_hub.types.rds_reserved_instances
    import aws_sdk_cost_optimization_hub.types.redshift_reserved_instances
    import aws_sdk_cost_optimization_hub.types.sage_maker_endpoint
    import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans
    import aws_sdk_cost_optimization_hub.types.work_spaces


class _ResourceDetails_lambdaFunction(TypedDict):
    lambdaFunction: "aws_sdk_cost_optimization_hub.types.lambda_function.LambdaFunction"


class _ResourceDetails_ecsService(TypedDict):
    ecsService: "aws_sdk_cost_optimization_hub.types.ecs_service.EcsService"


class _ResourceDetails_ec2Instance(TypedDict):
    ec2Instance: "aws_sdk_cost_optimization_hub.types.ec2_instance.Ec2Instance"


class _ResourceDetails_ebsVolume(TypedDict):
    ebsVolume: "aws_sdk_cost_optimization_hub.types.ebs_volume.EbsVolume"


class _ResourceDetails_ec2AutoScalingGroup(TypedDict):
    ec2AutoScalingGroup: (
        "aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group.Ec2AutoScalingGroup"
    )


class _ResourceDetails_ec2ReservedInstances(TypedDict):
    ec2ReservedInstances: "aws_sdk_cost_optimization_hub.types.ec2_reserved_instances.Ec2ReservedInstances"


class _ResourceDetails_rdsReservedInstances(TypedDict):
    rdsReservedInstances: "aws_sdk_cost_optimization_hub.types.rds_reserved_instances.RdsReservedInstances"


class _ResourceDetails_elastiCacheReservedInstances(TypedDict):
    elastiCacheReservedInstances: "aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances.ElastiCacheReservedInstances"


class _ResourceDetails_openSearchReservedInstances(TypedDict):
    openSearchReservedInstances: "aws_sdk_cost_optimization_hub.types.open_search_reserved_instances.OpenSearchReservedInstances"


class _ResourceDetails_redshiftReservedInstances(TypedDict):
    redshiftReservedInstances: "aws_sdk_cost_optimization_hub.types.redshift_reserved_instances.RedshiftReservedInstances"


class _ResourceDetails_ec2InstanceSavingsPlans(TypedDict):
    ec2InstanceSavingsPlans: "aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans.Ec2InstanceSavingsPlans"


class _ResourceDetails_computeSavingsPlans(TypedDict):
    computeSavingsPlans: (
        "aws_sdk_cost_optimization_hub.types.compute_savings_plans.ComputeSavingsPlans"
    )


class _ResourceDetails_sageMakerSavingsPlans(TypedDict):
    sageMakerSavingsPlans: "aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans.SageMakerSavingsPlans"


class _ResourceDetails_rdsDbInstance(TypedDict):
    rdsDbInstance: "aws_sdk_cost_optimization_hub.types.rds_db_instance.RdsDbInstance"


class _ResourceDetails_rdsDbInstanceStorage(TypedDict):
    rdsDbInstanceStorage: "aws_sdk_cost_optimization_hub.types.rds_db_instance_storage.RdsDbInstanceStorage"


class _ResourceDetails_auroraDbClusterStorage(TypedDict):
    auroraDbClusterStorage: "aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage.AuroraDbClusterStorage"


class _ResourceDetails_dynamoDbReservedCapacity(TypedDict):
    dynamoDbReservedCapacity: "aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity.DynamoDbReservedCapacity"


class _ResourceDetails_memoryDbReservedInstances(TypedDict):
    memoryDbReservedInstances: "aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances.MemoryDbReservedInstances"


class _ResourceDetails_natGateway(TypedDict):
    natGateway: "aws_sdk_cost_optimization_hub.types.nat_gateway.NatGateway"


class _ResourceDetails_dynamoDbTable(TypedDict):
    dynamoDbTable: "aws_sdk_cost_optimization_hub.types.dynamo_db_table.DynamoDbTable"


class _ResourceDetails_elastiCacheCluster(TypedDict):
    elastiCacheCluster: (
        "aws_sdk_cost_optimization_hub.types.elasti_cache_cluster.ElastiCacheCluster"
    )


class _ResourceDetails_memoryDbCluster(TypedDict):
    memoryDbCluster: (
        "aws_sdk_cost_optimization_hub.types.memory_db_cluster.MemoryDbCluster"
    )


class _ResourceDetails_documentDbCluster(TypedDict):
    documentDbCluster: (
        "aws_sdk_cost_optimization_hub.types.document_db_cluster.DocumentDbCluster"
    )


class _ResourceDetails_workSpaces(TypedDict):
    workSpaces: "aws_sdk_cost_optimization_hub.types.work_spaces.WorkSpaces"


class _ResourceDetails_sageMakerEndpoint(TypedDict):
    sageMakerEndpoint: (
        "aws_sdk_cost_optimization_hub.types.sage_maker_endpoint.SageMakerEndpoint"
    )


ResourceDetails: TypeAlias = (
    _ResourceDetails_lambdaFunction
    | _ResourceDetails_ecsService
    | _ResourceDetails_ec2Instance
    | _ResourceDetails_ebsVolume
    | _ResourceDetails_ec2AutoScalingGroup
    | _ResourceDetails_ec2ReservedInstances
    | _ResourceDetails_rdsReservedInstances
    | _ResourceDetails_elastiCacheReservedInstances
    | _ResourceDetails_openSearchReservedInstances
    | _ResourceDetails_redshiftReservedInstances
    | _ResourceDetails_ec2InstanceSavingsPlans
    | _ResourceDetails_computeSavingsPlans
    | _ResourceDetails_sageMakerSavingsPlans
    | _ResourceDetails_rdsDbInstance
    | _ResourceDetails_rdsDbInstanceStorage
    | _ResourceDetails_auroraDbClusterStorage
    | _ResourceDetails_dynamoDbReservedCapacity
    | _ResourceDetails_memoryDbReservedInstances
    | _ResourceDetails_natGateway
    | _ResourceDetails_dynamoDbTable
    | _ResourceDetails_elastiCacheCluster
    | _ResourceDetails_memoryDbCluster
    | _ResourceDetails_documentDbCluster
    | _ResourceDetails_workSpaces
    | _ResourceDetails_sageMakerEndpoint
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDetails) -> dict:
    if "lambdaFunction" in value:
        import aws_sdk_cost_optimization_hub.types.lambda_function

        return {
            "lambdaFunction": aws_sdk_cost_optimization_hub.types.lambda_function.serialize_aws_json_1_0(
                value["lambdaFunction"]
            )
        }
    elif "ecsService" in value:
        import aws_sdk_cost_optimization_hub.types.ecs_service

        return {
            "ecsService": aws_sdk_cost_optimization_hub.types.ecs_service.serialize_aws_json_1_0(
                value["ecsService"]
            )
        }
    elif "ec2Instance" in value:
        import aws_sdk_cost_optimization_hub.types.ec2_instance

        return {
            "ec2Instance": aws_sdk_cost_optimization_hub.types.ec2_instance.serialize_aws_json_1_0(
                value["ec2Instance"]
            )
        }
    elif "ebsVolume" in value:
        import aws_sdk_cost_optimization_hub.types.ebs_volume

        return {
            "ebsVolume": aws_sdk_cost_optimization_hub.types.ebs_volume.serialize_aws_json_1_0(
                value["ebsVolume"]
            )
        }
    elif "ec2AutoScalingGroup" in value:
        import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group

        return {
            "ec2AutoScalingGroup": aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group.serialize_aws_json_1_0(
                value["ec2AutoScalingGroup"]
            )
        }
    elif "ec2ReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.ec2_reserved_instances

        return {
            "ec2ReservedInstances": aws_sdk_cost_optimization_hub.types.ec2_reserved_instances.serialize_aws_json_1_0(
                value["ec2ReservedInstances"]
            )
        }
    elif "rdsReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.rds_reserved_instances

        return {
            "rdsReservedInstances": aws_sdk_cost_optimization_hub.types.rds_reserved_instances.serialize_aws_json_1_0(
                value["rdsReservedInstances"]
            )
        }
    elif "elastiCacheReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances

        return {
            "elastiCacheReservedInstances": aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances.serialize_aws_json_1_0(
                value["elastiCacheReservedInstances"]
            )
        }
    elif "openSearchReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances

        return {
            "openSearchReservedInstances": aws_sdk_cost_optimization_hub.types.open_search_reserved_instances.serialize_aws_json_1_0(
                value["openSearchReservedInstances"]
            )
        }
    elif "redshiftReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.redshift_reserved_instances

        return {
            "redshiftReservedInstances": aws_sdk_cost_optimization_hub.types.redshift_reserved_instances.serialize_aws_json_1_0(
                value["redshiftReservedInstances"]
            )
        }
    elif "ec2InstanceSavingsPlans" in value:
        import aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans

        return {
            "ec2InstanceSavingsPlans": aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans.serialize_aws_json_1_0(
                value["ec2InstanceSavingsPlans"]
            )
        }
    elif "computeSavingsPlans" in value:
        import aws_sdk_cost_optimization_hub.types.compute_savings_plans

        return {
            "computeSavingsPlans": aws_sdk_cost_optimization_hub.types.compute_savings_plans.serialize_aws_json_1_0(
                value["computeSavingsPlans"]
            )
        }
    elif "sageMakerSavingsPlans" in value:
        import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans

        return {
            "sageMakerSavingsPlans": aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans.serialize_aws_json_1_0(
                value["sageMakerSavingsPlans"]
            )
        }
    elif "rdsDbInstance" in value:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance

        return {
            "rdsDbInstance": aws_sdk_cost_optimization_hub.types.rds_db_instance.serialize_aws_json_1_0(
                value["rdsDbInstance"]
            )
        }
    elif "rdsDbInstanceStorage" in value:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance_storage

        return {
            "rdsDbInstanceStorage": aws_sdk_cost_optimization_hub.types.rds_db_instance_storage.serialize_aws_json_1_0(
                value["rdsDbInstanceStorage"]
            )
        }
    elif "auroraDbClusterStorage" in value:
        import aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage

        return {
            "auroraDbClusterStorage": aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage.serialize_aws_json_1_0(
                value["auroraDbClusterStorage"]
            )
        }
    elif "dynamoDbReservedCapacity" in value:
        import aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity

        return {
            "dynamoDbReservedCapacity": aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity.serialize_aws_json_1_0(
                value["dynamoDbReservedCapacity"]
            )
        }
    elif "memoryDbReservedInstances" in value:
        import aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances

        return {
            "memoryDbReservedInstances": aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances.serialize_aws_json_1_0(
                value["memoryDbReservedInstances"]
            )
        }
    elif "natGateway" in value:
        import aws_sdk_cost_optimization_hub.types.nat_gateway

        return {
            "natGateway": aws_sdk_cost_optimization_hub.types.nat_gateway.serialize_aws_json_1_0(
                value["natGateway"]
            )
        }
    elif "dynamoDbTable" in value:
        import aws_sdk_cost_optimization_hub.types.dynamo_db_table

        return {
            "dynamoDbTable": aws_sdk_cost_optimization_hub.types.dynamo_db_table.serialize_aws_json_1_0(
                value["dynamoDbTable"]
            )
        }
    elif "elastiCacheCluster" in value:
        import aws_sdk_cost_optimization_hub.types.elasti_cache_cluster

        return {
            "elastiCacheCluster": aws_sdk_cost_optimization_hub.types.elasti_cache_cluster.serialize_aws_json_1_0(
                value["elastiCacheCluster"]
            )
        }
    elif "memoryDbCluster" in value:
        import aws_sdk_cost_optimization_hub.types.memory_db_cluster

        return {
            "memoryDbCluster": aws_sdk_cost_optimization_hub.types.memory_db_cluster.serialize_aws_json_1_0(
                value["memoryDbCluster"]
            )
        }
    elif "documentDbCluster" in value:
        import aws_sdk_cost_optimization_hub.types.document_db_cluster

        return {
            "documentDbCluster": aws_sdk_cost_optimization_hub.types.document_db_cluster.serialize_aws_json_1_0(
                value["documentDbCluster"]
            )
        }
    elif "workSpaces" in value:
        import aws_sdk_cost_optimization_hub.types.work_spaces

        return {
            "workSpaces": aws_sdk_cost_optimization_hub.types.work_spaces.serialize_aws_json_1_0(
                value["workSpaces"]
            )
        }
    elif "sageMakerEndpoint" in value:
        import aws_sdk_cost_optimization_hub.types.sage_maker_endpoint

        return {
            "sageMakerEndpoint": aws_sdk_cost_optimization_hub.types.sage_maker_endpoint.serialize_aws_json_1_0(
                value["sageMakerEndpoint"]
            )
        }
    else:
        raise SerializationError("ResourceDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ResourceDetails:
    if "lambdaFunction" in data:
        import aws_sdk_cost_optimization_hub.types.lambda_function

        return {
            "lambdaFunction": aws_sdk_cost_optimization_hub.types.lambda_function.deserialize_aws_json_1_0(
                data["lambdaFunction"]
            )
        }
    elif "ecsService" in data:
        import aws_sdk_cost_optimization_hub.types.ecs_service

        return {
            "ecsService": aws_sdk_cost_optimization_hub.types.ecs_service.deserialize_aws_json_1_0(
                data["ecsService"]
            )
        }
    elif "ec2Instance" in data:
        import aws_sdk_cost_optimization_hub.types.ec2_instance

        return {
            "ec2Instance": aws_sdk_cost_optimization_hub.types.ec2_instance.deserialize_aws_json_1_0(
                data["ec2Instance"]
            )
        }
    elif "ebsVolume" in data:
        import aws_sdk_cost_optimization_hub.types.ebs_volume

        return {
            "ebsVolume": aws_sdk_cost_optimization_hub.types.ebs_volume.deserialize_aws_json_1_0(
                data["ebsVolume"]
            )
        }
    elif "ec2AutoScalingGroup" in data:
        import aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group

        return {
            "ec2AutoScalingGroup": aws_sdk_cost_optimization_hub.types.ec2_auto_scaling_group.deserialize_aws_json_1_0(
                data["ec2AutoScalingGroup"]
            )
        }
    elif "ec2ReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.ec2_reserved_instances

        return {
            "ec2ReservedInstances": aws_sdk_cost_optimization_hub.types.ec2_reserved_instances.deserialize_aws_json_1_0(
                data["ec2ReservedInstances"]
            )
        }
    elif "rdsReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.rds_reserved_instances

        return {
            "rdsReservedInstances": aws_sdk_cost_optimization_hub.types.rds_reserved_instances.deserialize_aws_json_1_0(
                data["rdsReservedInstances"]
            )
        }
    elif "elastiCacheReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances

        return {
            "elastiCacheReservedInstances": aws_sdk_cost_optimization_hub.types.elasti_cache_reserved_instances.deserialize_aws_json_1_0(
                data["elastiCacheReservedInstances"]
            )
        }
    elif "openSearchReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.open_search_reserved_instances

        return {
            "openSearchReservedInstances": aws_sdk_cost_optimization_hub.types.open_search_reserved_instances.deserialize_aws_json_1_0(
                data["openSearchReservedInstances"]
            )
        }
    elif "redshiftReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.redshift_reserved_instances

        return {
            "redshiftReservedInstances": aws_sdk_cost_optimization_hub.types.redshift_reserved_instances.deserialize_aws_json_1_0(
                data["redshiftReservedInstances"]
            )
        }
    elif "ec2InstanceSavingsPlans" in data:
        import aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans

        return {
            "ec2InstanceSavingsPlans": aws_sdk_cost_optimization_hub.types.ec2_instance_savings_plans.deserialize_aws_json_1_0(
                data["ec2InstanceSavingsPlans"]
            )
        }
    elif "computeSavingsPlans" in data:
        import aws_sdk_cost_optimization_hub.types.compute_savings_plans

        return {
            "computeSavingsPlans": aws_sdk_cost_optimization_hub.types.compute_savings_plans.deserialize_aws_json_1_0(
                data["computeSavingsPlans"]
            )
        }
    elif "sageMakerSavingsPlans" in data:
        import aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans

        return {
            "sageMakerSavingsPlans": aws_sdk_cost_optimization_hub.types.sage_maker_savings_plans.deserialize_aws_json_1_0(
                data["sageMakerSavingsPlans"]
            )
        }
    elif "rdsDbInstance" in data:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance

        return {
            "rdsDbInstance": aws_sdk_cost_optimization_hub.types.rds_db_instance.deserialize_aws_json_1_0(
                data["rdsDbInstance"]
            )
        }
    elif "rdsDbInstanceStorage" in data:
        import aws_sdk_cost_optimization_hub.types.rds_db_instance_storage

        return {
            "rdsDbInstanceStorage": aws_sdk_cost_optimization_hub.types.rds_db_instance_storage.deserialize_aws_json_1_0(
                data["rdsDbInstanceStorage"]
            )
        }
    elif "auroraDbClusterStorage" in data:
        import aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage

        return {
            "auroraDbClusterStorage": aws_sdk_cost_optimization_hub.types.aurora_db_cluster_storage.deserialize_aws_json_1_0(
                data["auroraDbClusterStorage"]
            )
        }
    elif "dynamoDbReservedCapacity" in data:
        import aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity

        return {
            "dynamoDbReservedCapacity": aws_sdk_cost_optimization_hub.types.dynamo_db_reserved_capacity.deserialize_aws_json_1_0(
                data["dynamoDbReservedCapacity"]
            )
        }
    elif "memoryDbReservedInstances" in data:
        import aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances

        return {
            "memoryDbReservedInstances": aws_sdk_cost_optimization_hub.types.memory_db_reserved_instances.deserialize_aws_json_1_0(
                data["memoryDbReservedInstances"]
            )
        }
    elif "natGateway" in data:
        import aws_sdk_cost_optimization_hub.types.nat_gateway

        return {
            "natGateway": aws_sdk_cost_optimization_hub.types.nat_gateway.deserialize_aws_json_1_0(
                data["natGateway"]
            )
        }
    elif "dynamoDbTable" in data:
        import aws_sdk_cost_optimization_hub.types.dynamo_db_table

        return {
            "dynamoDbTable": aws_sdk_cost_optimization_hub.types.dynamo_db_table.deserialize_aws_json_1_0(
                data["dynamoDbTable"]
            )
        }
    elif "elastiCacheCluster" in data:
        import aws_sdk_cost_optimization_hub.types.elasti_cache_cluster

        return {
            "elastiCacheCluster": aws_sdk_cost_optimization_hub.types.elasti_cache_cluster.deserialize_aws_json_1_0(
                data["elastiCacheCluster"]
            )
        }
    elif "memoryDbCluster" in data:
        import aws_sdk_cost_optimization_hub.types.memory_db_cluster

        return {
            "memoryDbCluster": aws_sdk_cost_optimization_hub.types.memory_db_cluster.deserialize_aws_json_1_0(
                data["memoryDbCluster"]
            )
        }
    elif "documentDbCluster" in data:
        import aws_sdk_cost_optimization_hub.types.document_db_cluster

        return {
            "documentDbCluster": aws_sdk_cost_optimization_hub.types.document_db_cluster.deserialize_aws_json_1_0(
                data["documentDbCluster"]
            )
        }
    elif "workSpaces" in data:
        import aws_sdk_cost_optimization_hub.types.work_spaces

        return {
            "workSpaces": aws_sdk_cost_optimization_hub.types.work_spaces.deserialize_aws_json_1_0(
                data["workSpaces"]
            )
        }
    elif "sageMakerEndpoint" in data:
        import aws_sdk_cost_optimization_hub.types.sage_maker_endpoint

        return {
            "sageMakerEndpoint": aws_sdk_cost_optimization_hub.types.sage_maker_endpoint.deserialize_aws_json_1_0(
                data["sageMakerEndpoint"]
            )
        }
    else:
        raise DeserializationError("ResourceDetails: no recognized variant key")
