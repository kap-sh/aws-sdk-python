"""Generated from Smithy shape ``com.amazonaws.scheduler#Target``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_scheduler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.dead_letter_config
    import aws_sdk_scheduler.types.ecs_parameters
    import aws_sdk_scheduler.types.event_bridge_parameters
    import aws_sdk_scheduler.types.kinesis_parameters
    import aws_sdk_scheduler.types.retry_policy
    import aws_sdk_scheduler.types.role_arn
    import aws_sdk_scheduler.types.sage_maker_pipeline_parameters
    import aws_sdk_scheduler.types.sqs_parameters
    import aws_sdk_scheduler.types.target_arn
    import aws_sdk_scheduler.types.target_input


class Target(TypedDict):
    arn: "aws_sdk_scheduler.types.target_arn.TargetArn"
    """<p>The Amazon Resource Name (ARN) of the target.</p>"""
    role_arn: "aws_sdk_scheduler.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that EventBridge Scheduler will use for this target when the schedule is invoked.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_scheduler.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>An object that contains information about an Amazon SQS queue that EventBridge Scheduler uses as a dead-letter queue for your schedule. If specified, EventBridge Scheduler delivers failed events that could not be successfully delivered to a target to the queue.</p>"""
    retry_policy: NotRequired["aws_sdk_scheduler.types.retry_policy.RetryPolicy"]
    """<p>A <code>RetryPolicy</code> object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.</p>"""
    input: NotRequired["aws_sdk_scheduler.types.target_input.TargetInput"]
    """<p>The text, or well-formed JSON, passed to the target. If you are configuring a templated Lambda, AWS Step Functions, or Amazon EventBridge target, the input must be a well-formed JSON. For all other target types, a JSON is not required. If you do not specify anything for this field, EventBridge Scheduler delivers a default notification to the target.</p>"""
    ecs_parameters: NotRequired["aws_sdk_scheduler.types.ecs_parameters.EcsParameters"]
    r"""<p>The templated target type for the Amazon ECS <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_RunTask.html\"> <code>RunTask</code> </a> API operation.</p>"""
    event_bridge_parameters: NotRequired[
        "aws_sdk_scheduler.types.event_bridge_parameters.EventBridgeParameters"
    ]
    r"""<p>The templated target type for the EventBridge <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html\"> <code>PutEvents</code> </a> API operation.</p>"""
    kinesis_parameters: NotRequired[
        "aws_sdk_scheduler.types.kinesis_parameters.KinesisParameters"
    ]
    r"""<p>The templated target type for the Amazon Kinesis <a href=\"kinesis/latest/APIReference/API_PutRecord.html\"> <code>PutRecord</code> </a> API operation.</p>"""
    sage_maker_pipeline_parameters: NotRequired[
        "aws_sdk_scheduler.types.sage_maker_pipeline_parameters.SageMakerPipelineParameters"
    ]
    r"""<p>The templated target type for the Amazon SageMaker <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html\"> <code>StartPipelineExecution</code> </a> API operation.</p>"""
    sqs_parameters: NotRequired["aws_sdk_scheduler.types.sqs_parameters.SqsParameters"]
    r"""<p>The templated target type for the Amazon SQS <a href=\"https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html\"> <code>SendMessage</code> </a> API operation. Contains the message group ID to use when the target is a FIFO queue. If you specify an Amazon SQS FIFO queue as a target, the queue must have content-based deduplication enabled. For more information, see <a href=\"https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html\">Using the Amazon SQS message deduplication ID</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["RoleArn"] = value["role_arn"]
    if "dead_letter_config" in value:
        import aws_sdk_scheduler.types.dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_scheduler.types.dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "retry_policy" in value:
        import aws_sdk_scheduler.types.retry_policy

        out["RetryPolicy"] = aws_sdk_scheduler.types.retry_policy.serialize_json(
            value["retry_policy"]
        )
    if "input" in value:
        out["Input"] = value["input"]
    if "ecs_parameters" in value:
        import aws_sdk_scheduler.types.ecs_parameters

        out["EcsParameters"] = aws_sdk_scheduler.types.ecs_parameters.serialize_json(
            value["ecs_parameters"]
        )
    if "event_bridge_parameters" in value:
        import aws_sdk_scheduler.types.event_bridge_parameters

        out["EventBridgeParameters"] = (
            aws_sdk_scheduler.types.event_bridge_parameters.serialize_json(
                value["event_bridge_parameters"]
            )
        )
    if "kinesis_parameters" in value:
        import aws_sdk_scheduler.types.kinesis_parameters

        out["KinesisParameters"] = (
            aws_sdk_scheduler.types.kinesis_parameters.serialize_json(
                value["kinesis_parameters"]
            )
        )
    if "sage_maker_pipeline_parameters" in value:
        import aws_sdk_scheduler.types.sage_maker_pipeline_parameters

        out["SageMakerPipelineParameters"] = (
            aws_sdk_scheduler.types.sage_maker_pipeline_parameters.serialize_json(
                value["sage_maker_pipeline_parameters"]
            )
        )
    if "sqs_parameters" in value:
        import aws_sdk_scheduler.types.sqs_parameters

        out["SqsParameters"] = aws_sdk_scheduler.types.sqs_parameters.serialize_json(
            value["sqs_parameters"]
        )
    return out


def deserialize_json(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Target.arn required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("Target.role_arn required")
    if "DeadLetterConfig" in data:
        import aws_sdk_scheduler.types.dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_scheduler.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if "RetryPolicy" in data:
        import aws_sdk_scheduler.types.retry_policy

        out["retry_policy"] = aws_sdk_scheduler.types.retry_policy.deserialize_json(
            data["RetryPolicy"]
        )
    if "Input" in data:
        out["input"] = data["Input"]
    if "EcsParameters" in data:
        import aws_sdk_scheduler.types.ecs_parameters

        out["ecs_parameters"] = aws_sdk_scheduler.types.ecs_parameters.deserialize_json(
            data["EcsParameters"]
        )
    if "EventBridgeParameters" in data:
        import aws_sdk_scheduler.types.event_bridge_parameters

        out["event_bridge_parameters"] = (
            aws_sdk_scheduler.types.event_bridge_parameters.deserialize_json(
                data["EventBridgeParameters"]
            )
        )
    if "KinesisParameters" in data:
        import aws_sdk_scheduler.types.kinesis_parameters

        out["kinesis_parameters"] = (
            aws_sdk_scheduler.types.kinesis_parameters.deserialize_json(
                data["KinesisParameters"]
            )
        )
    if "SageMakerPipelineParameters" in data:
        import aws_sdk_scheduler.types.sage_maker_pipeline_parameters

        out["sage_maker_pipeline_parameters"] = (
            aws_sdk_scheduler.types.sage_maker_pipeline_parameters.deserialize_json(
                data["SageMakerPipelineParameters"]
            )
        )
    if "SqsParameters" in data:
        import aws_sdk_scheduler.types.sqs_parameters

        out["sqs_parameters"] = aws_sdk_scheduler.types.sqs_parameters.deserialize_json(
            data["SqsParameters"]
        )
    return out
