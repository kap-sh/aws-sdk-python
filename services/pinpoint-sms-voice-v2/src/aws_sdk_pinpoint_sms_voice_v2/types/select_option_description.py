"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SelectOptionDescription``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError


class SelectOptionDescription(TypedDict, closed=True):
    option: "str"
    """<p>The value of the option.</p>"""
    title: NotRequired["str"]
    """<p>The title of the select option.</p>"""
    description: NotRequired["str"]
    """<p>A description of the option meaning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SelectOptionDescription) -> dict:
    out: dict = {}
    out["Option"] = value["option"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SelectOptionDescription:
    out: SelectOptionDescription = {}  # type: ignore[typeddict-item]
    if "Option" in data:
        out["option"] = data["Option"]
    else:
        raise DeserializationError("SelectOptionDescription.option required")
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
