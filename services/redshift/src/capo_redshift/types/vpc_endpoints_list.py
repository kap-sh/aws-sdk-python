"""Generated from Smithy shape ``com.amazonaws.redshift#VpcEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.vpc_endpoint

VpcEndpointsList: TypeAlias = list["capo_redshift.types.vpc_endpoint.VpcEndpoint"]


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.vpc_endpoint

    for n, item in enumerate(value, 1):
        capo_redshift.types.vpc_endpoint.serialize_query(
            item, pairs, f"{prefix}.VpcEndpoint.{n}"
        )


def deserialize_query(el: Element) -> VpcEndpointsList:
    import capo_redshift.types.vpc_endpoint

    out: VpcEndpointsList = []
    for child in el.findall("VpcEndpoint"):
        out.append(capo_redshift.types.vpc_endpoint.deserialize_query(child))
    return out


def serialize_query_flat(
    value: VpcEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.vpc_endpoint

    for n, item in enumerate(value, 1):
        capo_redshift.types.vpc_endpoint.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> VpcEndpointsList:
    import capo_redshift.types.vpc_endpoint

    out: VpcEndpointsList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.vpc_endpoint.deserialize_query(child))
    return out
