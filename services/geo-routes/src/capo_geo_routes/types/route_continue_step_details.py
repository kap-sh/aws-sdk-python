"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteContinueStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string_list


class RouteContinueStepDetails(TypedDict, closed=True):
    intersection: "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteContinueStepDetails) -> dict:
    out: dict = {}
    import capo_geo_routes.types.localized_string_list

    out["Intersection"] = capo_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    return out


def deserialize_json(data: dict) -> RouteContinueStepDetails:
    out: RouteContinueStepDetails = {}  # type: ignore[typeddict-item]
    if "Intersection" in data:
        import capo_geo_routes.types.localized_string_list

        out["intersection"] = (
            capo_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError("RouteContinueStepDetails.intersection required")
    return out
