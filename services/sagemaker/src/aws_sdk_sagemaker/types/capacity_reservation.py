"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacityReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_reservation_type


class CapacityReservation(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the Capacity Reservation.</p>"""
    type: NotRequired[
        "aws_sdk_sagemaker.types.capacity_reservation_type.CapacityReservationType"
    ]
    """<p>The type of Capacity Reservation. Valid values are <code>ODCR</code> (On-Demand Capacity Reservation) or <code>CRG</code> (Capacity Reservation Group).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservation) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        import aws_sdk_sagemaker.types.capacity_reservation_type

        out["Type"] = (
            aws_sdk_sagemaker.types.capacity_reservation_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityReservation:
    out: CapacityReservation = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        import aws_sdk_sagemaker.types.capacity_reservation_type

        out["type"] = (
            aws_sdk_sagemaker.types.capacity_reservation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
