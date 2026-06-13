"""Generated from Smithy shape ``com.amazonaws.securityir#UpdateResolverTypeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id
    import aws_sdk_security_ir.types.resolver_type


class UpdateResolverTypeRequest(TypedDict):
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element for UpdateResolverType to identify the case to update.</p>"""
    resolver_type: "aws_sdk_security_ir.types.resolver_type.ResolverType"
    """<p>Required element for UpdateResolverType to identify the new resolver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResolverTypeRequest) -> dict:
    out: dict = {}
    import aws_sdk_security_ir.types.resolver_type

    out["resolverType"] = aws_sdk_security_ir.types.resolver_type.serialize_json(
        value["resolver_type"]
    )
    return out


def deserialize_json(data: dict) -> UpdateResolverTypeRequest:
    out: UpdateResolverTypeRequest = {}  # type: ignore[typeddict-item]
    if "resolverType" in data:
        import aws_sdk_security_ir.types.resolver_type

        out["resolver_type"] = aws_sdk_security_ir.types.resolver_type.deserialize_json(
            data["resolverType"]
        )
    else:
        raise DeserializationError("UpdateResolverTypeRequest.resolver_type required")
    return out
