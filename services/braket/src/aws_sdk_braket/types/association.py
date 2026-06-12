"""Generated from Smithy shape ``com.amazonaws.braket#Association``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_braket.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_braket.types.association_type
    import aws_sdk_braket.types.braket_resource_arn

class Association(TypedDict):
    arn: "aws_sdk_braket.types.braket_resource_arn.BraketResourceArn"
    """<p>The Amazon Braket resource arn.</p>"""
    type: "aws_sdk_braket.types.association_type.AssociationType"
    """<p>The association type for the specified Amazon Braket resource arn.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: Association) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Association.arn required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Association.type required")
    return out