"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SceneError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.error_message
    import aws_sdk_iottwinmaker.types.scene_error_code


class SceneError(TypedDict, closed=True):
    code: NotRequired["aws_sdk_iottwinmaker.types.scene_error_code.SceneErrorCode"]
    """<p>The SceneError code.</p>"""
    message: NotRequired["aws_sdk_iottwinmaker.types.error_message.ErrorMessage"]
    """<p>The SceneError message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SceneError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> SceneError:
    out: SceneError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
