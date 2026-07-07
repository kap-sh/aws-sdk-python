"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class CreateBackendConfigRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_manager_app_id: NotRequired[
        "aws_sdk_amplifybackend.types.__string.__string"
    ]
    """<p>The app ID for the backend manager.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendConfigRequest) -> dict:
    out: dict = {}
    if "backend_manager_app_id" in value:
        out["backendManagerAppId"] = value["backend_manager_app_id"]
    return out


def deserialize_json(data: dict) -> CreateBackendConfigRequest:
    out: CreateBackendConfigRequest = {}  # type: ignore[typeddict-item]
    if "backendManagerAppId" in data:
        out["backend_manager_app_id"] = data["backendManagerAppId"]
    return out
