"""Generated from Smithy shape ``com.amazonaws.sns#ListOfEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_sns._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_sns.types.endpoint

ListOfEndpoints: TypeAlias = list["aws_sdk_sns.types.endpoint.Endpoint"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOfEndpoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.endpoint

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.endpoint.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> ListOfEndpoints:
    import aws_sdk_sns.types.endpoint

    out: ListOfEndpoints = []
    for child in el.findall("member"):
        out.append(aws_sdk_sns.types.endpoint.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ListOfEndpoints, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_sns.types.endpoint

    for n, item in enumerate(value, 1):
        aws_sdk_sns.types.endpoint.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ListOfEndpoints:
    import aws_sdk_sns.types.endpoint

    out: ListOfEndpoints = []
    for child in parent.findall(tag):
        out.append(aws_sdk_sns.types.endpoint.deserialize_query(child))
    return out
