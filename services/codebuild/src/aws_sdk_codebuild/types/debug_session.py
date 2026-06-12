"""Generated from Smithy shape ``com.amazonaws.codebuild#DebugSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.wrapper_boolean


class DebugSession(TypedDict):
    session_enabled: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Specifies if session debugging is enabled for this build.</p>"""
    session_target: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains the identifier of the Session Manager session used for the build. To work with the paused build, you open this session to examine, control, and resume the build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugSession) -> dict:
    out: dict = {}
    if "session_enabled" in value:
        out["sessionEnabled"] = value["session_enabled"]
    if "session_target" in value:
        out["sessionTarget"] = value["session_target"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DebugSession:
    out: DebugSession = {}  # type: ignore[typeddict-item]
    if "sessionEnabled" in data:
        out["session_enabled"] = data["sessionEnabled"]
    if "sessionTarget" in data:
        out["session_target"] = data["sessionTarget"]
    return out
