"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#S3OutputConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_data_exports.types.compression_option
    import aws_sdk_bcm_data_exports.types.format_option
    import aws_sdk_bcm_data_exports.types.overwrite_option
    import aws_sdk_bcm_data_exports.types.s3_output_type


class S3OutputConfigurations(TypedDict, closed=True):
    output_type: "aws_sdk_bcm_data_exports.types.s3_output_type.S3OutputType"
    """<p>The output type for the data export.</p>"""
    format: "aws_sdk_bcm_data_exports.types.format_option.FormatOption"
    """<p>The file format for the data export.</p>"""
    compression: "aws_sdk_bcm_data_exports.types.compression_option.CompressionOption"
    """<p>The compression type for the data export.</p>"""
    overwrite: "aws_sdk_bcm_data_exports.types.overwrite_option.OverwriteOption"
    """<p>The rule to follow when generating a version of the data export file. You have the choice to overwrite the previous version or to be delivered in addition to the previous versions. Overwriting exports can save on Amazon S3 storage costs. Creating new export versions allows you to track the changes in cost and usage data over time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3OutputConfigurations) -> dict:
    out: dict = {}
    import aws_sdk_bcm_data_exports.types.s3_output_type

    out["OutputType"] = (
        aws_sdk_bcm_data_exports.types.s3_output_type.serialize_aws_json_1_1(
            value["output_type"]
        )
    )
    import aws_sdk_bcm_data_exports.types.format_option

    out["Format"] = aws_sdk_bcm_data_exports.types.format_option.serialize_aws_json_1_1(
        value["format"]
    )
    import aws_sdk_bcm_data_exports.types.compression_option

    out["Compression"] = (
        aws_sdk_bcm_data_exports.types.compression_option.serialize_aws_json_1_1(
            value["compression"]
        )
    )
    import aws_sdk_bcm_data_exports.types.overwrite_option

    out["Overwrite"] = (
        aws_sdk_bcm_data_exports.types.overwrite_option.serialize_aws_json_1_1(
            value["overwrite"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3OutputConfigurations:
    out: S3OutputConfigurations = {}  # type: ignore[typeddict-item]
    if "OutputType" in data:
        import aws_sdk_bcm_data_exports.types.s3_output_type

        out["output_type"] = (
            aws_sdk_bcm_data_exports.types.s3_output_type.deserialize_aws_json_1_1(
                data["OutputType"]
            )
        )
    else:
        raise DeserializationError("S3OutputConfigurations.output_type required")
    if "Format" in data:
        import aws_sdk_bcm_data_exports.types.format_option

        out["format"] = (
            aws_sdk_bcm_data_exports.types.format_option.deserialize_aws_json_1_1(
                data["Format"]
            )
        )
    else:
        raise DeserializationError("S3OutputConfigurations.format required")
    if "Compression" in data:
        import aws_sdk_bcm_data_exports.types.compression_option

        out["compression"] = (
            aws_sdk_bcm_data_exports.types.compression_option.deserialize_aws_json_1_1(
                data["Compression"]
            )
        )
    else:
        raise DeserializationError("S3OutputConfigurations.compression required")
    if "Overwrite" in data:
        import aws_sdk_bcm_data_exports.types.overwrite_option

        out["overwrite"] = (
            aws_sdk_bcm_data_exports.types.overwrite_option.deserialize_aws_json_1_1(
                data["Overwrite"]
            )
        )
    else:
        raise DeserializationError("S3OutputConfigurations.overwrite required")
    return out
