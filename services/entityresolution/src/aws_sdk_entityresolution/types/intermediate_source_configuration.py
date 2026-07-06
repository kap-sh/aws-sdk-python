"""Generated from Smithy shape ``com.amazonaws.entityresolution#IntermediateSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.s3_path


class IntermediateSourceConfiguration(TypedDict, closed=True):
    intermediate_s3_path: "aws_sdk_entityresolution.types.s3_path.S3Path"
    """<p>The Amazon S3 location (bucket and prefix). For example: <code>s3://provider_bucket/DOC-EXAMPLE-BUCKET</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateSourceConfiguration) -> dict:
    out: dict = {}
    out["intermediateS3Path"] = value["intermediate_s3_path"]
    return out


def deserialize_json(data: dict) -> IntermediateSourceConfiguration:
    out: IntermediateSourceConfiguration = {}  # type: ignore[typeddict-item]
    if "intermediateS3Path" in data:
        out["intermediate_s3_path"] = data["intermediateS3Path"]
    else:
        raise DeserializationError(
            "IntermediateSourceConfiguration.intermediate_s3_path required"
        )
    return out
