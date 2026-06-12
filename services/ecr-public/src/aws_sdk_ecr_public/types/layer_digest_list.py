"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerDigestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.layer_digest

LayerDigestList: TypeAlias = list["aws_sdk_ecr_public.types.layer_digest.LayerDigest"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerDigestList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LayerDigestList:
    return list(data)
