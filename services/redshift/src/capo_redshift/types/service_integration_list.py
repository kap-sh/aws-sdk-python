"""Generated from Smithy shape ``com.amazonaws.redshift#ServiceIntegrationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.service_integrations_union

ServiceIntegrationList: TypeAlias = list[
    "capo_redshift.types.service_integrations_union.ServiceIntegrationsUnion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceIntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.service_integrations_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.service_integrations_union.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServiceIntegrationList:
    import capo_redshift.types.service_integrations_union

    out: ServiceIntegrationList = []
    for child in el.findall("member"):
        out.append(
            capo_redshift.types.service_integrations_union.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: ServiceIntegrationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.service_integrations_union

    for n, item in enumerate(value, 1):
        capo_redshift.types.service_integrations_union.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServiceIntegrationList:
    import capo_redshift.types.service_integrations_union

    out: ServiceIntegrationList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.service_integrations_union.deserialize_query(child)
        )
    return out
