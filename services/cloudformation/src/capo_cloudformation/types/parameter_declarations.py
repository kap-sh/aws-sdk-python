"""Generated from Smithy shape ``com.amazonaws.cloudformation#ParameterDeclarations``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.parameter_declaration

ParameterDeclarations: TypeAlias = list[
    "capo_cloudformation.types.parameter_declaration.ParameterDeclaration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ParameterDeclarations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.parameter_declaration

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.parameter_declaration.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ParameterDeclarations:
    import capo_cloudformation.types.parameter_declaration

    out: ParameterDeclarations = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.parameter_declaration.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ParameterDeclarations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.parameter_declaration

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.parameter_declaration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ParameterDeclarations:
    import capo_cloudformation.types.parameter_declaration

    out: ParameterDeclarations = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.parameter_declaration.deserialize_query(child)
        )
    return out
