"""Generated from Smithy shape ``com.amazonaws.appflow#HoneycodeDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.object


class HoneycodeDestinationProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Amazon Honeycode flow destination. </p>"""
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: HoneycodeDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "error_handling_config" in value:
        import capo_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            capo_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HoneycodeDestinationProperties:
    out: HoneycodeDestinationProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("HoneycodeDestinationProperties.object required")
    if "errorHandlingConfig" in data:
        import capo_appflow.types.error_handling_config

        out["error_handling_config"] = (
            capo_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    return out
