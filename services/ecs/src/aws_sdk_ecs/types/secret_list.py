"""Generated from Smithy shape ``com.amazonaws.ecs#SecretList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.secret

SecretList: TypeAlias = list["aws_sdk_ecs.types.secret.Secret"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretList) -> list:
    import aws_sdk_ecs.types.secret

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.secret.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SecretList:
    import aws_sdk_ecs.types.secret

    out: SecretList = []
    for item in data:
        out.append(aws_sdk_ecs.types.secret.deserialize_aws_json_1_1(item))
    return out
