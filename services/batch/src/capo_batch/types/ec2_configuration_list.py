"""Generated from Smithy shape ``com.amazonaws.batch#Ec2ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.ec2_configuration

Ec2ConfigurationList: TypeAlias = list[
    "capo_batch.types.ec2_configuration.Ec2Configuration"
]


# --- restJson1 ser/de ---
def serialize_json(value: Ec2ConfigurationList) -> list:
    import capo_batch.types.ec2_configuration

    out: list = []
    for item in value:
        out.append(capo_batch.types.ec2_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ec2ConfigurationList:
    import capo_batch.types.ec2_configuration

    out: Ec2ConfigurationList = []
    for item in data:
        out.append(capo_batch.types.ec2_configuration.deserialize_json(item))
    return out
