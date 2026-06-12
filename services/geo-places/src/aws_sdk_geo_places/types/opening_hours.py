"""Generated from Smithy shape ``com.amazonaws.geoplaces#OpeningHours``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.category_list
    import aws_sdk_geo_places.types.opening_hours_components_list
    import aws_sdk_geo_places.types.opening_hours_display_list
    import aws_sdk_geo_places.types.sensitive_boolean


class OpeningHours(TypedDict):
    display: NotRequired[
        "aws_sdk_geo_places.types.opening_hours_display_list.OpeningHoursDisplayList"
    ]
    """<p>List of opening hours in the format they are displayed in. This can vary by result and in most cases represents how the result uniquely formats their opening hours. </p>"""
    open_now: NotRequired["aws_sdk_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if the result/place is currently open. </p>"""
    components: NotRequired[
        "aws_sdk_geo_places.types.opening_hours_components_list.OpeningHoursComponentsList"
    ]
    """<p>Components of the opening hours object.</p>"""
    categories: NotRequired["aws_sdk_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong too.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpeningHours) -> dict:
    out: dict = {}
    if "display" in value:
        import aws_sdk_geo_places.types.opening_hours_display_list

        out["Display"] = (
            aws_sdk_geo_places.types.opening_hours_display_list.serialize_json(
                value["display"]
            )
        )
    if "open_now" in value:
        out["OpenNow"] = value["open_now"]
    if "components" in value:
        import aws_sdk_geo_places.types.opening_hours_components_list

        out["Components"] = (
            aws_sdk_geo_places.types.opening_hours_components_list.serialize_json(
                value["components"]
            )
        )
    if "categories" in value:
        import aws_sdk_geo_places.types.category_list

        out["Categories"] = aws_sdk_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> OpeningHours:
    out: OpeningHours = {}  # type: ignore[typeddict-item]
    if "Display" in data:
        import aws_sdk_geo_places.types.opening_hours_display_list

        out["display"] = (
            aws_sdk_geo_places.types.opening_hours_display_list.deserialize_json(
                data["Display"]
            )
        )
    if "OpenNow" in data:
        out["open_now"] = data["OpenNow"]
    if "Components" in data:
        import aws_sdk_geo_places.types.opening_hours_components_list

        out["components"] = (
            aws_sdk_geo_places.types.opening_hours_components_list.deserialize_json(
                data["Components"]
            )
        )
    if "Categories" in data:
        import aws_sdk_geo_places.types.category_list

        out["categories"] = aws_sdk_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    return out
