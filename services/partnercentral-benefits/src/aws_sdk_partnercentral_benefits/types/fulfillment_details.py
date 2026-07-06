"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_partnercentral_benefits.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.access_details
    import aws_sdk_partnercentral_benefits.types.consumable_details
    import aws_sdk_partnercentral_benefits.types.credit_details
    import aws_sdk_partnercentral_benefits.types.disbursement_details


class _FulfillmentDetails_DisbursementDetails(TypedDict, closed=True):
    DisbursementDetails: (
        "aws_sdk_partnercentral_benefits.types.disbursement_details.DisbursementDetails"
    )


class _FulfillmentDetails_ConsumableDetails(TypedDict, closed=True):
    ConsumableDetails: (
        "aws_sdk_partnercentral_benefits.types.consumable_details.ConsumableDetails"
    )


class _FulfillmentDetails_CreditDetails(TypedDict, closed=True):
    CreditDetails: "aws_sdk_partnercentral_benefits.types.credit_details.CreditDetails"


class _FulfillmentDetails_AccessDetails(TypedDict, closed=True):
    AccessDetails: "aws_sdk_partnercentral_benefits.types.access_details.AccessDetails"


FulfillmentDetails: TypeAlias = (
    _FulfillmentDetails_DisbursementDetails
    | _FulfillmentDetails_ConsumableDetails
    | _FulfillmentDetails_CreditDetails
    | _FulfillmentDetails_AccessDetails
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FulfillmentDetails) -> dict:
    if "DisbursementDetails" in value:
        import aws_sdk_partnercentral_benefits.types.disbursement_details

        return {
            "DisbursementDetails": aws_sdk_partnercentral_benefits.types.disbursement_details.serialize_aws_json_1_0(
                value["DisbursementDetails"]
            )
        }
    elif "ConsumableDetails" in value:
        import aws_sdk_partnercentral_benefits.types.consumable_details

        return {
            "ConsumableDetails": aws_sdk_partnercentral_benefits.types.consumable_details.serialize_aws_json_1_0(
                value["ConsumableDetails"]
            )
        }
    elif "CreditDetails" in value:
        import aws_sdk_partnercentral_benefits.types.credit_details

        return {
            "CreditDetails": aws_sdk_partnercentral_benefits.types.credit_details.serialize_aws_json_1_0(
                value["CreditDetails"]
            )
        }
    elif "AccessDetails" in value:
        import aws_sdk_partnercentral_benefits.types.access_details

        return {
            "AccessDetails": aws_sdk_partnercentral_benefits.types.access_details.serialize_aws_json_1_0(
                value["AccessDetails"]
            )
        }
    else:
        raise SerializationError("FulfillmentDetails: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FulfillmentDetails:
    if "DisbursementDetails" in data:
        import aws_sdk_partnercentral_benefits.types.disbursement_details

        return {
            "DisbursementDetails": aws_sdk_partnercentral_benefits.types.disbursement_details.deserialize_aws_json_1_0(
                data["DisbursementDetails"]
            )
        }
    elif "ConsumableDetails" in data:
        import aws_sdk_partnercentral_benefits.types.consumable_details

        return {
            "ConsumableDetails": aws_sdk_partnercentral_benefits.types.consumable_details.deserialize_aws_json_1_0(
                data["ConsumableDetails"]
            )
        }
    elif "CreditDetails" in data:
        import aws_sdk_partnercentral_benefits.types.credit_details

        return {
            "CreditDetails": aws_sdk_partnercentral_benefits.types.credit_details.deserialize_aws_json_1_0(
                data["CreditDetails"]
            )
        }
    elif "AccessDetails" in data:
        import aws_sdk_partnercentral_benefits.types.access_details

        return {
            "AccessDetails": aws_sdk_partnercentral_benefits.types.access_details.deserialize_aws_json_1_0(
                data["AccessDetails"]
            )
        }
    else:
        raise DeserializationError("FulfillmentDetails: no recognized variant key")
