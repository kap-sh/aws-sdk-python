"""Generated from Smithy shape ``com.amazonaws.b2bi#TestParsingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.parsed_split_file_contents_list
    import aws_sdk_b2bi.types.validation_messages


class TestParsingResponse(TypedDict):
    parsed_file_content: "str"
    """<p>Returns the contents of the input file being tested, parsed according to the specified EDI (electronic data interchange) type.</p>"""
    parsed_split_file_contents: NotRequired[
        "aws_sdk_b2bi.types.parsed_split_file_contents_list.ParsedSplitFileContentsList"
    ]
    """<p>Returns an array of parsed file contents when the input file is split according to the specified split options. Each element in the array represents a separate split file's parsed content.</p>"""
    validation_messages: NotRequired[
        "aws_sdk_b2bi.types.validation_messages.ValidationMessages"
    ]
    """<p>Returns an array of validation messages generated during EDI validation. These messages provide detailed information about validation errors, warnings, or confirmations based on the configured X12 validation rules such as element length constraints, code list validations, and element requirement checks. This field is populated when the <code>TestParsing</code> API validates EDI documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestParsingResponse) -> dict:
    out: dict = {}
    out["parsedFileContent"] = value["parsed_file_content"]
    if "parsed_split_file_contents" in value:
        import aws_sdk_b2bi.types.parsed_split_file_contents_list

        out["parsedSplitFileContents"] = (
            aws_sdk_b2bi.types.parsed_split_file_contents_list.serialize_aws_json_1_0(
                value["parsed_split_file_contents"]
            )
        )
    if "validation_messages" in value:
        import aws_sdk_b2bi.types.validation_messages

        out["validationMessages"] = (
            aws_sdk_b2bi.types.validation_messages.serialize_aws_json_1_0(
                value["validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestParsingResponse:
    out: TestParsingResponse = {}  # type: ignore[typeddict-item]
    if "parsedFileContent" in data:
        out["parsed_file_content"] = data["parsedFileContent"]
    else:
        raise DeserializationError("TestParsingResponse.parsed_file_content required")
    if "parsedSplitFileContents" in data:
        import aws_sdk_b2bi.types.parsed_split_file_contents_list

        out["parsed_split_file_contents"] = (
            aws_sdk_b2bi.types.parsed_split_file_contents_list.deserialize_aws_json_1_0(
                data["parsedSplitFileContents"]
            )
        )
    if "validationMessages" in data:
        import aws_sdk_b2bi.types.validation_messages

        out["validation_messages"] = (
            aws_sdk_b2bi.types.validation_messages.deserialize_aws_json_1_0(
                data["validationMessages"]
            )
        )
    return out
