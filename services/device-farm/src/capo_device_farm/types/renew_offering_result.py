"""Generated from Smithy shape ``com.amazonaws.devicefarm#RenewOfferingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.offering_transaction


class RenewOfferingResult(TypedDict, closed=True):
    offering_transaction: NotRequired[
        "capo_device_farm.types.offering_transaction.OfferingTransaction"
    ]
    """<p>Represents the status of the offering transaction for the renewal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewOfferingResult) -> dict:
    out: dict = {}
    if "offering_transaction" in value:
        import capo_device_farm.types.offering_transaction

        out["offeringTransaction"] = (
            capo_device_farm.types.offering_transaction.serialize_aws_json_1_1(
                value["offering_transaction"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewOfferingResult:
    out: RenewOfferingResult = {}  # type: ignore[typeddict-item]
    if "offeringTransaction" in data:
        import capo_device_farm.types.offering_transaction

        out["offering_transaction"] = (
            capo_device_farm.types.offering_transaction.deserialize_aws_json_1_1(
                data["offeringTransaction"]
            )
        )
    return out
