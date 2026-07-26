"""Generated from Smithy shape ``com.amazonaws.cloudformation#TemplateParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.template_parameter

TemplateParameters: TypeAlias = list[
    "capo_cloudformation.types.template_parameter.TemplateParameter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateParameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.template_parameter

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.template_parameter.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TemplateParameters:
    import capo_cloudformation.types.template_parameter

    out: TemplateParameters = []
    for child in el.findall("member"):
        out.append(
            capo_cloudformation.types.template_parameter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: TemplateParameters, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudformation.types.template_parameter

    for n, item in enumerate(value, 1):
        capo_cloudformation.types.template_parameter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TemplateParameters:
    import capo_cloudformation.types.template_parameter

    out: TemplateParameters = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudformation.types.template_parameter.deserialize_query(child)
        )
    return out
