"""Generated from Smithy shape ``com.amazonaws.iot#ValidateSecurityProfileBehaviorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.behaviors


class ValidateSecurityProfileBehaviorsRequest(TypedDict, closed=True):
    behaviors: "capo_iot.types.behaviors.Behaviors"
    """<p>Specifies the behaviors that, when violated by a device (thing), cause an alert.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateSecurityProfileBehaviorsRequest) -> dict:
    out: dict = {}
    import capo_iot.types.behaviors

    out["behaviors"] = capo_iot.types.behaviors.serialize_json(value["behaviors"])
    return out


def deserialize_json(data: dict) -> ValidateSecurityProfileBehaviorsRequest:
    out: ValidateSecurityProfileBehaviorsRequest = {}  # type: ignore[typeddict-item]
    if "behaviors" in data:
        import capo_iot.types.behaviors

        out["behaviors"] = capo_iot.types.behaviors.deserialize_json(data["behaviors"])
    else:
        raise DeserializationError(
            "ValidateSecurityProfileBehaviorsRequest.behaviors required"
        )
    return out
