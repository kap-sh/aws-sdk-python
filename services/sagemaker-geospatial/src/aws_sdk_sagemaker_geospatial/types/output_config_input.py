"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#OutputConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.export_s3_data_input


class OutputConfigInput(TypedDict):
    s3_data: "aws_sdk_sagemaker_geospatial.types.export_s3_data_input.ExportS3DataInput"
    """<p>Path to Amazon S3 storage location for the output configuration file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfigInput) -> dict:
    out: dict = {}
    import aws_sdk_sagemaker_geospatial.types.export_s3_data_input

    out["S3Data"] = (
        aws_sdk_sagemaker_geospatial.types.export_s3_data_input.serialize_json(
            value["s3_data"]
        )
    )
    return out


def deserialize_json(data: dict) -> OutputConfigInput:
    out: OutputConfigInput = {}  # type: ignore[typeddict-item]
    if "S3Data" in data:
        import aws_sdk_sagemaker_geospatial.types.export_s3_data_input

        out["s3_data"] = (
            aws_sdk_sagemaker_geospatial.types.export_s3_data_input.deserialize_json(
                data["S3Data"]
            )
        )
    else:
        raise DeserializationError("OutputConfigInput.s3_data required")
    return out
