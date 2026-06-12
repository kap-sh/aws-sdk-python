"""Generated from Smithy shape ``com.amazonaws.glacier#ProvisionedCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.provisioned_capacity_description

ProvisionedCapacityList: TypeAlias = list[
    "aws_sdk_glacier.types.provisioned_capacity_description.ProvisionedCapacityDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedCapacityList) -> list:
    import aws_sdk_glacier.types.provisioned_capacity_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glacier.types.provisioned_capacity_description.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProvisionedCapacityList:
    import aws_sdk_glacier.types.provisioned_capacity_description

    out: ProvisionedCapacityList = []
    for item in data:
        out.append(
            aws_sdk_glacier.types.provisioned_capacity_description.deserialize_json(
                item
            )
        )
    return out
