"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#Participant``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_account.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.account_summary
    import aws_sdk_partnercentral_account.types.partner_profile_summary
    import aws_sdk_partnercentral_account.types.seller_profile_summary


class _Participant_PartnerProfile(TypedDict):
    PartnerProfile: "aws_sdk_partnercentral_account.types.partner_profile_summary.PartnerProfileSummary"


class _Participant_SellerProfile(TypedDict):
    SellerProfile: "aws_sdk_partnercentral_account.types.seller_profile_summary.SellerProfileSummary"


class _Participant_Account(TypedDict):
    Account: "aws_sdk_partnercentral_account.types.account_summary.AccountSummary"


Participant: TypeAlias = (
    _Participant_PartnerProfile | _Participant_SellerProfile | _Participant_Account
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Participant) -> dict:
    if "PartnerProfile" in value:
        import aws_sdk_partnercentral_account.types.partner_profile_summary

        return {
            "PartnerProfile": aws_sdk_partnercentral_account.types.partner_profile_summary.serialize_aws_json_1_0(
                value["PartnerProfile"]
            )
        }
    elif "SellerProfile" in value:
        import aws_sdk_partnercentral_account.types.seller_profile_summary

        return {
            "SellerProfile": aws_sdk_partnercentral_account.types.seller_profile_summary.serialize_aws_json_1_0(
                value["SellerProfile"]
            )
        }
    elif "Account" in value:
        import aws_sdk_partnercentral_account.types.account_summary

        return {
            "Account": aws_sdk_partnercentral_account.types.account_summary.serialize_aws_json_1_0(
                value["Account"]
            )
        }
    else:
        raise SerializationError("Participant: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Participant:
    if "PartnerProfile" in data:
        import aws_sdk_partnercentral_account.types.partner_profile_summary

        return {
            "PartnerProfile": aws_sdk_partnercentral_account.types.partner_profile_summary.deserialize_aws_json_1_0(
                data["PartnerProfile"]
            )
        }
    elif "SellerProfile" in data:
        import aws_sdk_partnercentral_account.types.seller_profile_summary

        return {
            "SellerProfile": aws_sdk_partnercentral_account.types.seller_profile_summary.deserialize_aws_json_1_0(
                data["SellerProfile"]
            )
        }
    elif "Account" in data:
        import aws_sdk_partnercentral_account.types.account_summary

        return {
            "Account": aws_sdk_partnercentral_account.types.account_summary.deserialize_aws_json_1_0(
                data["Account"]
            )
        }
    else:
        raise DeserializationError("Participant: no recognized variant key")
