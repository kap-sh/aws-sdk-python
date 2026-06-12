"""Generated from Smithy shape ``com.amazonaws.wafv2#ChallengeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.failure_reason
    import aws_sdk_wafv2.types.response_code
    import aws_sdk_wafv2.types.solve_timestamp


class ChallengeResponse(TypedDict):
    response_code: NotRequired["aws_sdk_wafv2.types.response_code.ResponseCode"]
    """<p>The HTTP response code indicating the status of the challenge token in the web request. If the token is missing, invalid, or expired, this code is <code>202 Request Accepted</code>.</p>"""
    solve_timestamp: NotRequired["aws_sdk_wafv2.types.solve_timestamp.SolveTimestamp"]
    """<p>The time that the challenge was last solved for the supplied token. </p>"""
    failure_reason: NotRequired["aws_sdk_wafv2.types.failure_reason.FailureReason"]
    """<p>The reason for failure, populated when the evaluation of the token fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeResponse) -> dict:
    out: dict = {}
    if "response_code" in value:
        out["ResponseCode"] = value["response_code"]
    if "solve_timestamp" in value:
        out["SolveTimestamp"] = value["solve_timestamp"]
    if "failure_reason" in value:
        import aws_sdk_wafv2.types.failure_reason

        out["FailureReason"] = (
            aws_sdk_wafv2.types.failure_reason.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengeResponse:
    out: ChallengeResponse = {}  # type: ignore[typeddict-item]
    if "ResponseCode" in data:
        out["response_code"] = data["ResponseCode"]
    if "SolveTimestamp" in data:
        out["solve_timestamp"] = data["SolveTimestamp"]
    if "FailureReason" in data:
        import aws_sdk_wafv2.types.failure_reason

        out["failure_reason"] = (
            aws_sdk_wafv2.types.failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    return out
