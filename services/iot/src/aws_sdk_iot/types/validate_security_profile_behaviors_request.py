"""Generated from Smithy shape ``com.amazonaws.iot#ValidateSecurityProfileBehaviorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.behaviors


class ValidateSecurityProfileBehaviorsRequest(TypedDict):
    behaviors: "aws_sdk_iot.types.behaviors.Behaviors"
    """<p>Specifies the behaviors that, when violated by a device (thing), cause an alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSecurityProfileBehaviorsRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.behaviors

    out["behaviors"] = aws_sdk_iot.types.behaviors.serialize_json(value["behaviors"])
    return out


def deserialize_json(data: dict) -> ValidateSecurityProfileBehaviorsRequest:
    out: ValidateSecurityProfileBehaviorsRequest = {}  # type: ignore[typeddict-item]
    if "behaviors" in data:
        import aws_sdk_iot.types.behaviors

        out["behaviors"] = aws_sdk_iot.types.behaviors.deserialize_json(
            data["behaviors"]
        )
    else:
        raise DeserializationError(
            "ValidateSecurityProfileBehaviorsRequest.behaviors required"
        )
    return out
