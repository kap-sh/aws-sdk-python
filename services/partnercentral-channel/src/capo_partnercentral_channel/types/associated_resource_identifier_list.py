"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AssociatedResourceIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.associated_resource_identifier

AssociatedResourceIdentifierList: TypeAlias = list[
    "capo_partnercentral_channel.types.associated_resource_identifier.AssociatedResourceIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociatedResourceIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> AssociatedResourceIdentifierList:
    return list(data)
