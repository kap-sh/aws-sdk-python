"""Generated from Smithy shape ``com.amazonaws.redshift#VpcEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.vpc_endpoint

VpcEndpointsList: TypeAlias = list["aws_sdk_redshift.types.vpc_endpoint.VpcEndpoint"]


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.vpc_endpoint

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.vpc_endpoint.serialize_query(
            item, pairs, f"{prefix}.VpcEndpoint.{n}"
        )


def deserialize_query(el: Element) -> VpcEndpointsList:
    import aws_sdk_redshift.types.vpc_endpoint

    out: VpcEndpointsList = []
    for child in el.findall("VpcEndpoint"):
        out.append(aws_sdk_redshift.types.vpc_endpoint.deserialize_query(child))
    return out


def serialize_query_flat(
    value: VpcEndpointsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.vpc_endpoint

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.vpc_endpoint.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> VpcEndpointsList:
    import aws_sdk_redshift.types.vpc_endpoint

    out: VpcEndpointsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.vpc_endpoint.deserialize_query(child))
    return out
