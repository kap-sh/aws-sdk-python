"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ExternalUserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.external_user_id_type

ExternalUserIdList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.external_user_id_type.ExternalUserIdType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalUserIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExternalUserIdList:
    return list(data)
