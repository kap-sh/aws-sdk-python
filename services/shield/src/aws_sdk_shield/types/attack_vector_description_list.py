"""Generated from Smithy shape ``com.amazonaws.shield#AttackVectorDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_vector_description

AttackVectorDescriptionList: TypeAlias = list[
    "aws_sdk_shield.types.attack_vector_description.AttackVectorDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVectorDescriptionList) -> list:
    import aws_sdk_shield.types.attack_vector_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_shield.types.attack_vector_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttackVectorDescriptionList:
    import aws_sdk_shield.types.attack_vector_description

    out: AttackVectorDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_shield.types.attack_vector_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
