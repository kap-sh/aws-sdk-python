"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#PathPatternConditionConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.list_of_string


class PathPatternConditionConfig(TypedDict):
    values: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The path patterns to compare against the request URL. The maximum length of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).</p> <p>If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a <a href=\"https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#query-string-conditions\">query string condition</a>.</p>"""
    regex_values: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The regular expressions to compare against the request URL. The maximum length of each string is 128 characters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PathPatternConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "values" in value:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_string

        aws_sdk_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )
    if "regex_values" in value:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_string

        aws_sdk_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["regex_values"], pairs, f"{prefix}.RegexValues"
        )


def deserialize_query(el: Element) -> PathPatternConditionConfig:
    out: PathPatternConditionConfig = {}  # type: ignore[typeddict-item]
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_string

        out["values"] = (
            aws_sdk_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_values
            )
        )
    child_regex_values = el.find("RegexValues")
    if child_regex_values is not None:
        import aws_sdk_elastic_load_balancing_v2.types.list_of_string

        out["regex_values"] = (
            aws_sdk_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_regex_values
            )
        )
    return out
