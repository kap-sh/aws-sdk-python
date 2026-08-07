"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#HttpRequestMethodConditionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.list_of_string


class HttpRequestMethodConditionConfig(TypedDict, closed=True):
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The name of the request method. The maximum length is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.</p> <p>If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HttpRequestMethodConditionConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> HttpRequestMethodConditionConfig:
    out: HttpRequestMethodConditionConfig = {}  # type: ignore[typeddict-item]
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_values
            )
        )
    return out
