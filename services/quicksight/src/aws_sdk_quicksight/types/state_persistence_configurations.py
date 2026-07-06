"""Generated from Smithy shape ``com.amazonaws.quicksight#StatePersistenceConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class StatePersistenceConfigurations(TypedDict, closed=True):
    enabled: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>Determines if a Quick Sight dashboard's state persistence settings are turned on or off.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatePersistenceConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> StatePersistenceConfigurations:
    out: StatePersistenceConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
