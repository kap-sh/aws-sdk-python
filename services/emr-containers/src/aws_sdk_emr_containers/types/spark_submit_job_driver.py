"""Generated from Smithy shape ``com.amazonaws.emrcontainers#SparkSubmitJobDriver``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.entry_point_arguments
    import aws_sdk_emr_containers.types.entry_point_path
    import aws_sdk_emr_containers.types.spark_submit_parameters


class SparkSubmitJobDriver(TypedDict):
    entry_point: "aws_sdk_emr_containers.types.entry_point_path.EntryPointPath"
    """<p>The entry point of job application.</p>"""
    entry_point_arguments: NotRequired[
        "aws_sdk_emr_containers.types.entry_point_arguments.EntryPointArguments"
    ]
    """<p>The arguments for job application.</p>"""
    spark_submit_parameters: NotRequired[
        "aws_sdk_emr_containers.types.spark_submit_parameters.SparkSubmitParameters"
    ]
    """<p>The Spark submit parameters that are used for job runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkSubmitJobDriver) -> dict:
    out: dict = {}
    out["entryPoint"] = value["entry_point"]
    if "entry_point_arguments" in value:
        import aws_sdk_emr_containers.types.entry_point_arguments

        out["entryPointArguments"] = (
            aws_sdk_emr_containers.types.entry_point_arguments.serialize_json(
                value["entry_point_arguments"]
            )
        )
    if "spark_submit_parameters" in value:
        out["sparkSubmitParameters"] = value["spark_submit_parameters"]
    return out


def deserialize_json(data: dict) -> SparkSubmitJobDriver:
    out: SparkSubmitJobDriver = {}  # type: ignore[typeddict-item]
    if "entryPoint" in data:
        out["entry_point"] = data["entryPoint"]
    else:
        raise DeserializationError("SparkSubmitJobDriver.entry_point required")
    if "entryPointArguments" in data:
        import aws_sdk_emr_containers.types.entry_point_arguments

        out["entry_point_arguments"] = (
            aws_sdk_emr_containers.types.entry_point_arguments.deserialize_json(
                data["entryPointArguments"]
            )
        )
    if "sparkSubmitParameters" in data:
        out["spark_submit_parameters"] = data["sparkSubmitParameters"]
    return out
