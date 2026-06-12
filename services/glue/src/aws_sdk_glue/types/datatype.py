"""Generated from Smithy shape ``com.amazonaws.glue#Datatype``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_limited_string


class Datatype(TypedDict):
    id: "aws_sdk_glue.types.generic_limited_string.GenericLimitedString"
    """<p>The datatype of the value.</p>"""
    label: "aws_sdk_glue.types.generic_limited_string.GenericLimitedString"
    """<p>A label assigned to the datatype.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datatype) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Datatype:
    out: Datatype = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Datatype.id required")
    if "Label" in data:
        out["label"] = data["Label"]
    else:
        raise DeserializationError("Datatype.label required")
    return out
