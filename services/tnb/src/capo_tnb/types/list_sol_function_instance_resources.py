"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstanceResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_tnb.types.list_sol_function_instance_info

ListSolFunctionInstanceResources: TypeAlias = list[
    "capo_tnb.types.list_sol_function_instance_info.ListSolFunctionInstanceInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstanceResources) -> list:
    import capo_tnb.types.list_sol_function_instance_info

    out: list = []
    for item in value:
        out.append(capo_tnb.types.list_sol_function_instance_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSolFunctionInstanceResources:
    import capo_tnb.types.list_sol_function_instance_info

    out: ListSolFunctionInstanceResources = []
    for item in data:
        out.append(
            capo_tnb.types.list_sol_function_instance_info.deserialize_json(item)
        )
    return out
