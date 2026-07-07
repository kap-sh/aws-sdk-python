"""Generated from Smithy shape ``com.amazonaws.entityresolution#FailedRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.error_message
    import aws_sdk_entityresolution.types.input_source_arn


class FailedRecord(TypedDict, closed=True):
    input_source_arn: "aws_sdk_entityresolution.types.input_source_arn.InputSourceARN"
    """<p> The input source ARN of the record that didn't generate a Match ID.</p>"""
    unique_id: "str"
    """<p> The unique ID of the record that didn't generate a Match ID.</p>"""
    error_message: "aws_sdk_entityresolution.types.error_message.ErrorMessage"
    """<p> The error message for the record that didn't generate a Match ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedRecord) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["uniqueId"] = value["unique_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedRecord:
    out: FailedRecord = {}  # type: ignore[typeddict-item]
    if "inputSourceARN" in data:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        raise DeserializationError("FailedRecord.input_source_arn required")
    if "uniqueId" in data:
        out["unique_id"] = data["uniqueId"]
    else:
        raise DeserializationError("FailedRecord.unique_id required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("FailedRecord.error_message required")
    return out
