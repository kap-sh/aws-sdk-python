"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#VerificationDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_account.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.business_verification_details
    import aws_sdk_partnercentral_account.types.registrant_verification_details


class _VerificationDetails_BusinessVerificationDetails(TypedDict):
    BusinessVerificationDetails: "aws_sdk_partnercentral_account.types.business_verification_details.BusinessVerificationDetails"


class _VerificationDetails_RegistrantVerificationDetails(TypedDict):
    RegistrantVerificationDetails: "aws_sdk_partnercentral_account.types.registrant_verification_details.RegistrantVerificationDetails"


VerificationDetails: TypeAlias = (
    _VerificationDetails_BusinessVerificationDetails
    | _VerificationDetails_RegistrantVerificationDetails
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VerificationDetails) -> dict:
    if "BusinessVerificationDetails" in value:
        import aws_sdk_partnercentral_account.types.business_verification_details

        return {
            "BusinessVerificationDetails": aws_sdk_partnercentral_account.types.business_verification_details.serialize_aws_json_1_0(
                value["BusinessVerificationDetails"]
            )
        }
    elif "RegistrantVerificationDetails" in value:
        import aws_sdk_partnercentral_account.types.registrant_verification_details

        return {
            "RegistrantVerificationDetails": aws_sdk_partnercentral_account.types.registrant_verification_details.serialize_aws_json_1_0(
                value["RegistrantVerificationDetails"]
            )
        }
    else:
        raise SerializationError("VerificationDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> VerificationDetails:
    if "BusinessVerificationDetails" in data:
        import aws_sdk_partnercentral_account.types.business_verification_details

        return {
            "BusinessVerificationDetails": aws_sdk_partnercentral_account.types.business_verification_details.deserialize_aws_json_1_0(
                data["BusinessVerificationDetails"]
            )
        }
    elif "RegistrantVerificationDetails" in data:
        import aws_sdk_partnercentral_account.types.registrant_verification_details

        return {
            "RegistrantVerificationDetails": aws_sdk_partnercentral_account.types.registrant_verification_details.deserialize_aws_json_1_0(
                data["RegistrantVerificationDetails"]
            )
        }
    else:
        raise DeserializationError("VerificationDetails: no recognized variant key")
