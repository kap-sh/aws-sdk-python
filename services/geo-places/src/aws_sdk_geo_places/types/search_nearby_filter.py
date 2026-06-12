"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.bounding_box
    import aws_sdk_geo_places.types.country_code_list
    import aws_sdk_geo_places.types.filter_business_chain_list
    import aws_sdk_geo_places.types.filter_category_list
    import aws_sdk_geo_places.types.filter_food_type_list


class SearchNearbyFilter(TypedDict):
    bounding_box: NotRequired["aws_sdk_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    include_countries: NotRequired[
        "aws_sdk_geo_places.types.country_code_list.CountryCodeList"
    ]
    """<p>A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.</p>"""
    include_categories: NotRequired[
        "aws_sdk_geo_places.types.filter_category_list.FilterCategoryList"
    ]
    """<p>Categories of results that results must belong too.</p>"""
    exclude_categories: NotRequired[
        "aws_sdk_geo_places.types.filter_category_list.FilterCategoryList"
    ]
    """<p>Categories of results that results are excluded from.</p>"""
    include_business_chains: NotRequired[
        "aws_sdk_geo_places.types.filter_business_chain_list.FilterBusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    exclude_business_chains: NotRequired[
        "aws_sdk_geo_places.types.filter_business_chain_list.FilterBusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    include_food_types: NotRequired[
        "aws_sdk_geo_places.types.filter_food_type_list.FilterFoodTypeList"
    ]
    """<p>Food types that results are included from.</p>"""
    exclude_food_types: NotRequired[
        "aws_sdk_geo_places.types.filter_food_type_list.FilterFoodTypeList"
    ]
    """<p>Food types that results are excluded from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyFilter) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import aws_sdk_geo_places.types.bounding_box

        out["BoundingBox"] = aws_sdk_geo_places.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "include_countries" in value:
        import aws_sdk_geo_places.types.country_code_list

        out["IncludeCountries"] = (
            aws_sdk_geo_places.types.country_code_list.serialize_json(
                value["include_countries"]
            )
        )
    if "include_categories" in value:
        import aws_sdk_geo_places.types.filter_category_list

        out["IncludeCategories"] = (
            aws_sdk_geo_places.types.filter_category_list.serialize_json(
                value["include_categories"]
            )
        )
    if "exclude_categories" in value:
        import aws_sdk_geo_places.types.filter_category_list

        out["ExcludeCategories"] = (
            aws_sdk_geo_places.types.filter_category_list.serialize_json(
                value["exclude_categories"]
            )
        )
    if "include_business_chains" in value:
        import aws_sdk_geo_places.types.filter_business_chain_list

        out["IncludeBusinessChains"] = (
            aws_sdk_geo_places.types.filter_business_chain_list.serialize_json(
                value["include_business_chains"]
            )
        )
    if "exclude_business_chains" in value:
        import aws_sdk_geo_places.types.filter_business_chain_list

        out["ExcludeBusinessChains"] = (
            aws_sdk_geo_places.types.filter_business_chain_list.serialize_json(
                value["exclude_business_chains"]
            )
        )
    if "include_food_types" in value:
        import aws_sdk_geo_places.types.filter_food_type_list

        out["IncludeFoodTypes"] = (
            aws_sdk_geo_places.types.filter_food_type_list.serialize_json(
                value["include_food_types"]
            )
        )
    if "exclude_food_types" in value:
        import aws_sdk_geo_places.types.filter_food_type_list

        out["ExcludeFoodTypes"] = (
            aws_sdk_geo_places.types.filter_food_type_list.serialize_json(
                value["exclude_food_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchNearbyFilter:
    out: SearchNearbyFilter = {}  # type: ignore[typeddict-item]
    if "BoundingBox" in data:
        import aws_sdk_geo_places.types.bounding_box

        out["bounding_box"] = aws_sdk_geo_places.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if "IncludeCountries" in data:
        import aws_sdk_geo_places.types.country_code_list

        out["include_countries"] = (
            aws_sdk_geo_places.types.country_code_list.deserialize_json(
                data["IncludeCountries"]
            )
        )
    if "IncludeCategories" in data:
        import aws_sdk_geo_places.types.filter_category_list

        out["include_categories"] = (
            aws_sdk_geo_places.types.filter_category_list.deserialize_json(
                data["IncludeCategories"]
            )
        )
    if "ExcludeCategories" in data:
        import aws_sdk_geo_places.types.filter_category_list

        out["exclude_categories"] = (
            aws_sdk_geo_places.types.filter_category_list.deserialize_json(
                data["ExcludeCategories"]
            )
        )
    if "IncludeBusinessChains" in data:
        import aws_sdk_geo_places.types.filter_business_chain_list

        out["include_business_chains"] = (
            aws_sdk_geo_places.types.filter_business_chain_list.deserialize_json(
                data["IncludeBusinessChains"]
            )
        )
    if "ExcludeBusinessChains" in data:
        import aws_sdk_geo_places.types.filter_business_chain_list

        out["exclude_business_chains"] = (
            aws_sdk_geo_places.types.filter_business_chain_list.deserialize_json(
                data["ExcludeBusinessChains"]
            )
        )
    if "IncludeFoodTypes" in data:
        import aws_sdk_geo_places.types.filter_food_type_list

        out["include_food_types"] = (
            aws_sdk_geo_places.types.filter_food_type_list.deserialize_json(
                data["IncludeFoodTypes"]
            )
        )
    if "ExcludeFoodTypes" in data:
        import aws_sdk_geo_places.types.filter_food_type_list

        out["exclude_food_types"] = (
            aws_sdk_geo_places.types.filter_food_type_list.deserialize_json(
                data["ExcludeFoodTypes"]
            )
        )
    return out
