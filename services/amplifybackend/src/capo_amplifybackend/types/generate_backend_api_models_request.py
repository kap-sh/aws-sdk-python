"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GenerateBackendAPIModelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class GenerateBackendAPIModelsRequest(TypedDict, closed=True):
    app_id: "capo_amplifybackend.types.__string.__string"
    """<p>The app ID.</p>"""
    backend_environment_name: "capo_amplifybackend.types.__string.__string"
    """<p>The name of the backend environment.</p>"""
    resource_name: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The name of this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateBackendAPIModelsRequest) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_json(data: dict) -> GenerateBackendAPIModelsRequest:
    out: GenerateBackendAPIModelsRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out
