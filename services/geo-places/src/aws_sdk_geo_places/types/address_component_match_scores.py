"""Generated from Smithy shape ``com.amazonaws.geoplaces#AddressComponentMatchScores``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.match_score
    import aws_sdk_geo_places.types.match_score_list
    import aws_sdk_geo_places.types.secondary_address_component_match_score_list


class AddressComponentMatchScores(TypedDict):
    country: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The region or state results should be to be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>A subdivision of a district. </p> <p>Example: <code>Minden-Lübbecke</code> </p>"""
    postal_code: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess. </p>"""
    block: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    intersection: NotRequired[
        "aws_sdk_geo_places.types.match_score_list.MatchScoreList"
    ]
    """<p>Name of the streets in the intersection. </p> <p>Example: <code>[\"Friedrichstraße\",\"Unter den Linden\"]</code> </p>"""
    address_number: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The house number or address results should have. </p>"""
    building: "aws_sdk_geo_places.types.match_score.MatchScore"
    """<p>The name of the building at the address.</p>"""
    secondary_address_components: NotRequired[
        "aws_sdk_geo_places.types.secondary_address_component_match_score_list.SecondaryAddressComponentMatchScoreList"
    ]
    """<p>Match scores for the secondary address components in the result.</p> <note> <p>Coverage for this functionality is available in the following countries: AUS, AUT, BRA, CAN, ESP, FRA, GBR, IDN, IND, NZL, TUR, TWN, USA.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressComponentMatchScores) -> dict:
    out: dict = {}
    out["Country"] = value.get("country", 0)
    out["Region"] = value.get("region", 0)
    out["SubRegion"] = value.get("sub_region", 0)
    out["Locality"] = value.get("locality", 0)
    out["District"] = value.get("district", 0)
    out["SubDistrict"] = value.get("sub_district", 0)
    out["PostalCode"] = value.get("postal_code", 0)
    out["Block"] = value.get("block", 0)
    out["SubBlock"] = value.get("sub_block", 0)
    if "intersection" in value:
        import aws_sdk_geo_places.types.match_score_list

        out["Intersection"] = aws_sdk_geo_places.types.match_score_list.serialize_json(
            value["intersection"]
        )
    out["AddressNumber"] = value.get("address_number", 0)
    out["Building"] = value.get("building", 0)
    if "secondary_address_components" in value:
        import aws_sdk_geo_places.types.secondary_address_component_match_score_list

        out["SecondaryAddressComponents"] = (
            aws_sdk_geo_places.types.secondary_address_component_match_score_list.serialize_json(
                value["secondary_address_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddressComponentMatchScores:
    out: AddressComponentMatchScores = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        out["country"] = data["Country"]
    else:
        out["country"] = 0
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        out["region"] = 0
    if "SubRegion" in data:
        out["sub_region"] = data["SubRegion"]
    else:
        out["sub_region"] = 0
    if "Locality" in data:
        out["locality"] = data["Locality"]
    else:
        out["locality"] = 0
    if "District" in data:
        out["district"] = data["District"]
    else:
        out["district"] = 0
    if "SubDistrict" in data:
        out["sub_district"] = data["SubDistrict"]
    else:
        out["sub_district"] = 0
    if "PostalCode" in data:
        out["postal_code"] = data["PostalCode"]
    else:
        out["postal_code"] = 0
    if "Block" in data:
        out["block"] = data["Block"]
    else:
        out["block"] = 0
    if "SubBlock" in data:
        out["sub_block"] = data["SubBlock"]
    else:
        out["sub_block"] = 0
    if "Intersection" in data:
        import aws_sdk_geo_places.types.match_score_list

        out["intersection"] = (
            aws_sdk_geo_places.types.match_score_list.deserialize_json(
                data["Intersection"]
            )
        )
    if "AddressNumber" in data:
        out["address_number"] = data["AddressNumber"]
    else:
        out["address_number"] = 0
    if "Building" in data:
        out["building"] = data["Building"]
    else:
        out["building"] = 0
    if "SecondaryAddressComponents" in data:
        import aws_sdk_geo_places.types.secondary_address_component_match_score_list

        out["secondary_address_components"] = (
            aws_sdk_geo_places.types.secondary_address_component_match_score_list.deserialize_json(
                data["SecondaryAddressComponents"]
            )
        )
    return out
