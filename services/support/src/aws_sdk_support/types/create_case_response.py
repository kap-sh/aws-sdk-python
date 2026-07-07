"""Generated from Smithy shape ``com.amazonaws.support#CreateCaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_support.types.case_id


class CreateCaseResponse(TypedDict, closed=True):
    case_id: NotRequired["aws_sdk_support.types.case_id.CaseId"]
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string in the following format: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCaseResponse) -> dict:
    out: dict = {}
    if "case_id" in value:
        out["caseId"] = value["case_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCaseResponse:
    out: CreateCaseResponse = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    return out
