"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IdMappingConfig``."""

from typing import TypedDict


class IdMappingConfig(TypedDict):
    allow_use_as_dimension_column: "bool"
    """<p>An indicator as to whether you can use your column as a dimension column in the ID mapping table (<code>TRUE</code>) or not (<code>FALSE</code>).</p> <p>Default is <code>FALSE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingConfig) -> dict:
    out: dict = {}
    out["allowUseAsDimensionColumn"] = value.get("allow_use_as_dimension_column", False)
    return out


def deserialize_json(data: dict) -> IdMappingConfig:
    out: IdMappingConfig = {}  # type: ignore[typeddict-item]
    if "allowUseAsDimensionColumn" in data:
        out["allow_use_as_dimension_column"] = data["allowUseAsDimensionColumn"]
    else:
        out["allow_use_as_dimension_column"] = False
    return out
