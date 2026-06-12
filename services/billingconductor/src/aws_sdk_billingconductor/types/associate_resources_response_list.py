"""Generated from Smithy shape ``com.amazonaws.billingconductor#AssociateResourcesResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.associate_resource_response_element

AssociateResourcesResponseList: TypeAlias = list[
    "aws_sdk_billingconductor.types.associate_resource_response_element.AssociateResourceResponseElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourcesResponseList) -> list:
    import aws_sdk_billingconductor.types.associate_resource_response_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.associate_resource_response_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssociateResourcesResponseList:
    import aws_sdk_billingconductor.types.associate_resource_response_element

    out: AssociateResourcesResponseList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.associate_resource_response_element.deserialize_json(
                item
            )
        )
    return out
