"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ErrorMessageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.error_message_type


class ErrorMessageConfiguration(TypedDict, closed=True):
    type: "aws_sdk_cleanrooms.types.error_message_type.ErrorMessageType"
    """<p>The level of detail for error messages returned by the PySpark job. When set to DETAILED, error messages include more information to help troubleshoot issues with your PySpark job.</p> <p>Because this setting may expose sensitive data, it is recommended for development and testing environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorMessageConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.error_message_type

    out["type"] = aws_sdk_cleanrooms.types.error_message_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> ErrorMessageConfiguration:
    out: ErrorMessageConfiguration = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_cleanrooms.types.error_message_type

        out["type"] = aws_sdk_cleanrooms.types.error_message_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ErrorMessageConfiguration.type required")
    return out
