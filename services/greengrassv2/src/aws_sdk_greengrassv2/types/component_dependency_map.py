"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDependencyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_dependency_requirement
    import aws_sdk_greengrassv2.types.non_empty_string

ComponentDependencyMap: TypeAlias = dict[
    "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString",
    "aws_sdk_greengrassv2.types.component_dependency_requirement.ComponentDependencyRequirement",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentDependencyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_greengrassv2.types.component_dependency_requirement

        out[key] = (
            aws_sdk_greengrassv2.types.component_dependency_requirement.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentDependencyMap:
    out: ComponentDependencyMap = {}
    for key, value in data.items():
        import aws_sdk_greengrassv2.types.component_dependency_requirement

        out[key] = (
            aws_sdk_greengrassv2.types.component_dependency_requirement.deserialize_json(
                value
            )
        )
    return out
