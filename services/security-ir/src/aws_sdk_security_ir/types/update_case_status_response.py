"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateCaseStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.self_managed_case_status


class UpdateCaseStatusResponse(TypedDict, closed=True):
    case_status: NotRequired[
        "aws_sdk_security_ir.types.self_managed_case_status.SelfManagedCaseStatus"
    ]
    """<p>Response element for UpdateCaseStatus showing the newly configured status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCaseStatusResponse) -> dict:
    out: dict = {}
    if "case_status" in value:
        import aws_sdk_security_ir.types.self_managed_case_status

        out["caseStatus"] = (
            aws_sdk_security_ir.types.self_managed_case_status.serialize_json(
                value["case_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCaseStatusResponse:
    out: UpdateCaseStatusResponse = {}  # type: ignore[typeddict-item]
    if "caseStatus" in data:
        import aws_sdk_security_ir.types.self_managed_case_status

        out["case_status"] = (
            aws_sdk_security_ir.types.self_managed_case_status.deserialize_json(
                data["caseStatus"]
            )
        )
    return out
