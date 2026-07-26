"""Generated from Smithy shape ``com.amazonaws.rds#IntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integration

IntegrationList: TypeAlias = list["capo_rds.types.integration.Integration"]


# --- awsQuery ser/de ---
def serialize_query(
    value: IntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.integration

    for n, item in enumerate(value, 1):
        capo_rds.types.integration.serialize_query(
            item, pairs, f"{prefix}.Integration.{n}"
        )


def deserialize_query(el: Element) -> IntegrationList:
    import capo_rds.types.integration

    out: IntegrationList = []
    for child in el.findall("Integration"):
        out.append(capo_rds.types.integration.deserialize_query(child))
    return out


def serialize_query_flat(
    value: IntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.integration

    for n, item in enumerate(value, 1):
        capo_rds.types.integration.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> IntegrationList:
    import capo_rds.types.integration

    out: IntegrationList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.integration.deserialize_query(child))
    return out
