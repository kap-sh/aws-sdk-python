"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.dimension_value


class Dimension(TypedDict, closed=True):
    value: "capo_network_firewall.types.dimension_value.DimensionValue"
    """<p>The value to use in the custom metric dimension.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Dimension.value required")
    return out
