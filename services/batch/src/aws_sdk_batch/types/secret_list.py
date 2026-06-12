"""Generated from Smithy shape ``com.amazonaws.batch#SecretList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.secret

SecretList: TypeAlias = list["aws_sdk_batch.types.secret.Secret"]


# --- restJson1 ser/de ---
def serialize_json(value: SecretList) -> list:
    import aws_sdk_batch.types.secret

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.secret.serialize_json(item))
    return out


def deserialize_json(data: list) -> SecretList:
    import aws_sdk_batch.types.secret

    out: SecretList = []
    for item in data:
        out.append(aws_sdk_batch.types.secret.deserialize_json(item))
    return out
