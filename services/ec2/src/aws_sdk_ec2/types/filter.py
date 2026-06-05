"""Generated from Smithy shape ``com.amazonaws.ec2#Filter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class Filter(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an <code>OR</code>, and the request returns all results that match any of the specified values.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Filter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_ec2_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    if el.find("Values") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["values"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "Values"
        )
    return out
