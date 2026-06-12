"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDashRoleAudio``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.dash_role_audio

__listOfDashRoleAudio: TypeAlias = list[
    "aws_sdk_medialive.types.dash_role_audio.DashRoleAudio"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashRoleAudio) -> list:
    import aws_sdk_medialive.types.dash_role_audio

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.dash_role_audio.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDashRoleAudio:
    import aws_sdk_medialive.types.dash_role_audio

    out: __listOfDashRoleAudio = []
    for item in data:
        out.append(aws_sdk_medialive.types.dash_role_audio.deserialize_json(item))
    return out
