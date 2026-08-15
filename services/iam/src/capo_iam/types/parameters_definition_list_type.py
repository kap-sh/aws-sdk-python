"""Generated from Smithy shape ``com.amazonaws.iam#parametersDefinitionListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.parameter_definition

parametersDefinitionListType: TypeAlias = list[
    "capo_iam.types.parameter_definition.ParameterDefinition"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: parametersDefinitionListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.parameter_definition

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.parameter_definition.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> parametersDefinitionListType:
    import capo_iam.types.parameter_definition

    out: parametersDefinitionListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.parameter_definition.deserialize_query(child))
    return out


def serialize_query_flat(
    value: parametersDefinitionListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.parameter_definition

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.parameter_definition.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> parametersDefinitionListType:
    import capo_iam.types.parameter_definition

    out: parametersDefinitionListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.parameter_definition.deserialize_query(child))
    return out
