"""Generated from Smithy shape ``com.amazonaws.medialive#MotionGraphicsActivateScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__long_min0_max86400000
    import aws_sdk_medialive.types.__string


class MotionGraphicsActivateScheduleActionSettings(TypedDict, closed=True):
    duration: NotRequired[
        "aws_sdk_medialive.types.__long_min0_max86400000.__longMin0Max86400000"
    ]
    """Duration (in milliseconds) that motion graphics should render on to the video stream. Leaving out this property or setting to 0 will result in rendering continuing until a deactivate action is processed."""
    password_param: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Key used to extract the password from EC2 Parameter store"""
    url: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """URI of the HTML5 content to be rendered into the live stream."""
    username: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Documentation update needed"""


# --- restJson1 ser/de ---
def serialize_json(value: MotionGraphicsActivateScheduleActionSettings) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "url" in value:
        out["url"] = value["url"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> MotionGraphicsActivateScheduleActionSettings:
    out: MotionGraphicsActivateScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "passwordParam" in data:
        out["password_param"] = data["passwordParam"]
    if "url" in data:
        out["url"] = data["url"]
    if "username" in data:
        out["username"] = data["username"]
    return out
