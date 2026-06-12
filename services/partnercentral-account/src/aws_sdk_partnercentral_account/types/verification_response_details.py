"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationResponseDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_account.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.business_verification_response
    import aws_sdk_partnercentral_account.types.registrant_verification_response


class _VerificationResponseDetails_BusinessVerificationResponse(TypedDict):
    BusinessVerificationResponse: "aws_sdk_partnercentral_account.types.business_verification_response.BusinessVerificationResponse"


class _VerificationResponseDetails_RegistrantVerificationResponse(TypedDict):
    RegistrantVerificationResponse: "aws_sdk_partnercentral_account.types.registrant_verification_response.RegistrantVerificationResponse"


VerificationResponseDetails: TypeAlias = (
    _VerificationResponseDetails_BusinessVerificationResponse
    | _VerificationResponseDetails_RegistrantVerificationResponse
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationResponseDetails) -> dict:
    if "BusinessVerificationResponse" in value:
        import aws_sdk_partnercentral_account.types.business_verification_response

        return {
            "BusinessVerificationResponse": aws_sdk_partnercentral_account.types.business_verification_response.serialize_aws_json_1_0(
                value["BusinessVerificationResponse"]
            )
        }
    elif "RegistrantVerificationResponse" in value:
        import aws_sdk_partnercentral_account.types.registrant_verification_response

        return {
            "RegistrantVerificationResponse": aws_sdk_partnercentral_account.types.registrant_verification_response.serialize_aws_json_1_0(
                value["RegistrantVerificationResponse"]
            )
        }
    else:
        raise SerializationError("VerificationResponseDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> VerificationResponseDetails:
    if "BusinessVerificationResponse" in data:
        import aws_sdk_partnercentral_account.types.business_verification_response

        return {
            "BusinessVerificationResponse": aws_sdk_partnercentral_account.types.business_verification_response.deserialize_aws_json_1_0(
                data["BusinessVerificationResponse"]
            )
        }
    elif "RegistrantVerificationResponse" in data:
        import aws_sdk_partnercentral_account.types.registrant_verification_response

        return {
            "RegistrantVerificationResponse": aws_sdk_partnercentral_account.types.registrant_verification_response.deserialize_aws_json_1_0(
                data["RegistrantVerificationResponse"]
            )
        }
    else:
        raise DeserializationError(
            "VerificationResponseDetails: no recognized variant key"
        )
