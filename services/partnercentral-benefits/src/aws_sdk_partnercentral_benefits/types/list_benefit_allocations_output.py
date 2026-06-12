"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitAllocationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries


class ListBenefitAllocationsOutput(TypedDict):
    benefit_allocation_summaries: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries.BenefitAllocationSummaries"
    ]
    """<p>A list of benefit allocation summaries matching the specified criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results, if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitAllocationsOutput) -> dict:
    out: dict = {}
    if "benefit_allocation_summaries" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries

        out["BenefitAllocationSummaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries.serialize_aws_json_1_0(
                value["benefit_allocation_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitAllocationsOutput:
    out: ListBenefitAllocationsOutput = {}  # type: ignore[typeddict-item]
    if "BenefitAllocationSummaries" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries

        out["benefit_allocation_summaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_allocation_summaries.deserialize_aws_json_1_0(
                data["BenefitAllocationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
