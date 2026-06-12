"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListCoreNetworkRoutingInformationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.filter_map
    import aws_sdk_networkmanager.types.max_results
    import aws_sdk_networkmanager.types.next_token


class ListCoreNetworkRoutingInformationRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of the core network to retrieve routing information for.</p>"""
    segment_name: "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    """<p>The name of the segment to filter routing information by.</p>"""
    edge_location: (
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    )
    """<p>The edge location to filter routing information by.</p>"""
    next_hop_filters: NotRequired["aws_sdk_networkmanager.types.filter_map.FilterMap"]
    """<p>Filters to apply based on next hop information.</p>"""
    local_preference_matches: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Local preference values to match when filtering routing information.</p>"""
    exact_as_path_matches: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Exact AS path values to match when filtering routing information.</p>"""
    med_matches: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>Multi-Exit Discriminator (MED) values to match when filtering routing information.</p>"""
    community_matches: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>BGP community values to match when filtering routing information.</p>"""
    max_results: NotRequired["aws_sdk_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of routing information entries to return in a single page.</p>"""
    next_token: NotRequired["aws_sdk_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreNetworkRoutingInformationRequest) -> dict:
    out: dict = {}
    out["SegmentName"] = value["segment_name"]
    out["EdgeLocation"] = value["edge_location"]
    if "next_hop_filters" in value:
        import aws_sdk_networkmanager.types.filter_map

        out["NextHopFilters"] = aws_sdk_networkmanager.types.filter_map.serialize_json(
            value["next_hop_filters"]
        )
    if "local_preference_matches" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["LocalPreferenceMatches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["local_preference_matches"]
            )
        )
    if "exact_as_path_matches" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["ExactAsPathMatches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["exact_as_path_matches"]
            )
        )
    if "med_matches" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["MedMatches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["med_matches"]
            )
        )
    if "community_matches" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["CommunityMatches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["community_matches"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoreNetworkRoutingInformationRequest:
    out: ListCoreNetworkRoutingInformationRequest = {}  # type: ignore[typeddict-item]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    else:
        raise DeserializationError(
            "ListCoreNetworkRoutingInformationRequest.segment_name required"
        )
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    else:
        raise DeserializationError(
            "ListCoreNetworkRoutingInformationRequest.edge_location required"
        )
    if "NextHopFilters" in data:
        import aws_sdk_networkmanager.types.filter_map

        out["next_hop_filters"] = (
            aws_sdk_networkmanager.types.filter_map.deserialize_json(
                data["NextHopFilters"]
            )
        )
    if "LocalPreferenceMatches" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["local_preference_matches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["LocalPreferenceMatches"]
            )
        )
    if "ExactAsPathMatches" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["exact_as_path_matches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["ExactAsPathMatches"]
            )
        )
    if "MedMatches" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["med_matches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["MedMatches"]
            )
        )
    if "CommunityMatches" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["community_matches"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["CommunityMatches"]
            )
        )
    return out
