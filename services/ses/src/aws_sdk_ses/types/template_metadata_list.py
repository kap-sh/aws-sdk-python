"""Generated from Smithy shape ``com.amazonaws.ses#TemplateMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.template_metadata

TemplateMetadataList: TypeAlias = list[
    "aws_sdk_ses.types.template_metadata.TemplateMetadata"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TemplateMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.template_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.template_metadata.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TemplateMetadataList:
    import aws_sdk_ses.types.template_metadata

    out: TemplateMetadataList = []
    for child in el.findall("member"):
        out.append(aws_sdk_ses.types.template_metadata.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TemplateMetadataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.template_metadata

    for n, item in enumerate(value, 1):
        aws_sdk_ses.types.template_metadata.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TemplateMetadataList:
    import aws_sdk_ses.types.template_metadata

    out: TemplateMetadataList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ses.types.template_metadata.deserialize_query(child))
    return out
