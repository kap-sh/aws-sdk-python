"""Generated from Smithy shape ``com.amazonaws.redshift#InboundIntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.inbound_integration

InboundIntegrationList: TypeAlias = list[
    "aws_sdk_redshift.types.inbound_integration.InboundIntegration"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InboundIntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.inbound_integration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.inbound_integration.serialize_query(
            item, pairs, f"{prefix}.InboundIntegration.{n}"
        )


def deserialize_query(el: Element) -> InboundIntegrationList:
    import aws_sdk_redshift.types.inbound_integration

    out: InboundIntegrationList = []
    for child in el.findall("InboundIntegration"):
        out.append(aws_sdk_redshift.types.inbound_integration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: InboundIntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.inbound_integration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.inbound_integration.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InboundIntegrationList:
    import aws_sdk_redshift.types.inbound_integration

    out: InboundIntegrationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.inbound_integration.deserialize_query(child))
    return out
