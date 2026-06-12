"""Generated from Smithy shape ``com.amazonaws.b2bi#OutputConversion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.advanced_options
    import aws_sdk_b2bi.types.format_options
    import aws_sdk_b2bi.types.to_format


class OutputConversion(TypedDict):
    to_format: "aws_sdk_b2bi.types.to_format.ToFormat"
    """<p>The format for the output from an outbound transformer: only X12 is currently supported.</p>"""
    format_options: NotRequired["aws_sdk_b2bi.types.format_options.FormatOptions"]
    """<p>A structure that contains the X12 transaction set and version for the transformer output.</p>"""
    advanced_options: NotRequired["aws_sdk_b2bi.types.advanced_options.AdvancedOptions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputConversion) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.to_format

    out["toFormat"] = aws_sdk_b2bi.types.to_format.serialize_aws_json_1_0(
        value["to_format"]
    )
    if "format_options" in value:
        import aws_sdk_b2bi.types.format_options

        out["formatOptions"] = aws_sdk_b2bi.types.format_options.serialize_aws_json_1_0(
            value["format_options"]
        )
    if "advanced_options" in value:
        import aws_sdk_b2bi.types.advanced_options

        out["advancedOptions"] = (
            aws_sdk_b2bi.types.advanced_options.serialize_aws_json_1_0(
                value["advanced_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OutputConversion:
    out: OutputConversion = {}  # type: ignore[typeddict-item]
    if "toFormat" in data:
        import aws_sdk_b2bi.types.to_format

        out["to_format"] = aws_sdk_b2bi.types.to_format.deserialize_aws_json_1_0(
            data["toFormat"]
        )
    else:
        raise DeserializationError("OutputConversion.to_format required")
    if "formatOptions" in data:
        import aws_sdk_b2bi.types.format_options

        out["format_options"] = (
            aws_sdk_b2bi.types.format_options.deserialize_aws_json_1_0(
                data["formatOptions"]
            )
        )
    if "advancedOptions" in data:
        import aws_sdk_b2bi.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_b2bi.types.advanced_options.deserialize_aws_json_1_0(
                data["advancedOptions"]
            )
        )
    return out
