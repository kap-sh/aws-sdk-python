"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#QueryStringConditionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list


class QueryStringConditionConfig(TypedDict, closed=True):
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list.QueryStringKeyValuePairList"
    ]
    r"""<p>The key/value pairs or values to find in the query string. The maximum length of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal '*' or '?' character in a query string, you must escape these characters in <code>Values</code> using a '\' character.</p> <p>If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: QueryStringConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "values" in value:
        import capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list

        capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_query(el: Element) -> QueryStringConditionConfig:
    out: QueryStringConditionConfig = {}  # type: ignore[typeddict-item]
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list

        out["values"] = (
            capo_elastic_load_balancing_v2.types.query_string_key_value_pair_list.deserialize_query(
                child_values
            )
        )
    return out
