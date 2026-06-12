"""Generated from Smithy shape ``com.amazonaws.autoscaling#TagDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.tag_description

TagDescriptionList: TypeAlias = list[
    "aws_sdk_auto_scaling.types.tag_description.TagDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.tag_description

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.tag_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TagDescriptionList:
    import aws_sdk_auto_scaling.types.tag_description

    out: TagDescriptionList = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.tag_description.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TagDescriptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.tag_description

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.tag_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TagDescriptionList:
    import aws_sdk_auto_scaling.types.tag_description

    out: TagDescriptionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.tag_description.deserialize_query(child))
    return out
