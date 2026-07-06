"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_application_auto_scaling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.alarms
    import aws_sdk_application_auto_scaling.types.policy_name
    import aws_sdk_application_auto_scaling.types.policy_type
    import aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration
    import aws_sdk_application_auto_scaling.types.resource_id_max_len1600
    import aws_sdk_application_auto_scaling.types.scalable_dimension
    import aws_sdk_application_auto_scaling.types.service_namespace
    import aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration
    import aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration
    import aws_sdk_application_auto_scaling.types.timestamp_type


class ScalingPolicy(TypedDict, closed=True):
    policy_arn: "aws_sdk_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    """<p>The Amazon Resource Name (ARN) of the scaling policy.</p>"""
    policy_name: "aws_sdk_application_auto_scaling.types.policy_name.PolicyName"
    """<p>The name of the scaling policy.</p>"""
    service_namespace: (
        "aws_sdk_application_auto_scaling.types.service_namespace.ServiceNamespace"
    )
    """<p>The namespace of the Amazon Web Services service that provides the resource, or a <code>custom-resource</code>.</p>"""
    resource_id: "aws_sdk_application_auto_scaling.types.resource_id_max_len1600.ResourceIdMaxLen1600"
    r"""<p>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.</p> <ul> <li> <p>ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.</p> </li> <li> <p>Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.</p> </li> <li> <p>EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.</p> </li> <li> <p>AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.</p> </li> <li> <p>DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.</p> </li> <li> <p>DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.</p> </li> <li> <p>Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.</p> </li> <li> <p>SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our <a href=\"https://github.com/aws/aws-auto-scaling-custom-resource\">GitHub repository</a>.</p> </li> <li> <p>Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.</p> </li> <li> <p>Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.</p> </li> <li> <p>Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.</p> </li> <li> <p>Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.</p> </li> <li> <p>Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.</p> </li> <li> <p>Amazon ElastiCache cache cluster - The resource type is <code>cache-cluster</code> and the unique identifier is the cache cluster name. Example: <code>cache-cluster/mycluster</code>.</p> </li> <li> <p>Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.</p> </li> <li> <p>SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.</p> </li> <li> <p>SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</p> </li> <li> <p>Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</p> </li> </ul>"""
    scalable_dimension: (
        "aws_sdk_application_auto_scaling.types.scalable_dimension.ScalableDimension"
    )
    """<p>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.</p> <ul> <li> <p> <code>ecs:service:DesiredCount</code> - The task count of an ECS service.</p> </li> <li> <p> <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.</p> </li> <li> <p> <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.</p> </li> <li> <p> <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.</p> </li> <li> <p> <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.</p> </li> <li> <p> <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.</p> </li> <li> <p> <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.</p> </li> <li> <p> <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.</p> </li> <li> <p> <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.</p> </li> <li> <p> <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.</p> </li> <li> <p> <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.</p> </li> <li> <p> <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.</p> </li> <li> <p> <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.</p> </li> <li> <p> <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.</p> </li> <li> <p> <code>elasticache:cache-cluster:Nodes</code> - The number of nodes for an Amazon ElastiCache cache cluster.</p> </li> <li> <p> <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.</p> </li> <li> <p> <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.</p> </li> <li> <p> <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.</p> </li> <li> <p> <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</p> </li> <li> <p> <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</p> </li> </ul>"""
    policy_type: "aws_sdk_application_auto_scaling.types.policy_type.PolicyType"
    """<p>The scaling policy type.</p> <p>The following policy types are supported: </p> <p> <code>TargetTrackingScaling</code>—Not supported for Amazon EMR</p> <p> <code>StepScaling</code>—Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</p> <p> <code>PredictiveScaling</code>—Only supported for Amazon ECS</p>"""
    step_scaling_policy_configuration: NotRequired[
        "aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration.StepScalingPolicyConfiguration"
    ]
    """<p>A step scaling policy.</p>"""
    target_tracking_scaling_policy_configuration: NotRequired[
        "aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration.TargetTrackingScalingPolicyConfiguration"
    ]
    """<p>A target tracking scaling policy.</p>"""
    predictive_scaling_policy_configuration: NotRequired[
        "aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration.PredictiveScalingPolicyConfiguration"
    ]
    """<p> The predictive scaling policy configuration. </p>"""
    alarms: NotRequired["aws_sdk_application_auto_scaling.types.alarms.Alarms"]
    """<p>The CloudWatch alarms associated with the scaling policy.</p>"""
    creation_time: "aws_sdk_application_auto_scaling.types.timestamp_type.TimestampType"
    """<p>The Unix timestamp for when the scaling policy was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingPolicy) -> dict:
    out: dict = {}
    out["PolicyARN"] = value["policy_arn"]
    out["PolicyName"] = value["policy_name"]
    import aws_sdk_application_auto_scaling.types.service_namespace

    out["ServiceNamespace"] = (
        aws_sdk_application_auto_scaling.types.service_namespace.serialize_aws_json_1_1(
            value["service_namespace"]
        )
    )
    out["ResourceId"] = value["resource_id"]
    import aws_sdk_application_auto_scaling.types.scalable_dimension

    out["ScalableDimension"] = (
        aws_sdk_application_auto_scaling.types.scalable_dimension.serialize_aws_json_1_1(
            value["scalable_dimension"]
        )
    )
    import aws_sdk_application_auto_scaling.types.policy_type

    out["PolicyType"] = (
        aws_sdk_application_auto_scaling.types.policy_type.serialize_aws_json_1_1(
            value["policy_type"]
        )
    )
    if "step_scaling_policy_configuration" in value:
        import aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration

        out["StepScalingPolicyConfiguration"] = (
            aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration.serialize_aws_json_1_1(
                value["step_scaling_policy_configuration"]
            )
        )
    if "target_tracking_scaling_policy_configuration" in value:
        import aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration

        out["TargetTrackingScalingPolicyConfiguration"] = (
            aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration.serialize_aws_json_1_1(
                value["target_tracking_scaling_policy_configuration"]
            )
        )
    if "predictive_scaling_policy_configuration" in value:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration

        out["PredictiveScalingPolicyConfiguration"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration.serialize_aws_json_1_1(
                value["predictive_scaling_policy_configuration"]
            )
        )
    if "alarms" in value:
        import aws_sdk_application_auto_scaling.types.alarms

        out["Alarms"] = (
            aws_sdk_application_auto_scaling.types.alarms.serialize_aws_json_1_1(
                value["alarms"]
            )
        )
    import aws_sdk_application_auto_scaling.types.timestamp_type

    out["CreationTime"] = (
        aws_sdk_application_auto_scaling.types.timestamp_type.serialize_aws_json_1_1(
            value["creation_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingPolicy:
    out: ScalingPolicy = {}  # type: ignore[typeddict-item]
    if "PolicyARN" in data:
        out["policy_arn"] = data["PolicyARN"]
    else:
        raise DeserializationError("ScalingPolicy.policy_arn required")
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    else:
        raise DeserializationError("ScalingPolicy.policy_name required")
    if "ServiceNamespace" in data:
        import aws_sdk_application_auto_scaling.types.service_namespace

        out["service_namespace"] = (
            aws_sdk_application_auto_scaling.types.service_namespace.deserialize_aws_json_1_1(
                data["ServiceNamespace"]
            )
        )
    else:
        raise DeserializationError("ScalingPolicy.service_namespace required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ScalingPolicy.resource_id required")
    if "ScalableDimension" in data:
        import aws_sdk_application_auto_scaling.types.scalable_dimension

        out["scalable_dimension"] = (
            aws_sdk_application_auto_scaling.types.scalable_dimension.deserialize_aws_json_1_1(
                data["ScalableDimension"]
            )
        )
    else:
        raise DeserializationError("ScalingPolicy.scalable_dimension required")
    if "PolicyType" in data:
        import aws_sdk_application_auto_scaling.types.policy_type

        out["policy_type"] = (
            aws_sdk_application_auto_scaling.types.policy_type.deserialize_aws_json_1_1(
                data["PolicyType"]
            )
        )
    else:
        raise DeserializationError("ScalingPolicy.policy_type required")
    if "StepScalingPolicyConfiguration" in data:
        import aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration

        out["step_scaling_policy_configuration"] = (
            aws_sdk_application_auto_scaling.types.step_scaling_policy_configuration.deserialize_aws_json_1_1(
                data["StepScalingPolicyConfiguration"]
            )
        )
    if "TargetTrackingScalingPolicyConfiguration" in data:
        import aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration

        out["target_tracking_scaling_policy_configuration"] = (
            aws_sdk_application_auto_scaling.types.target_tracking_scaling_policy_configuration.deserialize_aws_json_1_1(
                data["TargetTrackingScalingPolicyConfiguration"]
            )
        )
    if "PredictiveScalingPolicyConfiguration" in data:
        import aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration

        out["predictive_scaling_policy_configuration"] = (
            aws_sdk_application_auto_scaling.types.predictive_scaling_policy_configuration.deserialize_aws_json_1_1(
                data["PredictiveScalingPolicyConfiguration"]
            )
        )
    if "Alarms" in data:
        import aws_sdk_application_auto_scaling.types.alarms

        out["alarms"] = (
            aws_sdk_application_auto_scaling.types.alarms.deserialize_aws_json_1_1(
                data["Alarms"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_application_auto_scaling.types.timestamp_type

        out["creation_time"] = (
            aws_sdk_application_auto_scaling.types.timestamp_type.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError("ScalingPolicy.creation_time required")
    return out
