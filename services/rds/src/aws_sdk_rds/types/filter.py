"""Generated from Smithy shape ``com.amazonaws.rds#Filter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_value_list
    import aws_sdk_rds.types.string


class Filter(TypedDict):
    name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired["aws_sdk_rds.types.filter_value_list.FilterValueList"]
    """<p>One or more filter values. Filter values are case-sensitive.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Filter, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import aws_sdk_rds.types.filter_value_list

        aws_sdk_rds.types.filter_value_list.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import aws_sdk_rds.types.filter_value_list

        out["values"] = aws_sdk_rds.types.filter_value_list.deserialize_query(
            child_values
        )
    return out
