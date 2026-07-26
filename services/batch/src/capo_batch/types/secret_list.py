"""Generated from Smithy shape ``com.amazonaws.batch#SecretList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.secret

SecretList: TypeAlias = list["capo_batch.types.secret.Secret"]


# --- restJson1 ser/de ---
def serialize_json(value: SecretList) -> list:
    import capo_batch.types.secret

    out: list = []
    for item in value:
        out.append(capo_batch.types.secret.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecretList:
    import capo_batch.types.secret

    out: SecretList = []
    for item in data:
        out.append(capo_batch.types.secret.deserialize_json(item))
    return out
