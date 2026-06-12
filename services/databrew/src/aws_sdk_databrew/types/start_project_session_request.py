"""Generated from Smithy shape ``com.amazonaws.databrew#StartProjectSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.assume_control
    import aws_sdk_databrew.types.project_name


class StartProjectSessionRequest(TypedDict):
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project to act upon.</p>"""
    assume_control: "aws_sdk_databrew.types.assume_control.AssumeControl"
    """<p>A value that, if true, enables you to take control of a session, even if a different client is currently accessing the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProjectSessionRequest) -> dict:
    out: dict = {}
    out["AssumeControl"] = value.get("assume_control", False)
    return out


def deserialize_json(data: dict) -> StartProjectSessionRequest:
    out: StartProjectSessionRequest = {}  # type: ignore[typeddict-item]
    if "AssumeControl" in data:
        out["assume_control"] = data["AssumeControl"]
    else:
        out["assume_control"] = False
    return out
