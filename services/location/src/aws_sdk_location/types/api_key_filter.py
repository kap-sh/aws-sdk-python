"""Generated from Smithy shape ``com.amazonaws.location#ApiKeyFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_location.types.status

class ApiKeyFilter(TypedDict):
    key_status: NotRequired["aws_sdk_location.types.status.Status"]
    """<p>Filter on <code>Active</code> or <code>Expired</code> API keys.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyFilter) -> dict:
    out: dict = {}
    if "key_status" in value:
        out["KeyStatus"] = value["key_status"]
    return out


def deserialize_json(data: dict) -> ApiKeyFilter:
    out: ApiKeyFilter = {}  # type: ignore[typeddict-item]
    if "KeyStatus" in data:
        out["key_status"] = data["KeyStatus"]
    return out