"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SelectOptionDescriptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.select_option_description

SelectOptionDescriptionsList: TypeAlias = list[
    "capo_pinpoint_sms_voice_v2.types.select_option_description.SelectOptionDescription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SelectOptionDescriptionsList) -> list:
    import capo_pinpoint_sms_voice_v2.types.select_option_description

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_sms_voice_v2.types.select_option_description.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SelectOptionDescriptionsList:
    import capo_pinpoint_sms_voice_v2.types.select_option_description

    out: SelectOptionDescriptionsList = []
    for item in data:
        out.append(
            capo_pinpoint_sms_voice_v2.types.select_option_description.deserialize_aws_json_1_0(
                item
            )
        )
    return out
