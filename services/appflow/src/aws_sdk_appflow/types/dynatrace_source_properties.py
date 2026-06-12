"""Generated from Smithy shape ``com.amazonaws.appflow#DynatraceSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class DynatraceSourceProperties(TypedDict):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Dynatrace flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> DynatraceSourceProperties:
    out: DynatraceSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("DynatraceSourceProperties.object required")
    return out
