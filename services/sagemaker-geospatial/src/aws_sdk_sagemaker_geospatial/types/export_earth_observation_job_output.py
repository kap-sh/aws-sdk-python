"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ExportEarthObservationJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn
    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_export_status
    import aws_sdk_sagemaker_geospatial.types.execution_role_arn
    import aws_sdk_sagemaker_geospatial.types.output_config_input


class ExportEarthObservationJobOutput(TypedDict):
    arn: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    """<p>The output Amazon Resource Name (ARN) of the Earth Observation job being exported.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    export_status: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_export_status.EarthObservationJobExportStatus"
    """<p>The status of the results of the Earth Observation job being exported.</p>"""
    execution_role_arn: (
        "aws_sdk_sagemaker_geospatial.types.execution_role_arn.ExecutionRoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the job.</p>"""
    output_config: (
        "aws_sdk_sagemaker_geospatial.types.output_config_input.OutputConfigInput"
    )
    """<p>An object containing information about the output file.</p>"""
    export_source_images: NotRequired["bool"]
    """<p>The source images provided to the Earth Observation job being exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportEarthObservationJobOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["ExportStatus"] = value["export_status"]
    out["ExecutionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_sagemaker_geospatial.types.output_config_input

    out["OutputConfig"] = (
        aws_sdk_sagemaker_geospatial.types.output_config_input.serialize_json(
            value["output_config"]
        )
    )
    if "export_source_images" in value:
        out["ExportSourceImages"] = value["export_source_images"]
    return out


def deserialize_json(data: dict) -> ExportEarthObservationJobOutput:
    out: ExportEarthObservationJobOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ExportEarthObservationJobOutput.arn required")
    if "CreationTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ExportEarthObservationJobOutput.creation_time required"
        )
    if "ExportStatus" in data:
        out["export_status"] = data["ExportStatus"]
    else:
        raise DeserializationError(
            "ExportEarthObservationJobOutput.export_status required"
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    else:
        raise DeserializationError(
            "ExportEarthObservationJobOutput.execution_role_arn required"
        )
    if "OutputConfig" in data:
        import aws_sdk_sagemaker_geospatial.types.output_config_input

        out["output_config"] = (
            aws_sdk_sagemaker_geospatial.types.output_config_input.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "ExportEarthObservationJobOutput.output_config required"
        )
    if "ExportSourceImages" in data:
        out["export_source_images"] = data["ExportSourceImages"]
    return out
