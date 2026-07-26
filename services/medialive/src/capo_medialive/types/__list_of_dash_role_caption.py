"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfDashRoleCaption``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.dash_role_caption

__listOfDashRoleCaption: TypeAlias = list[
    "capo_medialive.types.dash_role_caption.DashRoleCaption"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDashRoleCaption) -> list:
    import capo_medialive.types.dash_role_caption

    out: list = []
    for item in value:
        out.append(capo_medialive.types.dash_role_caption.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDashRoleCaption:
    import capo_medialive.types.dash_role_caption

    out: __listOfDashRoleCaption = []
    for item in data:
        out.append(capo_medialive.types.dash_role_caption.deserialize_json(item))
    return out
