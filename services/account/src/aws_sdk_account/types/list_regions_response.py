"""Generated from Smithy shape ``com.amazonaws.account#ListRegionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_account.types.region_opt_list


class ListRegionsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If there is more data to be returned, this will be populated. It should be passed into the <code>next-token</code> request parameter of <code>list-regions</code>.</p>"""
    regions: NotRequired["aws_sdk_account.types.region_opt_list.RegionOptList"]
    """<p>This is a list of Regions for a given account, or if the filtered parameter was used, a list of Regions that match the filter criteria set in the <code>filter</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "regions" in value:
        import aws_sdk_account.types.region_opt_list

        out["Regions"] = aws_sdk_account.types.region_opt_list.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> ListRegionsResponse:
    out: ListRegionsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Regions" in data:
        import aws_sdk_account.types.region_opt_list

        out["regions"] = aws_sdk_account.types.region_opt_list.deserialize_json(
            data["Regions"]
        )
    return out
