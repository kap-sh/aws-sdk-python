"""Generated from Smithy shape ``com.amazonaws.geoplaces#ContactDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.category_list
    import aws_sdk_geo_places.types.sensitive_string


class ContactDetails(TypedDict, closed=True):
    label: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The contact's label.</p>"""
    value: NotRequired["aws_sdk_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The contact's value.</p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong too.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactDetails) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "value" in value:
        out["Value"] = value["value"]
    if "categories" in value:
        import aws_sdk_geo_places.types.category_list

        out["Categories"] = aws_sdk_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> ContactDetails:
    out: ContactDetails = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Categories" in data:
        import aws_sdk_geo_places.types.category_list

        out["categories"] = aws_sdk_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    return out
