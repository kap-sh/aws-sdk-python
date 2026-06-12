"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#TagDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.tag_description

TagDescriptions: TypeAlias = list[
    "aws_sdk_elastic_load_balancing.types.tag_description.TagDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TagDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.tag_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.tag_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TagDescriptions:
    import aws_sdk_elastic_load_balancing.types.tag_description

    out: TagDescriptions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing.types.tag_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TagDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing.types.tag_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing.types.tag_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TagDescriptions:
    import aws_sdk_elastic_load_balancing.types.tag_description

    out: TagDescriptions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing.types.tag_description.deserialize_query(
                child
            )
        )
    return out
