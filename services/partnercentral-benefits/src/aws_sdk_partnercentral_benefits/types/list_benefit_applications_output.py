"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#ListBenefitApplicationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.benefit_application_summaries


class ListBenefitApplicationsOutput(TypedDict, closed=True):
    benefit_application_summaries: NotRequired[
        "aws_sdk_partnercentral_benefits.types.benefit_application_summaries.BenefitApplicationSummaries"
    ]
    """<p>A list of benefit application summaries matching the specified criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results, if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBenefitApplicationsOutput) -> dict:
    out: dict = {}
    if "benefit_application_summaries" in value:
        import aws_sdk_partnercentral_benefits.types.benefit_application_summaries

        out["BenefitApplicationSummaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_application_summaries.serialize_aws_json_1_0(
                value["benefit_application_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBenefitApplicationsOutput:
    out: ListBenefitApplicationsOutput = {}  # type: ignore[typeddict-item]
    if "BenefitApplicationSummaries" in data:
        import aws_sdk_partnercentral_benefits.types.benefit_application_summaries

        out["benefit_application_summaries"] = (
            aws_sdk_partnercentral_benefits.types.benefit_application_summaries.deserialize_aws_json_1_0(
                data["BenefitApplicationSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
