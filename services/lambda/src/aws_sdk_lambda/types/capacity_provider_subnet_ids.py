"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderSubnetIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.subnet_id

CapacityProviderSubnetIds: TypeAlias = list["aws_sdk_lambda.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderSubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> CapacityProviderSubnetIds:
    return list(data)
