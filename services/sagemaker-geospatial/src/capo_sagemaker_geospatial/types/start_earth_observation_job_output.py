"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#StartEarthObservationJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.earth_observation_job_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.input_config_output
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags


class StartEarthObservationJobOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the Earth Observation job.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the session, in seconds.</p>"""
    status: "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
    """<p>The status of the Earth Observation job.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: NotRequired[
        "capo_sagemaker_geospatial.types.input_config_output.InputConfigOutput"
    ]
    """<p>Input configuration information for the Earth Observation job.</p>"""
    job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput"
    """<p>An object containing information about the job configuration.</p>"""
    execution_role_arn: (
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartEarthObservationJobOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    import capo_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        capo_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "input_config" in value:
        import capo_sagemaker_geospatial.types.input_config_output

        out["InputConfig"] = (
            capo_sagemaker_geospatial.types.input_config_output.serialize_json(
                value["input_config"]
            )
        )
    import capo_sagemaker_geospatial.types.job_config_input

    out["JobConfig"] = capo_sagemaker_geospatial.types.job_config_input.serialize_json(
        value["job_config"]
    )
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartEarthObservationJobOutput:
    out: StartEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.name required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.arn required")
    if "CreationTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.creation_time required"
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.duration_in_seconds required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("StartEarthObservationJobOutput.status required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "InputConfig" in data:
        import capo_sagemaker_geospatial.types.input_config_output

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_output.deserialize_json(
                data["InputConfig"]
            )
        )
    if "JobConfig" in data:
        import capo_sagemaker_geospatial.types.job_config_input

        out["job_config"] = (
            capo_sagemaker_geospatial.types.job_config_input.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        raise DeserializationError("StartEarthObservationJobOutput.job_config required")
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "StartEarthObservationJobOutput.execution_role_arn required"
        )
    if "Tags" in data:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
