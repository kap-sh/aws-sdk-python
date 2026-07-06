"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CloneBackendRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class CloneBackendRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    target_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the destination backend environment to be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloneBackendRequest) -> dict:
    out: dict = {}
    if "target_environment_name" in value:
        out["targetEnvironmentName"] = value["target_environment_name"]
    return out


def deserialize_json(data: dict) -> CloneBackendRequest:
    out: CloneBackendRequest = {}  # type: ignore[typeddict-item]
    if "targetEnvironmentName" in data:
        out["target_environment_name"] = data["targetEnvironmentName"]
    return out
