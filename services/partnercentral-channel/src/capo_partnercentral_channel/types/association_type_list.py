"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AssociationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.association_type

AssociationTypeList: TypeAlias = list[
    "capo_partnercentral_channel.types.association_type.AssociationType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociationTypeList) -> list:
    import capo_partnercentral_channel.types.association_type

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_channel.types.association_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AssociationTypeList:
    import capo_partnercentral_channel.types.association_type

    out: AssociationTypeList = []
    for item in data:
        out.append(
            capo_partnercentral_channel.types.association_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
