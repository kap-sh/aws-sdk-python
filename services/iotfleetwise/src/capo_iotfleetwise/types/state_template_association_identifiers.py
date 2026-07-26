"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateAssociationIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotfleetwise.types.resource_identifier

StateTemplateAssociationIdentifiers: TypeAlias = list[
    "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateAssociationIdentifiers) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StateTemplateAssociationIdentifiers:
    return list(data)
