"""Generated from Smithy shape ``com.amazonaws.opensearch#ColdStorageOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean


class ColdStorageOptions(TypedDict, closed=True):
    enabled: "aws_sdk_opensearch.types.boolean.Boolean"
    """<p>Whether to enable or disable cold storage on the domain. You must enable UltraWarm storage to enable cold storage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColdStorageOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ColdStorageOptions:
    out: ColdStorageOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("ColdStorageOptions.enabled required")
    return out
