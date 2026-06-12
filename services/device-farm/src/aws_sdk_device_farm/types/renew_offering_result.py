"""Generated from Smithy shape ``com.amazonaws.devicefarm#RenewOfferingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.offering_transaction


class RenewOfferingResult(TypedDict):
    offering_transaction: NotRequired[
        "aws_sdk_device_farm.types.offering_transaction.OfferingTransaction"
    ]
    """<p>Represents the status of the offering transaction for the renewal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewOfferingResult) -> dict:
    out: dict = {}
    if "offering_transaction" in value:
        import aws_sdk_device_farm.types.offering_transaction

        out["offeringTransaction"] = (
            aws_sdk_device_farm.types.offering_transaction.serialize_aws_json_1_1(
                value["offering_transaction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewOfferingResult:
    out: RenewOfferingResult = {}  # type: ignore[typeddict-item]
    if "offeringTransaction" in data:
        import aws_sdk_device_farm.types.offering_transaction

        out["offering_transaction"] = (
            aws_sdk_device_farm.types.offering_transaction.deserialize_aws_json_1_1(
                data["offeringTransaction"]
            )
        )
    return out
