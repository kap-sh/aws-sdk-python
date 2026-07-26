"""Generated from Smithy shape ``com.amazonaws.neptune#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.filter_value_list
    import capo_neptune.types.string


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_neptune.types.string.String"]
    """<p>This parameter is not currently supported.</p>"""
    values: NotRequired["capo_neptune.types.filter_value_list.FilterValueList"]
    """<p>This parameter is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Filter, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "values" in value:
        import capo_neptune.types.filter_value_list

        capo_neptune.types.filter_value_list.serialize_query(
            value["values"], pairs, f"{prefix}.Values"
        )


def deserialize_query(el: Element) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_neptune.types.filter_value_list

        out["values"] = capo_neptune.types.filter_value_list.deserialize_query(
            child_values
        )
    return out
