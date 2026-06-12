"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckSummariesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_support.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_summary_list


class DescribeTrustedAdvisorCheckSummariesResponse(TypedDict):
    summaries: "aws_sdk_support.types.trusted_advisor_check_summary_list.TrustedAdvisorCheckSummaryList"
    """<p>The summary information for the requested Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorCheckSummariesResponse) -> dict:
    out: dict = {}
    import aws_sdk_support.types.trusted_advisor_check_summary_list

    out["summaries"] = (
        aws_sdk_support.types.trusted_advisor_check_summary_list.serialize_aws_json_1_1(
            value["summaries"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckSummariesResponse:
    out: DescribeTrustedAdvisorCheckSummariesResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import aws_sdk_support.types.trusted_advisor_check_summary_list

        out["summaries"] = (
            aws_sdk_support.types.trusted_advisor_check_summary_list.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeTrustedAdvisorCheckSummariesResponse.summaries required"
        )
    return out
