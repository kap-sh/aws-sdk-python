"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ArchitectureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr_public.types.architecture

ArchitectureList: TypeAlias = list["capo_ecr_public.types.architecture.Architecture"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArchitectureList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ArchitectureList:
    return list(data)
