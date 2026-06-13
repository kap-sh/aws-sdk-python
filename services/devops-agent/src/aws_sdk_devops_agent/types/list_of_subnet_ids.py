"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListOfSubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.subnet_id

ListOfSubnetIds: TypeAlias = list["aws_sdk_devops_agent.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfSubnetIds:
    return list(data)
