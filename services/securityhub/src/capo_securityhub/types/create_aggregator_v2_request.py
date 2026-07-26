"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateAggregatorV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.client_token
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list
    import capo_securityhub.types.tag_map


class CreateAggregatorV2Request(TypedDict, closed=True):
    region_linking_mode: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Determines how Regions are linked to an Aggregator V2.</p>"""
    linked_regions: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of Regions that are linked to the aggregation Region.</p>"""
    tags: NotRequired["capo_securityhub.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to be applied to the AggregatorV2.</p>"""
    client_token: NotRequired["capo_securityhub.types.client_token.ClientToken"]
    """<p>A unique identifier used to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAggregatorV2Request) -> dict:
    out: dict = {}
    if "region_linking_mode" in value:
        out["RegionLinkingMode"] = value["region_linking_mode"]
    if "linked_regions" in value:
        import capo_securityhub.types.string_list

        out["LinkedRegions"] = capo_securityhub.types.string_list.serialize_json(
            value["linked_regions"]
        )
    if "tags" in value:
        import capo_securityhub.types.tag_map

        out["Tags"] = capo_securityhub.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAggregatorV2Request:
    out: CreateAggregatorV2Request = {}  # type: ignore[typeddict-item]
    if "RegionLinkingMode" in data:
        out["region_linking_mode"] = data["RegionLinkingMode"]
    if "LinkedRegions" in data:
        import capo_securityhub.types.string_list

        out["linked_regions"] = capo_securityhub.types.string_list.deserialize_json(
            data["LinkedRegions"]
        )
    if "Tags" in data:
        import capo_securityhub.types.tag_map

        out["tags"] = capo_securityhub.types.tag_map.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
