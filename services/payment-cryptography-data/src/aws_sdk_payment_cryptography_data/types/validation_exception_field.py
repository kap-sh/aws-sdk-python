"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ValidationExceptionField``."""

from typing import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError


class ValidationExceptionField(TypedDict):
    path: "str"
    """<p>The request was denied due to an invalid request error.</p>"""
    message: "str"
    """<p>The request was denied due to an invalid request error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("ValidationExceptionField.path required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ValidationExceptionField.message required")
    return out
