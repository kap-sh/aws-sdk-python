"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ColdStorageOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean


class ColdStorageOptions(TypedDict):
    enabled: "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    """<p>Enable cold storage option. Accepted values true or false</p>"""


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
