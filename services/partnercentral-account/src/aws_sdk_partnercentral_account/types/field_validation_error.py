"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#FieldValidationError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.field_validation_code


class FieldValidationError(TypedDict):
    name: "str"
    """<p>The name of the field that failed validation.</p>"""
    message: "str"
    """<p>A description of the field validation error.</p>"""
    code: (
        "aws_sdk_partnercentral_account.types.field_validation_code.FieldValidationCode"
    )
    """<p>A code identifying the specific field validation error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FieldValidationError) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.field_validation_code

    out["Code"] = (
        aws_sdk_partnercentral_account.types.field_validation_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> FieldValidationError:
    out: FieldValidationError = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FieldValidationError.name required")
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("FieldValidationError.message required")
    if "Code" in data:
        import aws_sdk_partnercentral_account.types.field_validation_code

        out["code"] = (
            aws_sdk_partnercentral_account.types.field_validation_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("FieldValidationError.code required")
    return out
