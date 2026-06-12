"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#BusinessValidationError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.business_validation_code


class BusinessValidationError(TypedDict):
    message: "str"
    """<p>A description of the business validation error.</p>"""
    code: "aws_sdk_partnercentral_account.types.business_validation_code.BusinessValidationCode"
    """<p>A code identifying the specific business validation error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessValidationError) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import aws_sdk_partnercentral_account.types.business_validation_code

    out["Code"] = (
        aws_sdk_partnercentral_account.types.business_validation_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessValidationError:
    out: BusinessValidationError = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("BusinessValidationError.message required")
    if "Code" in data:
        import aws_sdk_partnercentral_account.types.business_validation_code

        out["code"] = (
            aws_sdk_partnercentral_account.types.business_validation_code.deserialize_aws_json_1_0(
                data["Code"]
            )
        )
    else:
        raise DeserializationError("BusinessValidationError.code required")
    return out
