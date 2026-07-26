"""Generated from Smithy shape ``com.amazonaws.evs#EipAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.eip_association

EipAssociationList: TypeAlias = list["capo_evs.types.eip_association.EipAssociation"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EipAssociationList) -> list:
    import capo_evs.types.eip_association

    out: list = []
    for item in value:
        out.append(capo_evs.types.eip_association.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EipAssociationList:
    import capo_evs.types.eip_association

    out: EipAssociationList = []
    for item in data:
        out.append(capo_evs.types.eip_association.deserialize_aws_json_1_0(item))
    return out
