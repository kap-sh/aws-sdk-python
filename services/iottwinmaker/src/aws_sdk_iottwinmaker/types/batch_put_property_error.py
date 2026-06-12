"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.property_value_entry
    import aws_sdk_iottwinmaker.types.string


class BatchPutPropertyError(TypedDict):
    error_code: "aws_sdk_iottwinmaker.types.string.String"
    """<p>The error code.</p>"""
    error_message: "aws_sdk_iottwinmaker.types.string.String"
    """<p>The error message.</p>"""
    entry: "aws_sdk_iottwinmaker.types.property_value_entry.PropertyValueEntry"
    """<p>An object that contains information about errors returned by the <code>BatchPutProperty</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyError) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    import aws_sdk_iottwinmaker.types.property_value_entry

    out["entry"] = aws_sdk_iottwinmaker.types.property_value_entry.serialize_json(
        value["entry"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutPropertyError:
    out: BatchPutPropertyError = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("BatchPutPropertyError.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("BatchPutPropertyError.error_message required")
    if "entry" in data:
        import aws_sdk_iottwinmaker.types.property_value_entry

        out["entry"] = aws_sdk_iottwinmaker.types.property_value_entry.deserialize_json(
            data["entry"]
        )
    else:
        raise DeserializationError("BatchPutPropertyError.entry required")
    return out
