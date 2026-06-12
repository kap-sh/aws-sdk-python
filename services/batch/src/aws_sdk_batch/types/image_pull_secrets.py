"""Generated from Smithy shape ``com.amazonaws.batch#ImagePullSecrets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.image_pull_secret

ImagePullSecrets: TypeAlias = list[
    "aws_sdk_batch.types.image_pull_secret.ImagePullSecret"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImagePullSecrets) -> list:
    import aws_sdk_batch.types.image_pull_secret

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.image_pull_secret.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImagePullSecrets:
    import aws_sdk_batch.types.image_pull_secret

    out: ImagePullSecrets = []
    for item in data:
        out.append(aws_sdk_batch.types.image_pull_secret.deserialize_json(item))
    return out
