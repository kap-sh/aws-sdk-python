"""Generated from Smithy shape ``com.amazonaws.connect#PropertyValidationExceptionProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.message
    import aws_sdk_connect.types.property_validation_exception_reason
    import aws_sdk_connect.types.string


class PropertyValidationExceptionProperty(TypedDict, closed=True):
    property_path: "aws_sdk_connect.types.string.String"
    """<p>The full property path.</p>"""
    reason: "aws_sdk_connect.types.property_validation_exception_reason.PropertyValidationExceptionReason"
    """<p>Why the property is not valid.</p>"""
    message: "aws_sdk_connect.types.message.Message"
    """<p>A message describing why the property is not valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValidationExceptionProperty) -> dict:
    out: dict = {}
    out["PropertyPath"] = value["property_path"]
    import aws_sdk_connect.types.property_validation_exception_reason

    out["Reason"] = (
        aws_sdk_connect.types.property_validation_exception_reason.serialize_json(
            value["reason"]
        )
    )
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PropertyValidationExceptionProperty:
    out: PropertyValidationExceptionProperty = {}  # type: ignore[typeddict-item]
    if "PropertyPath" in data:
        out["property_path"] = data["PropertyPath"]
    else:
        raise DeserializationError(
            "PropertyValidationExceptionProperty.property_path required"
        )
    if "Reason" in data:
        import aws_sdk_connect.types.property_validation_exception_reason

        out["reason"] = (
            aws_sdk_connect.types.property_validation_exception_reason.deserialize_json(
                data["Reason"]
            )
        )
    else:
        raise DeserializationError(
            "PropertyValidationExceptionProperty.reason required"
        )
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError(
            "PropertyValidationExceptionProperty.message required"
        )
    return out
