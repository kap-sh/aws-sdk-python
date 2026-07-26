"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeIntegrationsFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.describe_integrations_filter

DescribeIntegrationsFilterList: TypeAlias = list[
    "capo_redshift.types.describe_integrations_filter.DescribeIntegrationsFilter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIntegrationsFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.describe_integrations_filter

    for n, item in enumerate(value, 1):
        capo_redshift.types.describe_integrations_filter.serialize_query(
            item, pairs, f"{prefix}.DescribeIntegrationsFilter.{n}"
        )


def deserialize_query(el: Element) -> DescribeIntegrationsFilterList:
    import capo_redshift.types.describe_integrations_filter

    out: DescribeIntegrationsFilterList = []
    for child in el.findall("DescribeIntegrationsFilter"):
        out.append(
            capo_redshift.types.describe_integrations_filter.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DescribeIntegrationsFilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.describe_integrations_filter

    for n, item in enumerate(value, 1):
        capo_redshift.types.describe_integrations_filter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DescribeIntegrationsFilterList:
    import capo_redshift.types.describe_integrations_filter

    out: DescribeIntegrationsFilterList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.describe_integrations_filter.deserialize_query(child)
        )
    return out
