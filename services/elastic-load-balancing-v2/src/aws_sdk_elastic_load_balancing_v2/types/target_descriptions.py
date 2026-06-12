"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.target_description

TargetDescriptions: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.target_description.TargetDescription"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_description.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetDescriptions:
    import aws_sdk_elastic_load_balancing_v2.types.target_description

    out: TargetDescriptions = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_description.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TargetDescriptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.target_description

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.target_description.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> TargetDescriptions:
    import aws_sdk_elastic_load_balancing_v2.types.target_description

    out: TargetDescriptions = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.target_description.deserialize_query(
                child
            )
        )
    return out
