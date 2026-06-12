"""Generated from Smithy shape ``com.amazonaws.emrserverless#SparkSubmit``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_emr_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.entry_point_arguments
    import aws_sdk_emr_serverless.types.entry_point_path
    import aws_sdk_emr_serverless.types.spark_submit_parameters


class SparkSubmit(TypedDict):
    entry_point: "aws_sdk_emr_serverless.types.entry_point_path.EntryPointPath"
    """<p>The entry point for the Spark submit job run.</p>"""
    entry_point_arguments: NotRequired[
        "aws_sdk_emr_serverless.types.entry_point_arguments.EntryPointArguments"
    ]
    """<p>The arguments for the Spark submit job run.</p>"""
    spark_submit_parameters: NotRequired[
        "aws_sdk_emr_serverless.types.spark_submit_parameters.SparkSubmitParameters"
    ]
    """<p>The parameters for the Spark submit job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparkSubmit) -> dict:
    out: dict = {}
    out["entryPoint"] = value["entry_point"]
    if "entry_point_arguments" in value:
        import aws_sdk_emr_serverless.types.entry_point_arguments

        out["entryPointArguments"] = (
            aws_sdk_emr_serverless.types.entry_point_arguments.serialize_json(
                value["entry_point_arguments"]
            )
        )
    if "spark_submit_parameters" in value:
        out["sparkSubmitParameters"] = value["spark_submit_parameters"]
    return out


def deserialize_json(data: dict) -> SparkSubmit:
    out: SparkSubmit = {}  # type: ignore[typeddict-item]
    if "entryPoint" in data:
        out["entry_point"] = data["entryPoint"]
    else:
        raise DeserializationError("SparkSubmit.entry_point required")
    if "entryPointArguments" in data:
        import aws_sdk_emr_serverless.types.entry_point_arguments

        out["entry_point_arguments"] = (
            aws_sdk_emr_serverless.types.entry_point_arguments.deserialize_json(
                data["entryPointArguments"]
            )
        )
    if "sparkSubmitParameters" in data:
        out["spark_submit_parameters"] = data["sparkSubmitParameters"]
    return out
