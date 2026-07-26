"""Generated from Smithy shape ``com.amazonaws.lightsail#KeyPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.key_pair

KeyPairList: TypeAlias = list["capo_lightsail.types.key_pair.KeyPair"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyPairList) -> list:
    import capo_lightsail.types.key_pair

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.key_pair.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyPairList:
    import capo_lightsail.types.key_pair

    out: KeyPairList = []
    for item in data:
        out.append(capo_lightsail.types.key_pair.deserialize_aws_json_1_1(item))
    return out
