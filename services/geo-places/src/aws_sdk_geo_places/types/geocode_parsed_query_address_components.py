"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeParsedQueryAddressComponents``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_places.types.parsed_query_component_list
    import aws_sdk_geo_places.types.parsed_query_secondary_address_component_list


class GeocodeParsedQueryAddressComponents(TypedDict, closed=True):
    country: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The region or state results should be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The city or locality of the address.</p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>A subdivision of a district. </p> <p>Example: <code>Minden-Lübbecke</code>.</p>"""
    postal_code: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess. </p>"""
    block: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    street: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The name of the street results should be present in.</p>"""
    address_number: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The number that identifies an address within a street.</p>"""
    building: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The name of the building at the address.</p>"""
    secondary_address_components: NotRequired[
        "aws_sdk_geo_places.types.parsed_query_secondary_address_component_list.ParsedQuerySecondaryAddressComponentList"
    ]
    """<p>Parsed secondary address components from the provided query text.</p> <note> <p>Coverage for <code>ParsedQuery.Address.SecondaryAddressComponents</code> is available in the following countries:</p> <p>AUS, AUT, BRA, CAN, ESP, FRA, GBR, HKG, IDN, IND, NZL, TUR, TWN, USA</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeParsedQueryAddressComponents) -> dict:
    out: dict = {}
    if "country" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Country"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["country"]
            )
        )
    if "region" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Region"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["region"]
            )
        )
    if "sub_region" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["SubRegion"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Locality"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["locality"]
            )
        )
    if "district" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["District"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["district"]
            )
        )
    if "sub_district" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["SubDistrict"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_district"]
            )
        )
    if "postal_code" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["PostalCode"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["postal_code"]
            )
        )
    if "block" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Block"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["block"]
            )
        )
    if "sub_block" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["SubBlock"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_block"]
            )
        )
    if "street" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Street"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["street"]
            )
        )
    if "address_number" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["AddressNumber"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["address_number"]
            )
        )
    if "building" in value:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["Building"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.serialize_json(
                value["building"]
            )
        )
    if "secondary_address_components" in value:
        import aws_sdk_geo_places.types.parsed_query_secondary_address_component_list

        out["SecondaryAddressComponents"] = (
            aws_sdk_geo_places.types.parsed_query_secondary_address_component_list.serialize_json(
                value["secondary_address_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeParsedQueryAddressComponents:
    out: GeocodeParsedQueryAddressComponents = {}  # type: ignore[typeddict-item]
    if "Country" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["country"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Country"]
            )
        )
    if "Region" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["region"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Region"]
            )
        )
    if "SubRegion" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["sub_region"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubRegion"]
            )
        )
    if "Locality" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["locality"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Locality"]
            )
        )
    if "District" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["district"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["District"]
            )
        )
    if "SubDistrict" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["sub_district"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubDistrict"]
            )
        )
    if "PostalCode" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["postal_code"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["PostalCode"]
            )
        )
    if "Block" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["block"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Block"]
            )
        )
    if "SubBlock" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["sub_block"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubBlock"]
            )
        )
    if "Street" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["street"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Street"]
            )
        )
    if "AddressNumber" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["address_number"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["AddressNumber"]
            )
        )
    if "Building" in data:
        import aws_sdk_geo_places.types.parsed_query_component_list

        out["building"] = (
            aws_sdk_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Building"]
            )
        )
    if "SecondaryAddressComponents" in data:
        import aws_sdk_geo_places.types.parsed_query_secondary_address_component_list

        out["secondary_address_components"] = (
            aws_sdk_geo_places.types.parsed_query_secondary_address_component_list.deserialize_json(
                data["SecondaryAddressComponents"]
            )
        )
    return out
