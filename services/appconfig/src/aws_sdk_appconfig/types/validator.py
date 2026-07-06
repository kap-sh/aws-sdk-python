"""Generated from Smithy shape ``com.amazonaws.appconfig#Validator``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.string_with_length_between0_and32768
    import aws_sdk_appconfig.types.validator_type


class Validator(TypedDict, closed=True):
    type: "aws_sdk_appconfig.types.validator_type.ValidatorType"
    """<p>AppConfig supports validators of type <code>JSON_SCHEMA</code> and <code>LAMBDA</code> </p>"""
    content: "aws_sdk_appconfig.types.string_with_length_between0_and32768.StringWithLengthBetween0And32768"
    """<p>Either the JSON Schema content or the Amazon Resource Name (ARN) of an Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Validator) -> dict:
    out: dict = {}
    import aws_sdk_appconfig.types.validator_type

    out["Type"] = aws_sdk_appconfig.types.validator_type.serialize_json(value["type"])
    out["Content"] = value["content"]
    return out


def deserialize_json(data: dict) -> Validator:
    out: Validator = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_appconfig.types.validator_type

        out["type"] = aws_sdk_appconfig.types.validator_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("Validator.type required")
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("Validator.content required")
    return out
