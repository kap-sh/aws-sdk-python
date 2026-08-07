"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.search_filter_attribute
    import capo_elastic_beanstalk.types.search_filter_operator
    import capo_elastic_beanstalk.types.search_filter_values


class SearchFilter(TypedDict, closed=True):
    attribute: NotRequired[
        "capo_elastic_beanstalk.types.search_filter_attribute.SearchFilterAttribute"
    ]
    """<p>The result attribute to which the filter values are applied. Valid values vary by API action.</p>"""
    operator: NotRequired[
        "capo_elastic_beanstalk.types.search_filter_operator.SearchFilterOperator"
    ]
    """<p>The operator to apply to the <code>Attribute</code> with each of the <code>Values</code>. Valid values vary by <code>Attribute</code>.</p>"""
    values: NotRequired[
        "capo_elastic_beanstalk.types.search_filter_values.SearchFilterValues"
    ]
    """<p>The list of values applied to the <code>Attribute</code> and <code>Operator</code> attributes. Number of values and valid values vary by <code>Attribute</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SearchFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attribute" in value:
        pairs.append((f"{key_prefix}Attribute", str(value["attribute"])))
    if "operator" in value:
        pairs.append((f"{key_prefix}Operator", str(value["operator"])))
    if "values" in value:
        import capo_elastic_beanstalk.types.search_filter_values

        capo_elastic_beanstalk.types.search_filter_values.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    child_attribute = el.find("Attribute")
    if child_attribute is not None:
        out["attribute"] = str(child_attribute.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        out["operator"] = str(child_operator.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_beanstalk.types.search_filter_values

        out["values"] = (
            capo_elastic_beanstalk.types.search_filter_values.deserialize_query(
                child_values
            )
        )
    return out
