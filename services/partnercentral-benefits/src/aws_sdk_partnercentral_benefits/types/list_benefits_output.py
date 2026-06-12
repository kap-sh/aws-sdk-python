"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_summaries


class ListBenefitsOutput(TypedDict):
    benefit_summaries: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_summaries.BenefitSummaries"
    ]
    """<p>A list of benefit summaries matching the specified criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results, if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitsOutput) -> dict:
    out: dict = {}
    if "benefit_summaries" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_summaries

        out["BenefitSummaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_summaries.serialize_aws_json_1_0(
                value["benefit_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitsOutput:
    out: ListBenefitsOutput = {}  # type: ignore[typeddict-item]
    if "BenefitSummaries" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_summaries

        out["benefit_summaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_summaries.deserialize_aws_json_1_0(
                data["BenefitSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
