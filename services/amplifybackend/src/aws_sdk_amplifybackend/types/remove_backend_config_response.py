"""Generated from Smithy shape ``com.amazonaws.amplifybackend#RemoveBackendConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class RemoveBackendConfigResponse(TypedDict, closed=True):
    error: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>If the request fails, this error is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveBackendConfigResponse) -> dict:
    out: dict = {}
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> RemoveBackendConfigResponse:
    out: RemoveBackendConfigResponse = {}  # type: ignore[typeddict-item]
    if "error" in data:
        out["error"] = data["error"]
    return out
