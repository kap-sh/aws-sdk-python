"""Generated from Smithy shape ``com.amazonaws.devicefarm#PurchaseOfferingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_transaction


class PurchaseOfferingResult(TypedDict, closed=True):
    offering_transaction: NotRequired[
        "aws_sdk_device_farm.types.offering_transaction.OfferingTransaction"
    ]
    """<p>Represents the offering transaction for the purchase result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseOfferingResult) -> dict:
    out: dict = {}
    if "offering_transaction" in value:
        import aws_sdk_device_farm.types.offering_transaction

        out["offeringTransaction"] = (
            aws_sdk_device_farm.types.offering_transaction.serialize_aws_json_1_1(
                value["offering_transaction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseOfferingResult:
    out: PurchaseOfferingResult = {}  # type: ignore[typeddict-item]
    if "offeringTransaction" in data:
        import aws_sdk_device_farm.types.offering_transaction

        out["offering_transaction"] = (
            aws_sdk_device_farm.types.offering_transaction.deserialize_aws_json_1_1(
                data["offeringTransaction"]
            )
        )
    return out
