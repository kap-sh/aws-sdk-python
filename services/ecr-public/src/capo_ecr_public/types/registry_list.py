"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr_public.types.registry

RegistryList: TypeAlias = list["capo_ecr_public.types.registry.Registry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryList) -> list:
    import capo_ecr_public.types.registry

    out: list = []
    for item in value:
        out.append(capo_ecr_public.types.registry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RegistryList:
    import capo_ecr_public.types.registry

    out: RegistryList = []
    for item in data:
        out.append(capo_ecr_public.types.registry.deserialize_aws_json_1_1(item))
    return out
