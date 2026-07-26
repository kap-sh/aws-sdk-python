"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.association_id

AssociationIdList: TypeAlias = list["capo_ssm.types.association_id.AssociationId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssociationIdList:
    return list(data)
