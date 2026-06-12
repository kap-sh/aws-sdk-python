"""Generated from Smithy shape ``com.amazonaws.memorydb#RecurringChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.recurring_charge

RecurringChargeList: TypeAlias = list[
    "aws_sdk_memorydb.types.recurring_charge.RecurringCharge"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringChargeList) -> list:
    import aws_sdk_memorydb.types.recurring_charge

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.recurring_charge.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RecurringChargeList:
    import aws_sdk_memorydb.types.recurring_charge

    out: RecurringChargeList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.recurring_charge.deserialize_aws_json_1_1(item)
        )
    return out
