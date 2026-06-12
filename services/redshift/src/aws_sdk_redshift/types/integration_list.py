"""Generated from Smithy shape ``com.amazonaws.redshift#IntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integration

IntegrationList: TypeAlias = list["aws_sdk_redshift.types.integration.Integration"]


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.integration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.integration.serialize_query(
            item, pairs, f"{prefix}.Integration.{n}"
        )


def deserialize_query(el: Element) -> IntegrationList:
    import aws_sdk_redshift.types.integration

    out: IntegrationList = []
    for child in el.findall("Integration"):
        out.append(aws_sdk_redshift.types.integration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.integration

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.integration.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> IntegrationList:
    import aws_sdk_redshift.types.integration

    out: IntegrationList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.integration.deserialize_query(child))
    return out
