"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ListOfDescribeTargetHealthIncludeOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum

ListOfDescribeTargetHealthIncludeOptions: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum.DescribeTargetHealthInputIncludeEnum"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ListOfDescribeTargetHealthIncludeOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ListOfDescribeTargetHealthIncludeOptions:
    import capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum

    out: ListOfDescribeTargetHealthIncludeOptions = []
    for child in el.findall("member"):
        out.append(
            capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ListOfDescribeTargetHealthIncludeOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum

    for n, item in enumerate(value, 1):
        capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ListOfDescribeTargetHealthIncludeOptions:
    import capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum

    out: ListOfDescribeTargetHealthIncludeOptions = []
    for child in parent.findall(tag):
        out.append(
            capo_elastic_load_balancing_v2.types.describe_target_health_input_include_enum.deserialize_query(
                child
            )
        )
    return out
