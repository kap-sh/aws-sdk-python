"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteAddressHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.country_highlights
    import aws_sdk_geo_places.types.highlight_list
    import aws_sdk_geo_places.types.intersection_highlights_list
    import aws_sdk_geo_places.types.region_highlights
    import aws_sdk_geo_places.types.sub_region_highlights


class AutocompleteAddressHighlights(TypedDict, closed=True):
    label: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending indexes for result items where they are identified to match the input query. This should be used to provide emphasis to output display to make selecting the correct result from a list easier for end users.</p>"""
    country: NotRequired[
        "aws_sdk_geo_places.types.country_highlights.CountryHighlights"
    ]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired["aws_sdk_geo_places.types.region_highlights.RegionHighlights"]
    """<p>The region or state results should be to be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired[
        "aws_sdk_geo_places.types.sub_region_highlights.SubRegionHighlights"
    ]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>The city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the title in the text query that match the found title. </p>"""
    street: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>The name of the street results should be present in.</p>"""
    block: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    intersection: NotRequired[
        "aws_sdk_geo_places.types.intersection_highlights_list.IntersectionHighlightsList"
    ]
    r"""<p>Name of the streets in the intersection. For example: e.g. [\"Friedrichstraße\",\"Unter den Linden\"]</p>"""
    postal_code: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess. </p>"""
    address_number: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>The house number or address results should have. </p>"""
    building: NotRequired["aws_sdk_geo_places.types.highlight_list.HighlightList"]
    """<p>The name of the building at the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteAddressHighlights) -> dict:
    out: dict = {}
    if "label" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Label"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["label"]
        )
    if "country" in value:
        import aws_sdk_geo_places.types.country_highlights

        out["Country"] = aws_sdk_geo_places.types.country_highlights.serialize_json(
            value["country"]
        )
    if "region" in value:
        import aws_sdk_geo_places.types.region_highlights

        out["Region"] = aws_sdk_geo_places.types.region_highlights.serialize_json(
            value["region"]
        )
    if "sub_region" in value:
        import aws_sdk_geo_places.types.sub_region_highlights

        out["SubRegion"] = (
            aws_sdk_geo_places.types.sub_region_highlights.serialize_json(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Locality"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["locality"]
        )
    if "district" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["District"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["district"]
        )
    if "sub_district" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["SubDistrict"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["sub_district"]
        )
    if "street" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Street"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["street"]
        )
    if "block" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Block"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["block"]
        )
    if "sub_block" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["SubBlock"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["sub_block"]
        )
    if "intersection" in value:
        import aws_sdk_geo_places.types.intersection_highlights_list

        out["Intersection"] = (
            aws_sdk_geo_places.types.intersection_highlights_list.serialize_json(
                value["intersection"]
            )
        )
    if "postal_code" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["PostalCode"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["postal_code"]
        )
    if "address_number" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["AddressNumber"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["address_number"]
        )
    if "building" in value:
        import aws_sdk_geo_places.types.highlight_list

        out["Building"] = aws_sdk_geo_places.types.highlight_list.serialize_json(
            value["building"]
        )
    return out


def deserialize_json(data: dict) -> AutocompleteAddressHighlights:
    out: AutocompleteAddressHighlights = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["label"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Label"]
        )
    if "Country" in data:
        import aws_sdk_geo_places.types.country_highlights

        out["country"] = aws_sdk_geo_places.types.country_highlights.deserialize_json(
            data["Country"]
        )
    if "Region" in data:
        import aws_sdk_geo_places.types.region_highlights

        out["region"] = aws_sdk_geo_places.types.region_highlights.deserialize_json(
            data["Region"]
        )
    if "SubRegion" in data:
        import aws_sdk_geo_places.types.sub_region_highlights

        out["sub_region"] = (
            aws_sdk_geo_places.types.sub_region_highlights.deserialize_json(
                data["SubRegion"]
            )
        )
    if "Locality" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["locality"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Locality"]
        )
    if "District" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["district"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["District"]
        )
    if "SubDistrict" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["sub_district"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["SubDistrict"]
        )
    if "Street" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["street"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Street"]
        )
    if "Block" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["block"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Block"]
        )
    if "SubBlock" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["sub_block"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["SubBlock"]
        )
    if "Intersection" in data:
        import aws_sdk_geo_places.types.intersection_highlights_list

        out["intersection"] = (
            aws_sdk_geo_places.types.intersection_highlights_list.deserialize_json(
                data["Intersection"]
            )
        )
    if "PostalCode" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["postal_code"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["PostalCode"]
        )
    if "AddressNumber" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["address_number"] = (
            aws_sdk_geo_places.types.highlight_list.deserialize_json(
                data["AddressNumber"]
            )
        )
    if "Building" in data:
        import aws_sdk_geo_places.types.highlight_list

        out["building"] = aws_sdk_geo_places.types.highlight_list.deserialize_json(
            data["Building"]
        )
    return out
