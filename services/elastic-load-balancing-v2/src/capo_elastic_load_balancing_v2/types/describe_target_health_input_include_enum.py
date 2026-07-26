"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeTargetHealthInputIncludeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

DescribeTargetHealthInputIncludeEnum: TypeAlias = Literal[
    "AnomalyDetection",
    "All",
]


# --- awsQuery ser/de ---
def to_query_text(value: DescribeTargetHealthInputIncludeEnum) -> str:
    return value


def from_query_text(text: str) -> DescribeTargetHealthInputIncludeEnum:
    return cast(DescribeTargetHealthInputIncludeEnum, text)


def serialize_query(
    value: DescribeTargetHealthInputIncludeEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DescribeTargetHealthInputIncludeEnum:
    return from_query_text(el.text or "")
