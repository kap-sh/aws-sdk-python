"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DomainObjectTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.domain_object_types_list_item

DomainObjectTypesList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.domain_object_types_list_item.DomainObjectTypesListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainObjectTypesList) -> list:
    import aws_sdk_customer_profiles.types.domain_object_types_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.domain_object_types_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DomainObjectTypesList:
    import aws_sdk_customer_profiles.types.domain_object_types_list_item

    out: DomainObjectTypesList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.domain_object_types_list_item.deserialize_json(
                item
            )
        )
    return out
