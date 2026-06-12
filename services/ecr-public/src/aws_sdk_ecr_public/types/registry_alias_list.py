"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.registry_alias

RegistryAliasList: TypeAlias = list[
    "aws_sdk_ecr_public.types.registry_alias.RegistryAlias"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryAliasList) -> list:
    import aws_sdk_ecr_public.types.registry_alias

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr_public.types.registry_alias.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegistryAliasList:
    import aws_sdk_ecr_public.types.registry_alias

    out: RegistryAliasList = []
    for item in data:
        out.append(
            aws_sdk_ecr_public.types.registry_alias.deserialize_aws_json_1_1(item)
        )
    return out
