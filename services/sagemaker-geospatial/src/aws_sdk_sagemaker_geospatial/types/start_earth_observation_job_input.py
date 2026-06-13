"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartEarthObservationJobInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.execution_role_arn
    import aws_sdk_sagemaker_geospatial.types.input_config_input
    import aws_sdk_sagemaker_geospatial.types.job_config_input
    import aws_sdk_sagemaker_geospatial.types.kms_key
    import aws_sdk_sagemaker_geospatial.types.tags


class StartEarthObservationJobInput(TypedDict):
    name: "str"
    """<p>The name of the Earth Observation job.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique token that guarantees that the call to this API is idempotent.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: (
        "aws_sdk_sagemaker_geospatial.types.input_config_input.InputConfigInput"
    )
    """<p>Input configuration information for the Earth Observation job.</p>"""
    job_config: "aws_sdk_sagemaker_geospatial.types.job_config_input.JobConfigInput"
    """<p>An object containing information about the job configuration.</p>"""
    execution_role_arn: (
        "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    tags: NotRequired["aws_sdk_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartEarthObservationJobInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    import aws_sdk_sagemaker_geospatial.types.input_config_input

    out["InputConfig"] = (
        aws_sdk_sagemaker_geospatial.types.input_config_input.serialize_json(
            value["input_config"]
        )
    )
    import aws_sdk_sagemaker_geospatial.types.job_config_input

    out["JobConfig"] = (
        aws_sdk_sagemaker_geospatial.types.job_config_input.serialize_json(
            value["job_config"]
        )
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "tags" in value:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartEarthObservationJobInput:
    out: StartEarthObservationJobInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartEarthObservationJobInput.name required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "InputConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.input_config_input

        out["input_config"] = (
            aws_sdk_sagemaker_geospatial.types.input_config_input.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartEarthObservationJobInput.input_config required"
        )
    if "JobConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.job_config_input

        out["job_config"] = (
            aws_sdk_sagemaker_geospatial.types.job_config_input.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        raise DeserializationError("StartEarthObservationJobInput.job_config required")
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "StartEarthObservationJobInput.execution_role_arn required"
        )
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
