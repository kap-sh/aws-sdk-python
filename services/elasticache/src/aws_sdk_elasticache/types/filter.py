"""Generated from Smithy shape ``com.amazonaws.elasticache#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.filter_name
    import aws_sdk_elasticache.types.filter_value_list


class Filter(TypedDict):
    name: NotRequired["aws_sdk_elasticache.types.filter_name.FilterName"]
    """<p>The property being filtered. For example, UserId.</p>"""
    values: NotRequired["aws_sdk_elasticache.types.filter_value_list.FilterValueList"]
    """<p>The property values to filter on. For example, \"user-123\".</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Filter, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import aws_sdk_elasticache.types.filter_value_list

        aws_sdk_elasticache.types.filter_value_list.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_elasticache.types.filter_value_list

        out["values"] = aws_sdk_elasticache.types.filter_value_list.deserialize_query(
            child_values
        )
    return out
