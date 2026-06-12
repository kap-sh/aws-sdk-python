"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.rule

Rules: TypeAlias = list["aws_sdk_elastic_load_balancing_v2.types.rule.Rule"]


# --- awsQuery ser/de ---
def serialize_query(value: Rules, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.rule

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.rule.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Rules:
    import aws_sdk_elastic_load_balancing_v2.types.rule

    out: Rules = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.rule.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: Rules, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.rule

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.rule.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> Rules:
    import aws_sdk_elastic_load_balancing_v2.types.rule

    out: Rules = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.rule.deserialize_query(child)
        )
    return out
