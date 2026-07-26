"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateFindingAggregatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class CreateFindingAggregatorRequest(TypedDict, closed=True):
    region_linking_mode: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub CSPM supports them and you opt into them.</p> <p>The selected option also determines how to use the Regions provided in the Regions list.</p> <p>The options are as follows:</p> <ul> <li> <p> <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub CSPM is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub CSPM also automatically aggregates findings from new Regions as Security Hub CSPM supports them and you opt into them. </p> </li> <li> <p> <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub CSPM does not automatically aggregate findings from new Regions. </p> </li> <li> <p> <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions. </p> </li> </ul>"""
    regions: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.</p> <p>If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region. </p> <p>An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFindingAggregatorRequest) -> dict:
    out: dict = {}
    if "region_linking_mode" in value:
        out["RegionLinkingMode"] = value["region_linking_mode"]
    if "regions" in value:
        import capo_securityhub.types.string_list

        out["Regions"] = capo_securityhub.types.string_list.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> CreateFindingAggregatorRequest:
    out: CreateFindingAggregatorRequest = {}  # type: ignore[typeddict-item]
    if "RegionLinkingMode" in data:
        out["region_linking_mode"] = data["RegionLinkingMode"]
    if "Regions" in data:
        import capo_securityhub.types.string_list

        out["regions"] = capo_securityhub.types.string_list.deserialize_json(
            data["Regions"]
        )
    return out
