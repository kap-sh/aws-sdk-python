"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.attribute_identifier


class BatchPutAttributeOutput(TypedDict, closed=True):
    attribute_identifier: (
        "aws_sdk_datazone.types.attribute_identifier.AttributeIdentifier"
    )
    """<p>The attribute ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributeOutput) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    return out


def deserialize_json(data: dict) -> BatchPutAttributeOutput:
    out: BatchPutAttributeOutput = {}  # type: ignore[typeddict-item]
    if "attributeIdentifier" in data:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        raise DeserializationError(
            "BatchPutAttributeOutput.attribute_identifier required"
        )
    return out
