"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ValidationExceptionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.validation_exception_error_code


class ValidationExceptionError(TypedDict, closed=True):
    field_name: NotRequired["str"]
    """<p>Specifies the field name with the invalid value.</p>"""
    message: "str"
    """<p>Specifies the detailed error message for the invalid field value.</p>"""
    code: "aws_sdk_partnercentral_selling.types.validation_exception_error_code.ValidationExceptionErrorCode"
    """<p>Specifies the error code for the invalid field value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationExceptionError) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_selling.types.validation_exception_error_code

    out["Code"] = (
        aws_sdk_partnercentral_selling.types.validation_exception_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationExceptionError:
    out: ValidationExceptionError = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ValidationExceptionError.message required")
    if "Code" in data:
        import aws_sdk_partnercentral_selling.types.validation_exception_error_code

        out["code"] = (
            aws_sdk_partnercentral_selling.types.validation_exception_error_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("ValidationExceptionError.code required")
    return out
