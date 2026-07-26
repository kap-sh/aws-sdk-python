"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CheckNoPublicAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.check_no_public_access_result
    import capo_accessanalyzer.types.reason_summary_list


class CheckNoPublicAccessResponse(TypedDict, closed=True):
    result: NotRequired[
        "capo_accessanalyzer.types.check_no_public_access_result.CheckNoPublicAccessResult"
    ]
    """<p>The result of the check for public access to the specified resource type. If the result is <code>PASS</code>, the policy doesn't allow public access to the specified resource type. If the result is <code>FAIL</code>, the policy might allow public access to the specified resource type.</p>"""
    message: NotRequired["str"]
    """<p>The message indicating whether the specified policy allows public access to resources.</p>"""
    reasons: NotRequired[
        "capo_accessanalyzer.types.reason_summary_list.ReasonSummaryList"
    ]
    """<p>A list of reasons why the specified resource policy grants public access for the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckNoPublicAccessResponse) -> dict:
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


def deserialize_json(data: dict) -> CheckNoPublicAccessResponse:
    out: CheckNoPublicAccessResponse = {}  # type: ignore[typeddict-item]
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
