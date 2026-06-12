"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.association_description

AssociationDescriptionList: TypeAlias = list[
    "aws_sdk_ssm.types.association_description.AssociationDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationDescriptionList) -> list:
    import aws_sdk_ssm.types.association_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.association_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssociationDescriptionList:
    import aws_sdk_ssm.types.association_description

    out: AssociationDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.association_description.deserialize_aws_json_1_1(item)
        )
    return out
