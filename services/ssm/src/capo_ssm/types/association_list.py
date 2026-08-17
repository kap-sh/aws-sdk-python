"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association

AssociationList: TypeAlias = list["capo_ssm.types.association.Association"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationList) -> list:
    import capo_ssm.types.association

    out: list = []
    for item in value:
        out.append(capo_ssm.types.association.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationList:
    import capo_ssm.types.association

    out: AssociationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.association.deserialize_aws_json_1_1(item))
    return out
