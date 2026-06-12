"""Generated from Smithy shape ``com.amazonaws.redshift#EndpointAuthorizations``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.endpoint_authorization

EndpointAuthorizations: TypeAlias = list[
    "aws_sdk_redshift.types.endpoint_authorization.EndpointAuthorization"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EndpointAuthorizations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.endpoint_authorization

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.endpoint_authorization.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EndpointAuthorizations:
    import aws_sdk_redshift.types.endpoint_authorization

    out: EndpointAuthorizations = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_redshift.types.endpoint_authorization.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: EndpointAuthorizations, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.endpoint_authorization

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.endpoint_authorization.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EndpointAuthorizations:
    import aws_sdk_redshift.types.endpoint_authorization

    out: EndpointAuthorizations = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.endpoint_authorization.deserialize_query(child)
        )
    return out
