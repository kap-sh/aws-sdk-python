"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.app_instance_user_summary

AppInstanceUserList: TypeAlias = list[
    "capo_chime_sdk_identity.types.app_instance_user_summary.AppInstanceUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserList) -> list:
    import capo_chime_sdk_identity.types.app_instance_user_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_identity.types.app_instance_user_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AppInstanceUserList:
    import capo_chime_sdk_identity.types.app_instance_user_summary

    out: AppInstanceUserList = []
    for item in data:
        out.append(
            capo_chime_sdk_identity.types.app_instance_user_summary.deserialize_json(
                item
            )
        )
    return out
