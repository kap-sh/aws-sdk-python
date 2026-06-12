"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SslPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy

SslPolicies: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.ssl_policy.SslPolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SslPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.ssl_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SslPolicies:
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy

    out: SslPolicies = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.ssl_policy.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: SslPolicies, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.ssl_policy.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SslPolicies:
    import aws_sdk_elastic_load_balancing_v2.types.ssl_policy

    out: SslPolicies = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.ssl_policy.deserialize_query(child)
        )
    return out
