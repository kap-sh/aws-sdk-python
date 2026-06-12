"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDeploymentSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_deployment_specification
    import aws_sdk_greengrassv2.types.non_empty_string

ComponentDeploymentSpecifications: TypeAlias = dict[
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
    "aws_sdk_greengrassv2.types.component_deployment_specification.ComponentDeploymentSpecification",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentDeploymentSpecifications) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_greengrassv2.types.component_deployment_specification

        out[key] = (
            aws_sdk_greengrassv2.types.component_deployment_specification.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentDeploymentSpecifications:
    out: ComponentDeploymentSpecifications = {}
    for key, value in data.items():
        import aws_sdk_greengrassv2.types.component_deployment_specification

        out[key] = (
            aws_sdk_greengrassv2.types.component_deployment_specification.deserialize_json(
                value
            )
        )
    return out
