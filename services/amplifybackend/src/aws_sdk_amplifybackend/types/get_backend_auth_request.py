"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetBackendAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class GetBackendAuthRequest(TypedDict, closed=True):
    app_id: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "aws_sdk_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    resource_name: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackendAuthRequest) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> GetBackendAuthRequest:
    out: GetBackendAuthRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
