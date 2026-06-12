"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateAggregatorV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.string_list


class UpdateAggregatorV2Response(TypedDict):
    aggregator_v2_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Aggregator V2.</p>"""
    aggregation_region: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services Region where data is aggregated.</p>"""
    region_linking_mode: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Determines how Amazon Web Services Regions should be linked to the Aggregator V2.</p>"""
    linked_regions: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of Amazon Web Services Regions linked to the aggegation Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAggregatorV2Response) -> dict:
    out: dict = {}
    if "aggregator_v2_arn" in value:
        out["AggregatorV2Arn"] = value["aggregator_v2_arn"]
    if "aggregation_region" in value:
        out["AggregationRegion"] = value["aggregation_region"]
    if "region_linking_mode" in value:
        out["RegionLinkingMode"] = value["region_linking_mode"]
    if "linked_regions" in value:
        import aws_sdk_securityhub.types.string_list

        out["LinkedRegions"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["linked_regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAggregatorV2Response:
    out: UpdateAggregatorV2Response = {}  # type: ignore[typeddict-item]
    if "AggregatorV2Arn" in data:
        out["aggregator_v2_arn"] = data["AggregatorV2Arn"]
    if "AggregationRegion" in data:
        out["aggregation_region"] = data["AggregationRegion"]
    if "RegionLinkingMode" in data:
        out["region_linking_mode"] = data["RegionLinkingMode"]
    if "LinkedRegions" in data:
        import aws_sdk_securityhub.types.string_list

        out["linked_regions"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["LinkedRegions"]
        )
    return out
