"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceBotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_bot_summary

AppInstanceBotList: TypeAlias = list[
    "aws_sdk_chime_sdk_identity.types.app_instance_bot_summary.AppInstanceBotSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceBotList) -> list:
    import aws_sdk_chime_sdk_identity.types.app_instance_bot_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_bot_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AppInstanceBotList:
    import aws_sdk_chime_sdk_identity.types.app_instance_bot_summary

    out: AppInstanceBotList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_identity.types.app_instance_bot_summary.deserialize_json(
                item
            )
        )
    return out
