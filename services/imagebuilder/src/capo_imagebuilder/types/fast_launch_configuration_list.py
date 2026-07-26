"""Generated from Smithy shape ``com.amazonaws.imagebuilder#FastLaunchConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.fast_launch_configuration

FastLaunchConfigurationList: TypeAlias = list[
    "capo_imagebuilder.types.fast_launch_configuration.FastLaunchConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FastLaunchConfigurationList) -> list:
    import capo_imagebuilder.types.fast_launch_configuration

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.fast_launch_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FastLaunchConfigurationList:
    import capo_imagebuilder.types.fast_launch_configuration

    out: FastLaunchConfigurationList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.fast_launch_configuration.deserialize_json(item)
        )
    return out
