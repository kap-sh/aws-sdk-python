"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetEarthObservationJobOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_sagemaker_geospatial.types.earth_observation_job_error_details
    import capo_sagemaker_geospatial.types.earth_observation_job_export_status
    import capo_sagemaker_geospatial.types.earth_observation_job_output_bands
    import capo_sagemaker_geospatial.types.earth_observation_job_status
    import capo_sagemaker_geospatial.types.execution_role_arn
    import capo_sagemaker_geospatial.types.export_error_details
    import capo_sagemaker_geospatial.types.input_config_output
    import capo_sagemaker_geospatial.types.job_config_input
    import capo_sagemaker_geospatial.types.kms_key
    import capo_sagemaker_geospatial.types.tags


class GetEarthObservationJobOutput(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Earth Observation job.</p>"""
    name: "str"
    """<p>The name of the Earth Observation job.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time of the initiated Earth Observation job.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of Earth Observation job, in seconds.</p>"""
    status: "capo_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
    """<p>The status of a previously initiated Earth Observation job.</p>"""
    kms_key_id: NotRequired["capo_sagemaker_geospatial.types.kms_key.KmsKey"]
    """<p>The Key Management Service key ID for server-side encryption.</p>"""
    input_config: (
        "capo_sagemaker_geospatial.types.input_config_output.InputConfigOutput"
    )
    """<p>Input data for the Earth Observation job.</p>"""
    job_config: "capo_sagemaker_geospatial.types.job_config_input.JobConfigInput"
    """<p>An object containing information about the job configuration.</p>"""
    output_bands: NotRequired[
        "capo_sagemaker_geospatial.types.earth_observation_job_output_bands.EarthObservationJobOutputBands"
    ]
    """<p>Bands available in the output of an operation.</p>"""
    execution_role_arn: NotRequired[
        "capo_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    error_details: NotRequired[
        "capo_sagemaker_geospatial.types.earth_observation_job_error_details.EarthObservationJobErrorDetails"
    ]
    """<p>Details about the errors generated during the Earth Observation job.</p>"""
    export_status: NotRequired[
        "capo_sagemaker_geospatial.types.earth_observation_job_export_status.EarthObservationJobExportStatus"
    ]
    """<p>The status of the Earth Observation job.</p>"""
    export_error_details: NotRequired[
        "capo_sagemaker_geospatial.types.export_error_details.ExportErrorDetails"
    ]
    """<p>Details about the errors generated during ExportEarthObservationJob.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEarthObservationJobOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
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
    if "output_bands" in value:
        import capo_sagemaker_geospatial.types.earth_observation_job_output_bands

        out["OutputBands"] = (
            capo_sagemaker_geospatial.types.earth_observation_job_output_bands.serialize_json(
                value["output_bands"]
            )
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "error_details" in value:
        import capo_sagemaker_geospatial.types.earth_observation_job_error_details

        out["ErrorDetails"] = (
            capo_sagemaker_geospatial.types.earth_observation_job_error_details.serialize_json(
                value["error_details"]
            )
        )
    if "export_status" in value:
        out["ExportStatus"] = value["export_status"]
    if "export_error_details" in value:
        import capo_sagemaker_geospatial.types.export_error_details

        out["ExportErrorDetails"] = (
            capo_sagemaker_geospatial.types.export_error_details.serialize_json(
                value["export_error_details"]
            )
        )
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetEarthObservationJobOutput:
    out: GetEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetEarthObservationJobOutput.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetEarthObservationJobOutput.name required")
    if "CreationTime" in data:
        import capo_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            capo_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetEarthObservationJobOutput.creation_time required"
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "GetEarthObservationJobOutput.duration_in_seconds required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("GetEarthObservationJobOutput.status required")
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "InputConfig" in data:
        import capo_sagemaker_geospatial.types.input_config_output

        out["input_config"] = (
            capo_sagemaker_geospatial.types.input_config_output.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError("GetEarthObservationJobOutput.input_config required")
    if "JobConfig" in data:
        import capo_sagemaker_geospatial.types.job_config_input

        out["job_config"] = (
            capo_sagemaker_geospatial.types.job_config_input.deserialize_json(
                data["JobConfig"]
            )
        )
    else:
        raise DeserializationError("GetEarthObservationJobOutput.job_config required")
    if "OutputBands" in data:
        import capo_sagemaker_geospatial.types.earth_observation_job_output_bands

        out["output_bands"] = (
            capo_sagemaker_geospatial.types.earth_observation_job_output_bands.deserialize_json(
                data["OutputBands"]
            )
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "ErrorDetails" in data:
        import capo_sagemaker_geospatial.types.earth_observation_job_error_details

        out["error_details"] = (
            capo_sagemaker_geospatial.types.earth_observation_job_error_details.deserialize_json(
                data["ErrorDetails"]
            )
        )
    if "ExportStatus" in data:
        out["export_status"] = data["ExportStatus"]
    if "ExportErrorDetails" in data:
        import capo_sagemaker_geospatial.types.export_error_details

        out["export_error_details"] = (
            capo_sagemaker_geospatial.types.export_error_details.deserialize_json(
                data["ExportErrorDetails"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
