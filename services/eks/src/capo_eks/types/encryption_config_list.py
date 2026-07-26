"""Generated from Smithy shape ``com.amazonaws.eks#EncryptionConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.encryption_config

EncryptionConfigList: TypeAlias = list[
    "capo_eks.types.encryption_config.EncryptionConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionConfigList) -> list:
    import capo_eks.types.encryption_config

    out: list = []
    for item in value:
        out.append(capo_eks.types.encryption_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EncryptionConfigList:
    import capo_eks.types.encryption_config

    out: EncryptionConfigList = []
    for item in data:
        out.append(capo_eks.types.encryption_config.deserialize_json(item))
    return out
