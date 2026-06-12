"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesItems``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance

DescribeRecoveryInstancesItems: TypeAlias = list["aws_sdk_drs.types.recovery_instance.RecoveryInstance"]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesItems) -> list:
    import aws_sdk_drs.types.recovery_instance
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.recovery_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> DescribeRecoveryInstancesItems:
    import aws_sdk_drs.types.recovery_instance
    out: DescribeRecoveryInstancesItems = []
    for item in data:
        out.append(aws_sdk_drs.types.recovery_instance.deserialize_json(item))
    return out