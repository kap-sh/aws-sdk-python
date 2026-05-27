"""Generated from Smithy shape ``com.amazonaws.eks#EncryptionConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.encryption_config

EncryptionConfigList: TypeAlias = list[
    "aws_sdk_eks.types.encryption_config.EncryptionConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfigList) -> list:
    import aws_sdk_eks.types.encryption_config

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.encryption_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EncryptionConfigList:
    import aws_sdk_eks.types.encryption_config

    out: EncryptionConfigList = []
    for item in data:
        out.append(aws_sdk_eks.types.encryption_config.deserialize_json(item))
    return out
