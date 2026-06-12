"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_supplychain.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_supplychain.types.instance

class CreateInstanceResponse(TypedDict):
    instance: "aws_sdk_supplychain.types.instance.Instance"
    """<p>The AWS Supply Chain instance resource data details.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateInstanceResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.instance
    out["instance"] = aws_sdk_supplychain.types.instance.serialize_json(value["instance"])
    return out


def deserialize_json(data: dict) -> CreateInstanceResponse:
    out: CreateInstanceResponse = {}  # type: ignore[typeddict-item]
    if "instance" in data:
        import aws_sdk_supplychain.types.instance
        out["instance"] = aws_sdk_supplychain.types.instance.deserialize_json(data["instance"])
    else:
        raise DeserializationError("CreateInstanceResponse.instance required")
    return out