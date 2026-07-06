"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixExclusionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.country_code_list


class RouteMatrixExclusionOptions(TypedDict, closed=True):
    countries: "aws_sdk_geo_routes.types.country_code_list.CountryCodeList"
    """<p>List of countries to be avoided defined by two-letter or three-letter country codes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixExclusionOptions) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.country_code_list

    out["Countries"] = aws_sdk_geo_routes.types.country_code_list.serialize_json(
        value["countries"]
    )
    return out


def deserialize_json(data: dict) -> RouteMatrixExclusionOptions:
    out: RouteMatrixExclusionOptions = {}  # type: ignore[typeddict-item]
    if "Countries" in data:
        import aws_sdk_geo_routes.types.country_code_list

        out["countries"] = aws_sdk_geo_routes.types.country_code_list.deserialize_json(
            data["Countries"]
        )
    else:
        raise DeserializationError("RouteMatrixExclusionOptions.countries required")
    return out
