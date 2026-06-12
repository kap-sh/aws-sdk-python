"""Generated from Smithy shape ``com.amazonaws.pinpoint#OpenHours``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules


class OpenHours(TypedDict):
    email: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.MapOfListOfOpenHoursRules"
    ]
    """<p>Specifies the schedule settings for the email channel.</p>"""
    sms: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.MapOfListOfOpenHoursRules"
    ]
    """<p>Specifies the schedule settings for the SMS channel.</p>"""
    push: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.MapOfListOfOpenHoursRules"
    ]
    """<p>Specifies the schedule settings for the push channel.</p>"""
    voice: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.MapOfListOfOpenHoursRules"
    ]
    """<p>Specifies the schedule settings for the voice channel.</p>"""
    custom: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.MapOfListOfOpenHoursRules"
    ]
    """<p>Specifies the schedule settings for the custom channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenHours) -> dict:
    out: dict = {}
    if "email" in value:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["EMAIL"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.serialize_json(
                value["email"]
            )
        )
    if "sms" in value:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["SMS"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.serialize_json(
                value["sms"]
            )
        )
    if "push" in value:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["PUSH"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.serialize_json(
                value["push"]
            )
        )
    if "voice" in value:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["VOICE"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.serialize_json(
                value["voice"]
            )
        )
    if "custom" in value:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["CUSTOM"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.serialize_json(
                value["custom"]
            )
        )
    return out


def deserialize_json(data: dict) -> OpenHours:
    out: OpenHours = {}  # type: ignore[typeddict-item]
    if "EMAIL" in data:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["email"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.deserialize_json(
                data["EMAIL"]
            )
        )
    if "SMS" in data:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["sms"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.deserialize_json(
                data["SMS"]
            )
        )
    if "PUSH" in data:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["push"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.deserialize_json(
                data["PUSH"]
            )
        )
    if "VOICE" in data:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["voice"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.deserialize_json(
                data["VOICE"]
            )
        )
    if "CUSTOM" in data:
        import aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules

        out["custom"] = (
            aws_sdk_pinpoint.types.map_of_list_of_open_hours_rules.deserialize_json(
                data["CUSTOM"]
            )
        )
    return out
