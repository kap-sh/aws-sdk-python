"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationAnalysisResultsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.vpc_i_ds_filter


class ListNetworkMigrationAnalysisResultsFilters(TypedDict, closed=True):
    vpc_i_ds: NotRequired["capo_mgn.types.vpc_i_ds_filter.VpcIDsFilter"]
    """<p>A list of VPC IDs to filter results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationAnalysisResultsFilters) -> dict:
    out: dict = {}
    if "vpc_i_ds" in value:
        import capo_mgn.types.vpc_i_ds_filter

        out["vpcIDs"] = capo_mgn.types.vpc_i_ds_filter.serialize_json(value["vpc_i_ds"])
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationAnalysisResultsFilters:
    out: ListNetworkMigrationAnalysisResultsFilters = {}  # type: ignore[typeddict-item]
    if "vpcIDs" in data:
        import capo_mgn.types.vpc_i_ds_filter

        out["vpc_i_ds"] = capo_mgn.types.vpc_i_ds_filter.deserialize_json(
            data["vpcIDs"]
        )
    return out
