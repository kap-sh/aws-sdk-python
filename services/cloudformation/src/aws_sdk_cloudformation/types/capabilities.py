"""Generated from Smithy shape ``com.amazonaws.cloudformation#Capabilities``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.capability

Capabilities: TypeAlias = list["aws_sdk_cloudformation.types.capability.Capability"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Capabilities, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.capability

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.capability.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Capabilities:
    import aws_sdk_cloudformation.types.capability

    out: Capabilities = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudformation.types.capability.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Capabilities, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudformation.types.capability

    for n, item in enumerate(value, 1):
        aws_sdk_cloudformation.types.capability.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Capabilities:
    import aws_sdk_cloudformation.types.capability

    out: Capabilities = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudformation.types.capability.deserialize_query(child))
    return out
