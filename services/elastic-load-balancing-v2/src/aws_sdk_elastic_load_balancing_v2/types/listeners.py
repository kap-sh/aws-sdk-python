"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Listeners``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listener

Listeners: TypeAlias = list["aws_sdk_elastic_load_balancing_v2.types.listener.Listener"]


# --- awsQuery ser/de ---
def serialize_query(
    value: Listeners, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.listener

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.listener.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Listeners:
    import aws_sdk_elastic_load_balancing_v2.types.listener

    out: Listeners = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.listener.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: Listeners, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.listener

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.listener.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Listeners:
    import aws_sdk_elastic_load_balancing_v2.types.listener

    out: Listeners = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.listener.deserialize_query(child)
        )
    return out
