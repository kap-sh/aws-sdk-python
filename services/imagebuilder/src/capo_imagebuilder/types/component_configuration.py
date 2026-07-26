"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_parameter_list
    import capo_imagebuilder.types.component_version_arn_or_build_version_arn


class ComponentConfiguration(TypedDict, closed=True):
    component_arn: "capo_imagebuilder.types.component_version_arn_or_build_version_arn.ComponentVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
    parameters: NotRequired[
        "capo_imagebuilder.types.component_parameter_list.ComponentParameterList"
    ]
    """<p>A group of parameter settings that Image Builder uses to configure the component for a specific recipe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentConfiguration) -> dict:
    out: dict = {}
    out["componentArn"] = value["component_arn"]
    if "parameters" in value:
        import capo_imagebuilder.types.component_parameter_list

        out["parameters"] = (
            capo_imagebuilder.types.component_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentConfiguration:
    out: ComponentConfiguration = {}  # type: ignore[typeddict-item]
    if "componentArn" in data:
        out["component_arn"] = data["componentArn"]
    else:
        raise DeserializationError("ComponentConfiguration.component_arn required")
    if "parameters" in data:
        import capo_imagebuilder.types.component_parameter_list

        out["parameters"] = (
            capo_imagebuilder.types.component_parameter_list.deserialize_json(
                data["parameters"]
            )
        )
    return out
