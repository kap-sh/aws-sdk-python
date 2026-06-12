"""Generated from Smithy shape ``com.amazonaws.shield#AttackProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_property

AttackProperties: TypeAlias = list[
    "aws_sdk_shield.types.attack_property.AttackProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackProperties) -> list:
    import aws_sdk_shield.types.attack_property

    out: list = []
    for item in value:
        out.append(aws_sdk_shield.types.attack_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttackProperties:
    import aws_sdk_shield.types.attack_property

    out: AttackProperties = []
    for item in data:
        out.append(aws_sdk_shield.types.attack_property.deserialize_aws_json_1_1(item))
    return out
