"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingTransaction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.monetary_amount
    import aws_sdk_device_farm.types.offering_promotion_identifier
    import aws_sdk_device_farm.types.offering_status
    import aws_sdk_device_farm.types.transaction_identifier


class OfferingTransaction(TypedDict, closed=True):
    offering_status: NotRequired[
        "aws_sdk_device_farm.types.offering_status.OfferingStatus"
    ]
    """<p>The status of an offering transaction.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_device_farm.types.transaction_identifier.TransactionIdentifier"
    ]
    """<p>The transaction ID of the offering transaction.</p>"""
    offering_promotion_id: NotRequired[
        "aws_sdk_device_farm.types.offering_promotion_identifier.OfferingPromotionIdentifier"
    ]
    """<p>The ID that corresponds to a device offering promotion.</p>"""
    created_on: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The date on which an offering transaction was created.</p>"""
    cost: NotRequired["aws_sdk_device_farm.types.monetary_amount.MonetaryAmount"]
    """<p>The cost of an offering transaction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingTransaction) -> dict:
    out: dict = {}
    if "offering_status" in value:
        import aws_sdk_device_farm.types.offering_status

        out["offeringStatus"] = (
            aws_sdk_device_farm.types.offering_status.serialize_aws_json_1_1(
                value["offering_status"]
            )
        )
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    if "offering_promotion_id" in value:
        out["offeringPromotionId"] = value["offering_promotion_id"]
    if "created_on" in value:
        import aws_sdk_device_farm.types.date_time

        out["createdOn"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created_on"]
        )
    if "cost" in value:
        import aws_sdk_device_farm.types.monetary_amount

        out["cost"] = aws_sdk_device_farm.types.monetary_amount.serialize_aws_json_1_1(
            value["cost"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OfferingTransaction:
    out: OfferingTransaction = {}  # type: ignore[typeddict-item]
    if "offeringStatus" in data:
        import aws_sdk_device_farm.types.offering_status

        out["offering_status"] = (
            aws_sdk_device_farm.types.offering_status.deserialize_aws_json_1_1(
                data["offeringStatus"]
            )
        )
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    if "offeringPromotionId" in data:
        out["offering_promotion_id"] = data["offeringPromotionId"]
    if "createdOn" in data:
        import aws_sdk_device_farm.types.date_time

        out["created_on"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["createdOn"]
            )
        )
    if "cost" in data:
        import aws_sdk_device_farm.types.monetary_amount

        out["cost"] = (
            aws_sdk_device_farm.types.monetary_amount.deserialize_aws_json_1_1(
                data["cost"]
            )
        )
    return out
