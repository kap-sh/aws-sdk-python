"""Generated from Smithy shape ``com.amazonaws.mgn#SourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.source_environment
    import aws_sdk_mgn.types.source_s3_configuration


class SourceConfiguration(TypedDict, closed=True):
    source_environment: "aws_sdk_mgn.types.source_environment.SourceEnvironment"
    """<p>The source environment type.</p>"""
    source_s3_configuration: (
        "aws_sdk_mgn.types.source_s3_configuration.SourceS3Configuration"
    )
    """<p>The S3 configuration for the source data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    out: dict = {}
    out["sourceEnvironment"] = value["source_environment"]
    import aws_sdk_mgn.types.source_s3_configuration

    out["sourceS3Configuration"] = (
        aws_sdk_mgn.types.source_s3_configuration.serialize_json(
            value["source_s3_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceEnvironment" in data:
        out["source_environment"] = data["sourceEnvironment"]
    else:
        raise DeserializationError("SourceConfiguration.source_environment required")
    if "sourceS3Configuration" in data:
        import aws_sdk_mgn.types.source_s3_configuration

        out["source_s3_configuration"] = (
            aws_sdk_mgn.types.source_s3_configuration.deserialize_json(
                data["sourceS3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "SourceConfiguration.source_s3_configuration required"
        )
    return out
