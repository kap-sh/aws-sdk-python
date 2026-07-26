"""Generated from Smithy shape ``com.amazonaws.support#ResolveCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.case_status


class ResolveCaseResponse(TypedDict, closed=True):
    initial_case_status: NotRequired["capo_support.types.case_status.CaseStatus"]
    """<p>The status of the case when the <a>ResolveCase</a> request was sent.</p>"""
    final_case_status: NotRequired["capo_support.types.case_status.CaseStatus"]
    """<p>The status of the case after the <a>ResolveCase</a> request was processed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolveCaseResponse) -> dict:
    out: dict = {}
    if "initial_case_status" in value:
        out["initialCaseStatus"] = value["initial_case_status"]
    if "final_case_status" in value:
        out["finalCaseStatus"] = value["final_case_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolveCaseResponse:
    out: ResolveCaseResponse = {}  # type: ignore[typeddict-item]
    if "initialCaseStatus" in data:
        out["initial_case_status"] = data["initialCaseStatus"]
    if "finalCaseStatus" in data:
        out["final_case_status"] = data["finalCaseStatus"]
    return out
