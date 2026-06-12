"""Generated from Smithy shape ``com.amazonaws.greengrass#GetThingRuntimeConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetThingRuntimeConfigurationRequest(TypedDict):
    thing_name: "aws_sdk_greengrass.types.__string.__string"
    """The thing name."""


# --- restJson1 ser/de ---
def serialize_json(value: GetThingRuntimeConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetThingRuntimeConfigurationRequest:
    out: GetThingRuntimeConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
