"""Generated from Smithy shape ``com.amazonaws.glue#S3DeltaSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.enclosed_in_string_properties
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.s3_direct_source_additional_options


class S3DeltaSource(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Delta Lake source.</p>"""
    paths: "aws_sdk_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>A list of the Amazon S3 paths to read from.</p>"""
    additional_delta_options: NotRequired[
        "aws_sdk_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""
    additional_options: NotRequired[
        "aws_sdk_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Specifies additional options for the connector.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the Delta Lake source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DeltaSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.enclosed_in_string_properties

    out["Paths"] = (
        aws_sdk_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
            value["paths"]
        )
    )
    if "additional_delta_options" in value:
        import aws_sdk_glue.types.additional_options

        out["AdditionalDeltaOptions"] = (
            aws_sdk_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_delta_options"]
            )
        )
    if "additional_options" in value:
        import aws_sdk_glue.types.s3_direct_source_additional_options

        out["AdditionalOptions"] = (
            aws_sdk_glue.types.s3_direct_source_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DeltaSource:
    out: S3DeltaSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("S3DeltaSource.name required")
    if "Paths" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties

        out["paths"] = (
            aws_sdk_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        raise DeserializationError("S3DeltaSource.paths required")
    if "AdditionalDeltaOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_delta_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalDeltaOptions"]
            )
        )
    if "AdditionalOptions" in data:
        import aws_sdk_glue.types.s3_direct_source_additional_options

        out["additional_options"] = (
            aws_sdk_glue.types.s3_direct_source_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
