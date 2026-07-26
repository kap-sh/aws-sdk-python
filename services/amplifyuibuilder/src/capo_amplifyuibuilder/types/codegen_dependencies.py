"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenDependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_dependency

CodegenDependencies: TypeAlias = list[
    "capo_amplifyuibuilder.types.codegen_dependency.CodegenDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenDependencies) -> list:
    import capo_amplifyuibuilder.types.codegen_dependency

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.codegen_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodegenDependencies:
    import capo_amplifyuibuilder.types.codegen_dependency

    out: CodegenDependencies = []
    for item in data:
        out.append(
            capo_amplifyuibuilder.types.codegen_dependency.deserialize_json(item)
        )
    return out
