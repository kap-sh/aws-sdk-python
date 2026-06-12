"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#FaultCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.fault_code

FaultCodes: TypeAlias = list["aws_sdk_lookoutequipment.types.fault_code.FaultCode"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FaultCodes) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> FaultCodes:
    return list(data)
