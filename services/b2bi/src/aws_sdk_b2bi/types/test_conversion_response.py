"""Generated from Smithy shape ``com.amazonaws.b2bi#TestConversionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.validation_messages


class TestConversionResponse(TypedDict):
    converted_file_content: "str"
    """<p>Returns the converted file content.</p>"""
    validation_messages: NotRequired[
        "aws_sdk_b2bi.types.validation_messages.ValidationMessages"
    ]
    """<p>Returns an array of validation messages that Amazon Web Services B2B Data Interchange generates during the conversion process. These messages include both standard EDI validation results and custom validation messages when custom validation rules are configured. Custom validation messages provide detailed feedback on element length constraints, code list validations, and element requirement checks applied during the outbound EDI generation process.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestConversionResponse) -> dict:
    out: dict = {}
    out["convertedFileContent"] = value["converted_file_content"]
    if "validation_messages" in value:
        import aws_sdk_b2bi.types.validation_messages

        out["validationMessages"] = (
            aws_sdk_b2bi.types.validation_messages.serialize_aws_json_1_0(
                value["validation_messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestConversionResponse:
    out: TestConversionResponse = {}  # type: ignore[typeddict-item]
    if "convertedFileContent" in data:
        out["converted_file_content"] = data["convertedFileContent"]
    else:
        raise DeserializationError(
            "TestConversionResponse.converted_file_content required"
        )
    if "validationMessages" in data:
        import aws_sdk_b2bi.types.validation_messages

        out["validation_messages"] = (
            aws_sdk_b2bi.types.validation_messages.deserialize_aws_json_1_0(
                data["validationMessages"]
            )
        )
    return out
