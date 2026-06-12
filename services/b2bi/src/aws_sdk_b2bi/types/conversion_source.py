"""Generated from Smithy shape ``com.amazonaws.b2bi#ConversionSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.conversion_source_format
    import aws_sdk_b2bi.types.input_file_source


class ConversionSource(TypedDict):
    file_format: "aws_sdk_b2bi.types.conversion_source_format.ConversionSourceFormat"
    """<p>The format for the input file: either JSON or XML.</p>"""
    input_file: "aws_sdk_b2bi.types.input_file_source.InputFileSource"
    """File to be converted"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConversionSource) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.conversion_source_format

    out["fileFormat"] = (
        aws_sdk_b2bi.types.conversion_source_format.serialize_aws_json_1_0(
            value["file_format"]
        )
    )
    import aws_sdk_b2bi.types.input_file_source

    out["inputFile"] = aws_sdk_b2bi.types.input_file_source.serialize_aws_json_1_0(
        value["input_file"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConversionSource:
    out: ConversionSource = {}  # type: ignore[typeddict-item]
    if "fileFormat" in data:
        import aws_sdk_b2bi.types.conversion_source_format

        out["file_format"] = (
            aws_sdk_b2bi.types.conversion_source_format.deserialize_aws_json_1_0(
                data["fileFormat"]
            )
        )
    else:
        raise DeserializationError("ConversionSource.file_format required")
    if "inputFile" in data:
        import aws_sdk_b2bi.types.input_file_source

        out["input_file"] = (
            aws_sdk_b2bi.types.input_file_source.deserialize_aws_json_1_0(
                data["inputFile"]
            )
        )
    else:
        raise DeserializationError("ConversionSource.input_file required")
    return out
