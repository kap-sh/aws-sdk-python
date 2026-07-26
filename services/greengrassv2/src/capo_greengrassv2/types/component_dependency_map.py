"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDependencyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.component_dependency_requirement
    import capo_greengrassv2.types.non_empty_string

ComponentDependencyMap: TypeAlias = dict[
    "capo_greengrassv2.types.non_empty_string.NonEmptyString",
    "capo_greengrassv2.types.component_dependency_requirement.ComponentDependencyRequirement",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComponentDependencyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_greengrassv2.types.component_dependency_requirement

        out[key] = (
            capo_greengrassv2.types.component_dependency_requirement.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComponentDependencyMap:
    out: ComponentDependencyMap = {}
    for key, value in data.items():
        import capo_greengrassv2.types.component_dependency_requirement

        out[key] = (
            capo_greengrassv2.types.component_dependency_requirement.deserialize_json(
                value
            )
        )
    return out
