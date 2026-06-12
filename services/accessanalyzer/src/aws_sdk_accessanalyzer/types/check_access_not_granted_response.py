"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckAccessNotGrantedResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.check_access_not_granted_result
    import aws_sdk_accessanalyzer.types.reason_summary_list


class CheckAccessNotGrantedResponse(TypedDict):
    result: NotRequired[
        "aws_sdk_accessanalyzer.types.check_access_not_granted_result.CheckAccessNotGrantedResult"
    ]
    """<p>The result of the check for whether the access is allowed. If the result is <code>PASS</code>, the specified policy doesn't allow any of the specified permissions in the access object. If the result is <code>FAIL</code>, the specified policy might allow some or all of the permissions in the access object.</p>"""
    message: NotRequired["str"]
    """<p>The message indicating whether the specified access is allowed.</p>"""
    reasons: NotRequired[
        "aws_sdk_accessanalyzer.types.reason_summary_list.ReasonSummaryList"
    ]
    """<p>A description of the reasoning of the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckAccessNotGrantedResponse) -> dict:
    out: dict = {}
    if "result" in value:
        out["result"] = value["result"]
    if "message" in value:
        out["message"] = value["message"]
    if "reasons" in value:
        import aws_sdk_accessanalyzer.types.reason_summary_list

        out["reasons"] = (
            aws_sdk_accessanalyzer.types.reason_summary_list.serialize_json(
                value["reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> CheckAccessNotGrantedResponse:
    out: CheckAccessNotGrantedResponse = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    if "message" in data:
        out["message"] = data["message"]
    if "reasons" in data:
        import aws_sdk_accessanalyzer.types.reason_summary_list

        out["reasons"] = (
            aws_sdk_accessanalyzer.types.reason_summary_list.deserialize_json(
                data["reasons"]
            )
        )
    return out
