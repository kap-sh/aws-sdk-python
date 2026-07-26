"""Generated from Smithy shape ``com.amazonaws.greengrass#GetThingRuntimeConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.runtime_configuration


class GetThingRuntimeConfigurationResponse(TypedDict, closed=True):
    runtime_configuration: NotRequired[
        "capo_greengrass.types.runtime_configuration.RuntimeConfiguration"
    ]
    """Runtime configuration for a thing."""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingRuntimeConfigurationResponse) -> dict:
    out: dict = {}
    if "runtime_configuration" in value:
        import capo_greengrass.types.runtime_configuration

        out["RuntimeConfiguration"] = (
            capo_greengrass.types.runtime_configuration.serialize_json(
                value["runtime_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetThingRuntimeConfigurationResponse:
    out: GetThingRuntimeConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "RuntimeConfiguration" in data:
        import capo_greengrass.types.runtime_configuration

        out["runtime_configuration"] = (
            capo_greengrass.types.runtime_configuration.deserialize_json(
                data["RuntimeConfiguration"]
            )
        )
    return out
