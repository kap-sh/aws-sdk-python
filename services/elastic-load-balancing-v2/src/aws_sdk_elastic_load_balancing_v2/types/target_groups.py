"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_group

TargetGroups: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.target_group.TargetGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_group

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetGroups:
    import aws_sdk_elastic_load_balancing_v2.types.target_group

    out: TargetGroups = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_group.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TargetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_group

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetGroups:
    import aws_sdk_elastic_load_balancing_v2.types.target_group

    out: TargetGroups = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_group.deserialize_query(
                child
            )
        )
    return out
