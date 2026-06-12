"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.offering
    import aws_sdk_device_farm.types.offering_transaction_type


class OfferingStatus(TypedDict):
    type: NotRequired[
        "aws_sdk_device_farm.types.offering_transaction_type.OfferingTransactionType"
    ]
    """<p>The type specified for the offering status.</p>"""
    offering: NotRequired["aws_sdk_device_farm.types.offering.Offering"]
    """<p>Represents the metadata of an offering status.</p>"""
    quantity: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The number of available devices in the offering.</p>"""
    effective_on: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The date on which the offering is effective.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingStatus) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_device_farm.types.offering_transaction_type

        out["type"] = (
            aws_sdk_device_farm.types.offering_transaction_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "offering" in value:
        import aws_sdk_device_farm.types.offering

        out["offering"] = aws_sdk_device_farm.types.offering.serialize_aws_json_1_1(
            value["offering"]
        )
    if "quantity" in value:
        out["quantity"] = value["quantity"]
    if "effective_on" in value:
        import aws_sdk_device_farm.types.date_time

        out["effectiveOn"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["effective_on"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OfferingStatus:
    out: OfferingStatus = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_device_farm.types.offering_transaction_type

        out["type"] = (
            aws_sdk_device_farm.types.offering_transaction_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "offering" in data:
        import aws_sdk_device_farm.types.offering

        out["offering"] = aws_sdk_device_farm.types.offering.deserialize_aws_json_1_1(
            data["offering"]
        )
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    if "effectiveOn" in data:
        import aws_sdk_device_farm.types.date_time

        out["effective_on"] = (
            aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
                data["effectiveOn"]
            )
        )
    return out
