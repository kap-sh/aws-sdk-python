"""Generated from Smithy shape ``com.amazonaws.ssm#FailedCreateAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.failed_create_association

FailedCreateAssociationList: TypeAlias = list[
    "capo_ssm.types.failed_create_association.FailedCreateAssociation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedCreateAssociationList) -> list:
    import capo_ssm.types.failed_create_association

    out: list = []
    for item in value:
        out.append(
            capo_ssm.types.failed_create_association.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedCreateAssociationList:
    import capo_ssm.types.failed_create_association

    out: FailedCreateAssociationList = []
    for item in data:
        out.append(
            capo_ssm.types.failed_create_association.deserialize_aws_json_1_1(item)
        )
    return out
