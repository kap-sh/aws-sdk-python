"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingAggregatorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class GetFindingAggregatorResponse(TypedDict, closed=True):
    finding_aggregator_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the finding aggregator.</p>"""
    finding_aggregation_region: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The home Region. Findings generated in linked Regions are replicated and sent to the home Region.</p>"""
    region_linking_mode: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether to link all Regions, all Regions except for a list of excluded Regions, or a list of included Regions.</p>"""
    regions: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The list of excluded Regions or included Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingAggregatorResponse) -> dict:
    out: dict = {}
    if "finding_aggregator_arn" in value:
        out["FindingAggregatorArn"] = value["finding_aggregator_arn"]
    if "finding_aggregation_region" in value:
        out["FindingAggregationRegion"] = value["finding_aggregation_region"]
    if "region_linking_mode" in value:
        out["RegionLinkingMode"] = value["region_linking_mode"]
    if "regions" in value:
        import capo_securityhub.types.string_list

        out["Regions"] = capo_securityhub.types.string_list.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingAggregatorResponse:
    out: GetFindingAggregatorResponse = {}  # type: ignore[typeddict-item]
    if "FindingAggregatorArn" in data:
        out["finding_aggregator_arn"] = data["FindingAggregatorArn"]
    if "FindingAggregationRegion" in data:
        out["finding_aggregation_region"] = data["FindingAggregationRegion"]
    if "RegionLinkingMode" in data:
        out["region_linking_mode"] = data["RegionLinkingMode"]
    if "Regions" in data:
        import capo_securityhub.types.string_list

        out["regions"] = capo_securityhub.types.string_list.deserialize_json(
            data["Regions"]
        )
    return out
