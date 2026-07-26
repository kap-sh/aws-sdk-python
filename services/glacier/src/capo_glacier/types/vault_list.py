"""Generated from Smithy shape ``com.amazonaws.glacier#VaultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glacier.types.describe_vault_output

VaultList: TypeAlias = list[
    "capo_glacier.types.describe_vault_output.DescribeVaultOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: VaultList) -> list:
    import capo_glacier.types.describe_vault_output

    out: list = []
    for item in value:
        out.append(capo_glacier.types.describe_vault_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> VaultList:
    import capo_glacier.types.describe_vault_output

    out: VaultList = []
    for item in data:
        out.append(capo_glacier.types.describe_vault_output.deserialize_json(item))
    return out
