"""Generated from Smithy shape ``com.amazonaws.ssmsap#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.instance_id

InstanceList: TypeAlias = list["aws_sdk_ssm_sap.types.instance_id.InstanceId"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceList:
    return list(data)
