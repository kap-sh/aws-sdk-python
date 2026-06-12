"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckResultResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_support.types.trusted_advisor_check_result


class DescribeTrustedAdvisorCheckResultResponse(TypedDict):
    result: NotRequired[
        "aws_sdk_support.types.trusted_advisor_check_result.TrustedAdvisorCheckResult"
    ]
    """<p>The detailed results of the Trusted Advisor check.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTrustedAdvisorCheckResultResponse) -> dict:
    out: dict = {}
    if "result" in value:
        import aws_sdk_support.types.trusted_advisor_check_result

        out["result"] = (
            aws_sdk_support.types.trusted_advisor_check_result.serialize_aws_json_1_1(
                value["result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTrustedAdvisorCheckResultResponse:
    out: DescribeTrustedAdvisorCheckResultResponse = {}  # type: ignore[typeddict-item]
    if "result" in data:
        import aws_sdk_support.types.trusted_advisor_check_result

        out["result"] = (
            aws_sdk_support.types.trusted_advisor_check_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    return out
