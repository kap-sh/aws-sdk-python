"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_summary_list


class DescribeTrustedAdvisorCheckSummariesResponse(TypedDict, closed=True):
    summaries: "capo_support.types.trusted_advisor_check_summary_list.TrustedAdvisorCheckSummaryList"
    """<p>The summary information for the requested Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorCheckSummariesResponse) -> dict:
    out: dict = {}
    import capo_support.types.trusted_advisor_check_summary_list

    out["summaries"] = (
        capo_support.types.trusted_advisor_check_summary_list.serialize_aws_json_1_1(
            value["summaries"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckSummariesResponse:
    out: DescribeTrustedAdvisorCheckSummariesResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import capo_support.types.trusted_advisor_check_summary_list

        out["summaries"] = (
            capo_support.types.trusted_advisor_check_summary_list.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorCheckSummariesResponse.summaries required"
        )
    return out
