"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#QueryStringKeyValuePairList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair

QueryStringKeyValuePairList: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair.QueryStringKeyValuePair"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: QueryStringKeyValuePairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> QueryStringKeyValuePairList:
    import aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair

    out: QueryStringKeyValuePairList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: QueryStringKeyValuePairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair

    for n, item in enumerate(value, 1):
        aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> QueryStringKeyValuePairList:
    import aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair

    out: QueryStringKeyValuePairList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elastic_load_balancing_v2.types.query_string_key_value_pair.deserialize_query(
                child
            )
        )
    return out
