"""Generated from Smithy shape ``com.amazonaws.appflow#SingularSourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.object


class SingularSourceProperties(TypedDict):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Singular flow source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingularSourceProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    return out


def deserialize_json(data: dict) -> SingularSourceProperties:
    out: SingularSourceProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("SingularSourceProperties.object required")
    return out
