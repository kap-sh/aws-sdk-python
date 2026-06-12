"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDashRoleCaption``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.dash_role_caption

__listOfDashRoleCaption: TypeAlias = list[
    "aws_sdk_medialive.types.dash_role_caption.DashRoleCaption"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashRoleCaption) -> list:
    import aws_sdk_medialive.types.dash_role_caption

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.dash_role_caption.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDashRoleCaption:
    import aws_sdk_medialive.types.dash_role_caption

    out: __listOfDashRoleCaption = []
    for item in data:
        out.append(aws_sdk_medialive.types.dash_role_caption.deserialize_json(item))
    return out
