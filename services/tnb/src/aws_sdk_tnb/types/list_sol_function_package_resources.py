"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionPackageResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_tnb.types.list_sol_function_package_info

ListSolFunctionPackageResources: TypeAlias = list[
    "aws_sdk_tnb.types.list_sol_function_package_info.ListSolFunctionPackageInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionPackageResources) -> list:
    import aws_sdk_tnb.types.list_sol_function_package_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_tnb.types.list_sol_function_package_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListSolFunctionPackageResources:
    import aws_sdk_tnb.types.list_sol_function_package_info

    out: ListSolFunctionPackageResources = []
    for item in data:
        out.append(
            aws_sdk_tnb.types.list_sol_function_package_info.deserialize_json(item)
        )
    return out
