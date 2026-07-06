"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class GetBackendRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The name of the backend environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendRequest) -> dict:
    out: dict = {}
    if "backend_environment_name" in value:
        out["backendEnvironmentName"] = value["backend_environment_name"]
    return out


def deserialize_json(data: dict) -> GetBackendRequest:
    out: GetBackendRequest = {}  # type: ignore[typeddict-item]
    if "backendEnvironmentName" in data:
        out["backend_environment_name"] = data["backendEnvironmentName"]
    return out
