"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_property

InstanceProperties: TypeAlias = list[
    "capo_ssm.types.instance_property.InstanceProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProperties) -> list:
    import capo_ssm.types.instance_property

    out: list = []
    for item in value:
        out.append(capo_ssm.types.instance_property.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InstanceProperties:
    import capo_ssm.types.instance_property

    out: InstanceProperties = []
    for item in data:
        out.append(capo_ssm.types.instance_property.deserialize_aws_json_1_1(item))
    return out
