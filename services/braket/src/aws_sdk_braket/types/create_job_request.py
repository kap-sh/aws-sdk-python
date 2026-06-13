"""Generated from Smithy shape ``com.amazonaws.braket#CreateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.algorithm_specification
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.device_config
    import aws_sdk_braket.types.hyper_parameters
    import aws_sdk_braket.types.input_config_list
    import aws_sdk_braket.types.instance_config
    import aws_sdk_braket.types.job_checkpoint_config
    import aws_sdk_braket.types.job_output_data_config
    import aws_sdk_braket.types.job_stopping_condition
    import aws_sdk_braket.types.role_arn
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map


class CreateJobRequest(TypedDict):
    client_token: "aws_sdk_braket.types.string64.String64"
    """<p>The client token associated with this request that guarantees that the request is idempotent.</p>"""
    algorithm_specification: (
        "aws_sdk_braket.types.algorithm_specification.AlgorithmSpecification"
    )
    """<p>Definition of the Amazon Braket job to be created. Specifies the container image the job uses and information about the Python scripts used for entry and training.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_braket.types.input_config_list.InputConfigList"
    ]
    """<p>A list of parameters that specify the name and type of input data and where it is located.</p>"""
    output_data_config: (
        "aws_sdk_braket.types.job_output_data_config.JobOutputDataConfig"
    )
    """<p>The path to the S3 location where you want to store hybrid job artifacts and the encryption key used to store them.</p>"""
    checkpoint_config: NotRequired[
        "aws_sdk_braket.types.job_checkpoint_config.JobCheckpointConfig"
    ]
    """<p>Information about the output locations for hybrid job checkpoint data.</p>"""
    job_name: "str"
    """<p>The name of the Amazon Braket hybrid job.</p>"""
    role_arn: "aws_sdk_braket.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output results and hybrid job details to the users' s3 buckets.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_braket.types.job_stopping_condition.JobStoppingCondition"
    ]
    """<p> The user-defined criteria that specifies when a hybrid job stops running.</p>"""
    instance_config: "aws_sdk_braket.types.instance_config.InstanceConfig"
    """<p>Configuration of the resource instances to use while running the hybrid job on Amazon Braket.</p>"""
    hyper_parameters: NotRequired[
        "aws_sdk_braket.types.hyper_parameters.HyperParameters"
    ]
    """<p>Algorithm-specific parameters used by an Amazon Braket hybrid job that influence the quality of the training job. The values are set with a map of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of the hyperparameter.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any hyperparameter fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request hyperparameter variable or plain text fields.</p> </important>"""
    device_config: "aws_sdk_braket.types.device_config.DeviceConfig"
    """<p>The quantum processing unit (QPU) or simulator used to create an Amazon Braket hybrid job.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>Tags to be added to the hybrid job you're creating.</p>"""
    associations: NotRequired["aws_sdk_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the hybrid job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    import aws_sdk_braket.types.algorithm_specification

    out["algorithmSpecification"] = (
        aws_sdk_braket.types.algorithm_specification.serialize_json(
            value["algorithm_specification"]
        )
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
    if "checkpoint_config" in value:
        import aws_sdk_braket.types.job_checkpoint_config

        out["checkpointConfig"] = (
            aws_sdk_braket.types.job_checkpoint_config.serialize_json(
                value["checkpoint_config"]
            )
        )
    out["jobName"] = value["job_name"]
    out["roleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import aws_sdk_braket.types.job_stopping_condition

        out["stoppingCondition"] = (
            aws_sdk_braket.types.job_stopping_condition.serialize_json(
                value["stopping_condition"]
            )
        )
    import aws_sdk_braket.types.instance_config

    out["instanceConfig"] = aws_sdk_braket.types.instance_config.serialize_json(
        value["instance_config"]
    )
    if "hyper_parameters" in value:
        import aws_sdk_braket.types.hyper_parameters

        out["hyperParameters"] = aws_sdk_braket.types.hyper_parameters.serialize_json(
            value["hyper_parameters"]
        )
    import aws_sdk_braket.types.device_config

    out["deviceConfig"] = aws_sdk_braket.types.device_config.serialize_json(
        value["device_config"]
    )
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    if "associations" in value:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.serialize_json(
            value["associations"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobRequest:
    out: CreateJobRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateJobRequest.client_token required")
    if "algorithmSpecification" in data:
        import aws_sdk_braket.types.algorithm_specification

        out["algorithm_specification"] = (
            aws_sdk_braket.types.algorithm_specification.deserialize_json(
                data["algorithmSpecification"]
            )
        )
    else:
        raise DeserializationError("CreateJobRequest.algorithm_specification required")
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
        raise DeserializationError("CreateJobRequest.output_data_config required")
    if "checkpointConfig" in data:
        import aws_sdk_braket.types.job_checkpoint_config

        out["checkpoint_config"] = (
            aws_sdk_braket.types.job_checkpoint_config.deserialize_json(
                data["checkpointConfig"]
            )
        )
    if "jobName" in data:
        out["job_name"] = data["jobName"]
    else:
        raise DeserializationError("CreateJobRequest.job_name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateJobRequest.role_arn required")
    if "stoppingCondition" in data:
        import aws_sdk_braket.types.job_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_braket.types.job_stopping_condition.deserialize_json(
                data["stoppingCondition"]
            )
        )
    if "instanceConfig" in data:
        import aws_sdk_braket.types.instance_config

        out["instance_config"] = aws_sdk_braket.types.instance_config.deserialize_json(
            data["instanceConfig"]
        )
    else:
        raise DeserializationError("CreateJobRequest.instance_config required")
    if "hyperParameters" in data:
        import aws_sdk_braket.types.hyper_parameters

        out["hyper_parameters"] = (
            aws_sdk_braket.types.hyper_parameters.deserialize_json(
                data["hyperParameters"]
            )
        )
    if "deviceConfig" in data:
        import aws_sdk_braket.types.device_config

        out["device_config"] = aws_sdk_braket.types.device_config.deserialize_json(
            data["deviceConfig"]
        )
    else:
        raise DeserializationError("CreateJobRequest.device_config required")
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    if "associations" in data:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.deserialize_json(
            data["associations"]
        )
    return out
