"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckNoNewAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.check_no_new_access_result
    import aws_sdk_accessanalyzer.types.reason_summary_list


class CheckNoNewAccessResponse(TypedDict, closed=True):
    result: NotRequired[
        "aws_sdk_accessanalyzer.types.check_no_new_access_result.CheckNoNewAccessResult"
    ]
    """<p>The result of the check for new access. If the result is <code>PASS</code>, no new access is allowed by the updated policy. If the result is <code>FAIL</code>, the updated policy might allow new access.</p>"""
    message: NotRequired["str"]
    """<p>The message indicating whether the updated policy allows new access.</p>"""
    reasons: NotRequired[
        "aws_sdk_accessanalyzer.types.reason_summary_list.ReasonSummaryList"
    ]
    """<p>A description of the reasoning of the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckNoNewAccessResponse) -> dict:
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


def deserialize_json(data: dict) -> CheckNoNewAccessResponse:
    out: CheckNoNewAccessResponse = {}  # type: ignore[typeddict-item]
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
