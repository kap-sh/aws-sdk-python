"""Generated from Smithy shape ``com.amazonaws.billingconductor#DisassociateResourcesResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.disassociate_resource_response_element

DisassociateResourcesResponseList: TypeAlias = list[
    "aws_sdk_billingconductor.types.disassociate_resource_response_element.DisassociateResourceResponseElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourcesResponseList) -> list:
    import aws_sdk_billingconductor.types.disassociate_resource_response_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.disassociate_resource_response_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DisassociateResourcesResponseList:
    import aws_sdk_billingconductor.types.disassociate_resource_response_element

    out: DisassociateResourcesResponseList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.disassociate_resource_response_element.deserialize_json(
                item
            )
        )
    return out
