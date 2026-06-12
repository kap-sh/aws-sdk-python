"""Generated from Smithy shape ``com.amazonaws.outposts#ListSitesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.city_list
    import aws_sdk_outposts.types.country_code_list
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.state_or_region_list
    import aws_sdk_outposts.types.token


class ListSitesInput(TypedDict):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    operating_address_country_code_filter: NotRequired[
        "aws_sdk_outposts.types.country_code_list.CountryCodeList"
    ]
    """<p>Filters the results by country code.</p>"""
    operating_address_state_or_region_filter: NotRequired[
        "aws_sdk_outposts.types.state_or_region_list.StateOrRegionList"
    ]
    """<p>Filters the results by state or region.</p>"""
    operating_address_city_filter: NotRequired[
        "aws_sdk_outposts.types.city_list.CityList"
    ]
    """<p>Filters the results by city.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSitesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSitesInput:
    out: ListSitesInput = {}  # type: ignore[typeddict-item]
    return out
