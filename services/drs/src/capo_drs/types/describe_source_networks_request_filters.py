"""Generated from Smithy shape ``com.amazonaws.drs#DescribeSourceNetworksRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.account_id
    import capo_drs.types.aws_region
    import capo_drs.types.describe_source_networks_request_filters_i_ds


class DescribeSourceNetworksRequestFilters(TypedDict, closed=True):
    source_network_i_ds: NotRequired[
        "capo_drs.types.describe_source_networks_request_filters_i_ds.DescribeSourceNetworksRequestFiltersIDs"
    ]
    """<p>An array of Source Network IDs that should be returned. An empty array means all Source Networks.</p>"""
    origin_account_id: NotRequired["capo_drs.types.account_id.AccountID"]
    """<p>Filter Source Networks by account ID containing the protected VPCs.</p>"""
    origin_region: NotRequired["capo_drs.types.aws_region.AwsRegion"]
    """<p>Filter Source Networks by the region containing the protected VPCs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSourceNetworksRequestFilters) -> dict:
    out: dict = {}
    if "source_network_i_ds" in value:
        import capo_drs.types.describe_source_networks_request_filters_i_ds

        out["sourceNetworkIDs"] = (
            capo_drs.types.describe_source_networks_request_filters_i_ds.serialize_json(
                value["source_network_i_ds"]
            )
        )
    if "origin_account_id" in value:
        out["originAccountID"] = value["origin_account_id"]
    if "origin_region" in value:
        out["originRegion"] = value["origin_region"]
    return out


def deserialize_json(data: dict) -> DescribeSourceNetworksRequestFilters:
    out: DescribeSourceNetworksRequestFilters = {}  # type: ignore[typeddict-item]
    if "sourceNetworkIDs" in data:
        import capo_drs.types.describe_source_networks_request_filters_i_ds

        out["source_network_i_ds"] = (
            capo_drs.types.describe_source_networks_request_filters_i_ds.deserialize_json(
                data["sourceNetworkIDs"]
            )
        )
    if "originAccountID" in data:
        out["origin_account_id"] = data["originAccountID"]
    if "originRegion" in data:
        out["origin_region"] = data["originRegion"]
    return out
