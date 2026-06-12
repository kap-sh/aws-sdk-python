"""Generated from Smithy shape ``com.amazonaws.cloudformation#ResourceMappings``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.resource_mapping

ResourceMappings: TypeAlias = list[
    "aws_sdk_cloudformation.types.resource_mapping.ResourceMapping"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_mapping

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_mapping.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ResourceMappings:
    import aws_sdk_cloudformation.types.resource_mapping

    out: ResourceMappings = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_cloudformation.types.resource_mapping.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ResourceMappings, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.resource_mapping

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.resource_mapping.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ResourceMappings:
    import aws_sdk_cloudformation.types.resource_mapping

    out: ResourceMappings = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_cloudformation.types.resource_mapping.deserialize_query(child)
        )
    return out
