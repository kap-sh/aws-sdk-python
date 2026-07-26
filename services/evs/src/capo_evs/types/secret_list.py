"""Generated from Smithy shape ``com.amazonaws.evs#SecretList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.secret

SecretList: TypeAlias = list["capo_evs.types.secret.Secret"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecretList) -> list:
    import capo_evs.types.secret

    out: list = []
    for item in value:
        out.append(capo_evs.types.secret.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SecretList:
    import capo_evs.types.secret

    out: SecretList = []
    for item in data:
        out.append(capo_evs.types.secret.deserialize_aws_json_1_0(item))
    return out
