"""Generated from Smithy shape ``com.amazonaws.b2bi#TestParsingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.advanced_options
    import aws_sdk_b2bi.types.edi_type
    import aws_sdk_b2bi.types.file_format
    import aws_sdk_b2bi.types.s3_location


class TestParsingRequest(TypedDict):
    input_file: "aws_sdk_b2bi.types.s3_location.S3Location"
    """<p>Specifies an <code>S3Location</code> object, which contains the Amazon S3 bucket and prefix for the location of the input file.</p>"""
    file_format: "aws_sdk_b2bi.types.file_format.FileFormat"
    """<p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""
    edi_type: "aws_sdk_b2bi.types.edi_type.EdiType"
    """<p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>"""
    advanced_options: NotRequired["aws_sdk_b2bi.types.advanced_options.AdvancedOptions"]
    """<p>Specifies advanced options for parsing the input EDI file. These options allow for more granular control over the parsing process, including split options for X12 files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestParsingRequest) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.s3_location

    out["inputFile"] = aws_sdk_b2bi.types.s3_location.serialize_aws_json_1_0(
        value["input_file"]
    )
    import aws_sdk_b2bi.types.file_format

    out["fileFormat"] = aws_sdk_b2bi.types.file_format.serialize_aws_json_1_0(
        value["file_format"]
    )
    import aws_sdk_b2bi.types.edi_type

    out["ediType"] = aws_sdk_b2bi.types.edi_type.serialize_aws_json_1_0(
        value["edi_type"]
    )
    if "advanced_options" in value:
        import aws_sdk_b2bi.types.advanced_options

        out["advancedOptions"] = (
            aws_sdk_b2bi.types.advanced_options.serialize_aws_json_1_0(
                value["advanced_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestParsingRequest:
    out: TestParsingRequest = {}  # type: ignore[typeddict-item]
    if "inputFile" in data:
        import aws_sdk_b2bi.types.s3_location

        out["input_file"] = aws_sdk_b2bi.types.s3_location.deserialize_aws_json_1_0(
            data["inputFile"]
        )
    else:
        raise DeserializationError("TestParsingRequest.input_file required")
    if "fileFormat" in data:
        import aws_sdk_b2bi.types.file_format

        out["file_format"] = aws_sdk_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("TestParsingRequest.file_format required")
    if "ediType" in data:
        import aws_sdk_b2bi.types.edi_type

        out["edi_type"] = aws_sdk_b2bi.types.edi_type.deserialize_aws_json_1_0(
            data["ediType"]
        )
    else:
        raise DeserializationError("TestParsingRequest.edi_type required")
    if "advancedOptions" in data:
        import aws_sdk_b2bi.types.advanced_options

        out["advanced_options"] = (
            aws_sdk_b2bi.types.advanced_options.deserialize_aws_json_1_0(
                data["advancedOptions"]
            )
        )
    return out
