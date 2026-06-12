"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_tuple

TargetGroupList: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.target_group_tuple.TargetGroupTuple"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_tuple

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_group_tuple.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetGroupList:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_tuple

    out: TargetGroupList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_group_tuple.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TargetGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_tuple

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_group_tuple.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetGroupList:
    import aws_sdk_elastic_load_balancing_v2.types.target_group_tuple

    out: TargetGroupList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_group_tuple.deserialize_query(
                child
            )
        )
    return out
