"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DataStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.optional_boolean


class DataStoreRequest(TypedDict, closed=True):
    enabled: NotRequired[
        "capo_customer_profiles.types.optional_boolean.optionalBoolean"
    ]
    """<p>Enabled: Set to true to enabled data store for this domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataStoreRequest) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> DataStoreRequest:
    out: DataStoreRequest = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
