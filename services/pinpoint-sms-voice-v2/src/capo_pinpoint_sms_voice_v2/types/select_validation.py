"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SelectValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.string_list


class SelectValidation(TypedDict, closed=True):
    min_choices: "int"
    """<p>The minimum number of choices for the select.</p>"""
    max_choices: "int"
    """<p>The maximum number of choices for the select.</p>"""
    options: "capo_pinpoint_sms_voice_v2.types.string_list.StringList"
    """<p>An array of strings for the possible selection options. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SelectValidation) -> dict:
    out: dict = {}
    out["MinChoices"] = value["min_choices"]
    out["MaxChoices"] = value["max_choices"]
    import capo_pinpoint_sms_voice_v2.types.string_list

    out["Options"] = (
        capo_pinpoint_sms_voice_v2.types.string_list.serialize_aws_json_1_0(
            value["options"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SelectValidation:
    out: SelectValidation = {}  # type: ignore[typeddict-item]
    if "MinChoices" in data:
        out["min_choices"] = data["MinChoices"]
    else:
        raise DeserializationError("SelectValidation.min_choices required")
    if "MaxChoices" in data:
        out["max_choices"] = data["MaxChoices"]
    else:
        raise DeserializationError("SelectValidation.max_choices required")
    if "Options" in data:
        import capo_pinpoint_sms_voice_v2.types.string_list

        out["options"] = (
            capo_pinpoint_sms_voice_v2.types.string_list.deserialize_aws_json_1_0(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("SelectValidation.options required")
    return out
