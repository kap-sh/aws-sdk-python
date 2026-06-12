"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetVerificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.verification_type


class GetVerificationRequest(TypedDict):
    verification_type: (
        "aws_sdk_partnercentral_account.types.verification_type.VerificationType"
    )
    """<p>The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVerificationRequest) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.verification_type

    out["VerificationType"] = (
        aws_sdk_partnercentral_account.types.verification_type.serialize_aws_json_1_0(
            value["verification_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVerificationRequest:
    out: GetVerificationRequest = {}  # type: ignore[typeddict-item]
    if "VerificationType" in data:
        import aws_sdk_partnercentral_account.types.verification_type

        out["verification_type"] = (
            aws_sdk_partnercentral_account.types.verification_type.deserialize_aws_json_1_0(
                data["VerificationType"]
            )
        )
    else:
        raise DeserializationError("GetVerificationRequest.verification_type required")
    return out
