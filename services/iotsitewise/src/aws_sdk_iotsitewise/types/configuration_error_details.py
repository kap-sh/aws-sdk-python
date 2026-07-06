"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.error_code
    import aws_sdk_iotsitewise.types.error_message


class ConfigurationErrorDetails(TypedDict, closed=True):
    code: "aws_sdk_iotsitewise.types.error_code.ErrorCode"
    """<p>The error code.</p>"""
    message: "aws_sdk_iotsitewise.types.error_message.ErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationErrorDetails) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.error_code

    out["code"] = aws_sdk_iotsitewise.types.error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConfigurationErrorDetails:
    out: ConfigurationErrorDetails = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_iotsitewise.types.error_code

        out["code"] = aws_sdk_iotsitewise.types.error_code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("ConfigurationErrorDetails.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConfigurationErrorDetails.message required")
    return out
