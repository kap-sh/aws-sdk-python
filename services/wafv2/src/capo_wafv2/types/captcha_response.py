"""Generated from Smithy shape ``com.amazonaws.wafv2#CaptchaResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.failure_reason
    import capo_wafv2.types.response_code
    import capo_wafv2.types.solve_timestamp


class CaptchaResponse(TypedDict, closed=True):
    response_code: NotRequired["capo_wafv2.types.response_code.ResponseCode"]
    """<p>The HTTP response code indicating the status of the <code>CAPTCHA</code> token in the web request. If the token is missing, invalid, or expired, this code is <code>405 Method Not Allowed</code>.</p>"""
    solve_timestamp: NotRequired["capo_wafv2.types.solve_timestamp.SolveTimestamp"]
    """<p>The time that the <code>CAPTCHA</code> was last solved for the supplied token. </p>"""
    failure_reason: NotRequired["capo_wafv2.types.failure_reason.FailureReason"]
    """<p>The reason for failure, populated when the evaluation of the token fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaptchaResponse) -> dict:
    out: dict = {}
    if "response_code" in value:
        out["ResponseCode"] = value["response_code"]
    if "solve_timestamp" in value:
        out["SolveTimestamp"] = value["solve_timestamp"]
    if "failure_reason" in value:
        import capo_wafv2.types.failure_reason

        out["FailureReason"] = capo_wafv2.types.failure_reason.serialize_aws_json_1_1(
            value["failure_reason"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CaptchaResponse:
    out: CaptchaResponse = {}  # type: ignore[typeddict-item]
    if "ResponseCode" in data:
        out["response_code"] = data["ResponseCode"]
    if "SolveTimestamp" in data:
        out["solve_timestamp"] = data["SolveTimestamp"]
    if "FailureReason" in data:
        import capo_wafv2.types.failure_reason

        out["failure_reason"] = (
            capo_wafv2.types.failure_reason.deserialize_aws_json_1_1(
                data["FailureReason"]
            )
        )
    return out
