"""Generated from Smithy shape ``com.amazonaws.ses#TemplateMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.template_metadata

TemplateMetadataList: TypeAlias = list[
    "capo_ses.types.template_metadata.TemplateMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.template_metadata

    for n, item in enumerate(value, 1):
        capo_ses.types.template_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TemplateMetadataList:
    import capo_ses.types.template_metadata

    out: TemplateMetadataList = []
    for child in el.findall("member"):
        out.append(capo_ses.types.template_metadata.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TemplateMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.template_metadata

    for n, item in enumerate(value, 1):
        capo_ses.types.template_metadata.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TemplateMetadataList:
    import capo_ses.types.template_metadata

    out: TemplateMetadataList = []
    for child in parent.findall(tag):
        out.append(capo_ses.types.template_metadata.deserialize_query(child))
    return out
