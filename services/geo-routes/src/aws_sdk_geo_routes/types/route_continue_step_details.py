"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteContinueStepDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.localized_string_list


class RouteContinueStepDetails(TypedDict):
    intersection: "aws_sdk_geo_routes.types.localized_string_list.LocalizedStringList"
    """<p>Name of the intersection, if applicable to the step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteContinueStepDetails) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.localized_string_list

    out["Intersection"] = aws_sdk_geo_routes.types.localized_string_list.serialize_json(
        value["intersection"]
    )
    return out


def deserialize_json(data: dict) -> RouteContinueStepDetails:
    out: RouteContinueStepDetails = {}  # type: ignore[typeddict-item]
    if "Intersection" in data:
        import aws_sdk_geo_routes.types.localized_string_list

        out["intersection"] = (
            aws_sdk_geo_routes.types.localized_string_list.deserialize_json(
                data["Intersection"]
            )
        )
    else:
        raise DeserializationError("RouteContinueStepDetails.intersection required")
    return out
