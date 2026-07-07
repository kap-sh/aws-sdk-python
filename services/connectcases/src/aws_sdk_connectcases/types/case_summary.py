"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_id
    import aws_sdk_connectcases.types.template_id


class CaseSummary(TypedDict, closed=True):
    case_id: "aws_sdk_connectcases.types.case_id.CaseId"
    """<p>A unique identifier of the case.</p>"""
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummary) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    out["templateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> CaseSummary:
    out: CaseSummary = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("CaseSummary.case_id required")
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CaseSummary.template_id required")
    return out
