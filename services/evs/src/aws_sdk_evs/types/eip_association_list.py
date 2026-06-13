"""Generated from Smithy shape ``com.amazonaws.evs#EipAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.eip_association

EipAssociationList: TypeAlias = list["aws_sdk_evs.types.eip_association.EipAssociation"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EipAssociationList) -> list:
    import aws_sdk_evs.types.eip_association

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.eip_association.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EipAssociationList:
    import aws_sdk_evs.types.eip_association

    out: EipAssociationList = []
    for item in data:
        out.append(aws_sdk_evs.types.eip_association.deserialize_aws_json_1_0(item))
    return out
