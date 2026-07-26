"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckAccessNotGrantedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.check_access_not_granted_result
    import capo_accessanalyzer.types.reason_summary_list


class CheckAccessNotGrantedResponse(TypedDict, closed=True):
    result: NotRequired[
        "capo_accessanalyzer.types.check_access_not_granted_result.CheckAccessNotGrantedResult"
    ]
    """<p>The result of the check for whether the access is allowed. If the result is <code>PASS</code>, the specified policy doesn't allow any of the specified permissions in the access object. If the result is <code>FAIL</code>, the specified policy might allow some or all of the permissions in the access object.</p>"""
    message: NotRequired["str"]
    """<p>The message indicating whether the specified access is allowed.</p>"""
    reasons: NotRequired[
        "capo_accessanalyzer.types.reason_summary_list.ReasonSummaryList"
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
        import capo_accessanalyzer.types.reason_summary_list

        out["reasons"] = capo_accessanalyzer.types.reason_summary_list.serialize_json(
            value["reasons"]
        )
    return out


def deserialize_json(data: dict) -> CheckAccessNotGrantedResponse:
    out: CheckAccessNotGrantedResponse = {}  # type: ignore[typeddict-item]
    if "result" in data:
        out["result"] = data["result"]
    if "message" in data:
        out["message"] = data["message"]
    if "reasons" in data:
        import capo_accessanalyzer.types.reason_summary_list

        out["reasons"] = capo_accessanalyzer.types.reason_summary_list.deserialize_json(
            data["reasons"]
        )
    return out
