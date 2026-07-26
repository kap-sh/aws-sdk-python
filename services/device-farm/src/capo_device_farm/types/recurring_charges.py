"""Generated from Smithy shape ``com.amazonaws.devicefarm#RecurringCharges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.recurring_charge

RecurringCharges: TypeAlias = list[
    "capo_device_farm.types.recurring_charge.RecurringCharge"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringCharges) -> list:
    import capo_device_farm.types.recurring_charge

    out: list = []
    for item in value:
        out.append(capo_device_farm.types.recurring_charge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecurringCharges:
    import capo_device_farm.types.recurring_charge

    out: RecurringCharges = []
    for item in data:
        out.append(
            capo_device_farm.types.recurring_charge.deserialize_aws_json_1_1(item)
        )
    return out
