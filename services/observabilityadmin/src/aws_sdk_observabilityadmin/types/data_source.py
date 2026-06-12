"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DataSource``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DataSource(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the data source. For CloudWatch Logs sources, this corresponds to the <code>data_source_name</code> from the log event metadata. For third-party sources, this is either the configured <code>data_source_name</code> or defaults to the plugin name if not specified.</p>"""
    type: NotRequired["str"]
    """<p>The type of the data source. For CloudWatch Logs sources, this corresponds to the <code>data_source_type</code> from the log event metadata. For third-party sources, this field is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSource) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
