"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.filter_name
    import capo_imagebuilder.types.filter_values


class Filter(TypedDict, closed=True):
    name: NotRequired["capo_imagebuilder.types.filter_name.FilterName"]
    """<p>The name of the filter. Filter names are case-sensitive.</p>"""
    values: NotRequired["capo_imagebuilder.types.filter_values.FilterValues"]
    """<p>The filter values. Filter values are case-sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "values" in value:
        import capo_imagebuilder.types.filter_values

        out["values"] = capo_imagebuilder.types.filter_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "values" in data:
        import capo_imagebuilder.types.filter_values

        out["values"] = capo_imagebuilder.types.filter_values.deserialize_json(
            data["values"]
        )
    return out
