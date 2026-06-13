"""Generated from Smithy shape ``com.amazonaws.braket#GetJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_braket.types.algorithm_specification
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.device_config
    import aws_sdk_braket.types.hybrid_job_queue_info
    import aws_sdk_braket.types.hyper_parameters
    import aws_sdk_braket.types.input_config_list
    import aws_sdk_braket.types.instance_config
    import aws_sdk_braket.types.job_arn
    import aws_sdk_braket.types.job_checkpoint_config
    import aws_sdk_braket.types.job_events
    import aws_sdk_braket.types.job_output_data_config
    import aws_sdk_braket.types.job_primary_status
    import aws_sdk_braket.types.job_stopping_condition
    import aws_sdk_braket.types.role_arn
    import aws_sdk_braket.types.string1024
    import aws_sdk_braket.types.tags_map


class GetJobResponse(TypedDict):
    status: "aws_sdk_braket.types.job_primary_status.JobPrimaryStatus"
    """<p>The status of the Amazon Braket hybrid job.</p>"""
    job_arn: "aws_sdk_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job.</p>"""
    role_arn: "aws_sdk_braket.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and other hybrid job details to the s3 buckets of a user.</p>"""
    failure_reason: NotRequired["aws_sdk_braket.types.string1024.String1024"]
    """<p>A description of the reason why an Amazon Braket hybrid job failed, if it failed.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_braket.types.hyper_parameters.HyperParameters"
    ]
    """<p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the traiing job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of th hyperparameter.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_braket.types.input_config_list.InputConfigList"
    ]
    """<p>A list of parameters that specify the name and type of input data and where it is located.</p>"""
    output_data_config: (
        "aws_sdk_braket.types.job_output_data_config.JobOutputDataConfig"
    )
    """<p>The path to the S3 location where hybrid job artifacts are stored and the encryption key used to store them there.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_braket.types.job_stopping_condition.JobStoppingCondition"
    ]
    """<p>The user-defined criteria that specifies when to stop a running hybrid job.</p>"""
    checkpoint_config: NotRequired[
        "aws_sdk_braket.types.job_checkpoint_config.JobCheckpointConfig"
    ]
    """<p>Information about the output locations for hybrid job checkpoint data.</p>"""
    algorithm_specification: (
        "aws_sdk_braket.types.algorithm_specification.AlgorithmSpecification"
    )
    """<p>Definition of the Amazon Braket hybrid job created. Provides information about the container image used, and the Python scripts used for training.</p>"""
    instance_config: "aws_sdk_braket.types.instance_config.InstanceConfig"
    """<p>The resource instances to use while running the hybrid job on Amazon Braket.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the Amazon Braket hybrid job was created.</p>"""
    started_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job was started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the Amazon Braket hybrid job ended.</p>"""
    billable_duration: NotRequired["int"]
    """<p>The billable time for which the Amazon Braket hybrid job used to complete.</p>"""
    device_config: NotRequired["aws_sdk_braket.types.device_config.DeviceConfig"]
    """<p>The primary device used by the Amazon Braket hybrid job.</p>"""
    events: NotRequired["aws_sdk_braket.types.job_events.JobEvents"]
    """<p>Details about the time and type of events occurred related to the Amazon Braket hybrid job.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>The tags associated with this hybrid job.</p>"""
    queue_info: NotRequired[
        "aws_sdk_braket.types.hybrid_job_queue_info.HybridJobQueueInfo"
    ]
    """<p>Queue information for the requested hybrid job. Only returned if <code>QueueInfo</code> is specified in the <code>additionalAttributeNames\"</code> field in the <code>GetJob</code> API request.</p>"""
    associations: NotRequired["aws_sdk_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResponse) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    out["jobArn"] = value["job_arn"]
    out["roleArn"] = value["role_arn"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["jobName"] = value["job_name"]
    if "hyper_parameters" in value:
        import aws_sdk_braket.types.hyper_parameters

        out["hyperParameters"] = aws_sdk_braket.types.hyper_parameters.serialize_json(
            value["hyper_parameters"]
        )
    if "input_data_config" in value:
        import aws_sdk_braket.types.input_config_list

        out["inputDataConfig"] = aws_sdk_braket.types.input_config_list.serialize_json(
            value["input_data_config"]
        )
    import aws_sdk_braket.types.job_output_data_config

    out["outputDataConfig"] = (
        aws_sdk_braket.types.job_output_data_config.serialize_json(
            value["output_data_config"]
        )
    )
    if "stopping_condition" in value:
        import aws_sdk_braket.types.job_stopping_condition

        out["stoppingCondition"] = (
            aws_sdk_braket.types.job_stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    if "checkpoint_config" in value:
        import aws_sdk_braket.types.job_checkpoint_config

        out["checkpointConfig"] = (
            aws_sdk_braket.types.job_checkpoint_config.serialize_json(
                value["checkpoint_config"]
            )
        )
    import aws_sdk_braket.types.algorithm_specification

    out["algorithmSpecification"] = (
        aws_sdk_braket.types.algorithm_specification.serialize_json(
            value["algorithm_specification"]
        )
    )
    import aws_sdk_braket.types.instance_config

    out["instanceConfig"] = aws_sdk_braket.types.instance_config.serialize_json(
        value["instance_config"]
    )
    import aws_sdk_braket.types._prelude.timestamp

    out["createdAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "started_at" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["startedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["started_at"]
        )
    if "ended_at" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["endedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "billable_duration" in value:
        out["billableDuration"] = value["billable_duration"]
    if "device_config" in value:
        import aws_sdk_braket.types.device_config

        out["deviceConfig"] = aws_sdk_braket.types.device_config.serialize_json(
            value["device_config"]
        )
    if "events" in value:
        import aws_sdk_braket.types.job_events

        out["events"] = aws_sdk_braket.types.job_events.serialize_json(value["events"])
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    if "queue_info" in value:
        import aws_sdk_braket.types.hybrid_job_queue_info

        out["queueInfo"] = aws_sdk_braket.types.hybrid_job_queue_info.serialize_json(
            value["queue_info"]
        )
    if "associations" in value:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.serialize_json(
            value["associations"]
        )
    return out


def deserialize_json(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetJobResponse.status required")
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("GetJobResponse.job_arn required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("GetJobResponse.role_arn required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("GetJobResponse.job_name required")
    if "hyperParameters" in data:
        import aws_sdk_braket.types.hyper_parameters

        out["hyper_parameters"] = (
            aws_sdk_braket.types.hyper_parameters.deserialize_json(
                data["hyperParameters"]
            )
        )
    if "inputDataConfig" in data:
        import aws_sdk_braket.types.input_config_list

        out["input_data_config"] = (
            aws_sdk_braket.types.input_config_list.deserialize_json(
                data["inputDataConfig"]
            )
        )
    if "outputDataConfig" in data:
        import aws_sdk_braket.types.job_output_data_config

        out["output_data_config"] = (
            aws_sdk_braket.types.job_output_data_config.deserialize_json(
                data["outputDataConfig"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.output_data_config required")
    if "stoppingCondition" in data:
        import aws_sdk_braket.types.job_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_braket.types.job_stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if "checkpointConfig" in data:
        import aws_sdk_braket.types.job_checkpoint_config

        out["checkpoint_config"] = (
            aws_sdk_braket.types.job_checkpoint_config.deserialize_json(
                data["checkpointConfig"]
            )
        )
    if "algorithmSpecification" in data:
        import aws_sdk_braket.types.algorithm_specification

        out["algorithm_specification"] = (
            aws_sdk_braket.types.algorithm_specification.deserialize_json(
                data["algorithmSpecification"]
            )
        )
    else:
        raise DeserializationError("GetJobResponse.algorithm_specification required")
    if "instanceConfig" in data:
        import aws_sdk_braket.types.instance_config

        out["instance_config"] = aws_sdk_braket.types.instance_config.deserialize_json(
            data["instanceConfig"]
        )
    else:
        raise DeserializationError("GetJobResponse.instance_config required")
    if "createdAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["created_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetJobResponse.created_at required")
    if "startedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["started_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["startedAt"]
        )
    if "endedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["ended_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "billableDuration" in data:
        out["billable_duration"] = data["billableDuration"]
    if "deviceConfig" in data:
        import aws_sdk_braket.types.device_config

        out["device_config"] = aws_sdk_braket.types.device_config.deserialize_json(
            data["deviceConfig"]
        )
    if "events" in data:
        import aws_sdk_braket.types.job_events

        out["events"] = aws_sdk_braket.types.job_events.deserialize_json(data["events"])
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    if "queueInfo" in data:
        import aws_sdk_braket.types.hybrid_job_queue_info

        out["queue_info"] = aws_sdk_braket.types.hybrid_job_queue_info.deserialize_json(
            data["queueInfo"]
        )
    if "associations" in data:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.deserialize_json(
            data["associations"]
        )
    return out
