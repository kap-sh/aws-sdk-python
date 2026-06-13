"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateResolverTypeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.case_status
    import aws_sdk_security_ir.types.resolver_type


class UpdateResolverTypeResponse(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Response element for UpdateResolver identifying the case ID being updated.</p>"""
    case_status: NotRequired["aws_sdk_security_ir.types.case_status.CaseStatus"]
    """<p>Response element for UpdateResolver identifying the current status of the case.</p>"""
    resolver_type: NotRequired["aws_sdk_security_ir.types.resolver_type.ResolverType"]
    """<p>Response element for UpdateResolver identifying the current resolver of the case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResolverTypeResponse) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "case_status" in value:
        import aws_sdk_security_ir.types.case_status

        out["caseStatus"] = aws_sdk_security_ir.types.case_status.serialize_json(
            value["case_status"]
        )
    if "resolver_type" in value:
        import aws_sdk_security_ir.types.resolver_type

        out["resolverType"] = aws_sdk_security_ir.types.resolver_type.serialize_json(
            value["resolver_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResolverTypeResponse:
    out: UpdateResolverTypeResponse = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("UpdateResolverTypeResponse.case_id required")
    if "caseStatus" in data:
        import aws_sdk_security_ir.types.case_status

        out["case_status"] = aws_sdk_security_ir.types.case_status.deserialize_json(
            data["caseStatus"]
        )
    if "resolverType" in data:
        import aws_sdk_security_ir.types.resolver_type

        out["resolver_type"] = aws_sdk_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    return out
