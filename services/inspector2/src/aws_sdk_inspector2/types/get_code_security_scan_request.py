"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityScanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_resource
    import aws_sdk_inspector2.types.code_security_uuid


class GetCodeSecurityScanRequest(TypedDict):
    resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"
    """<p>The resource identifier for the code repository that was scanned.</p>"""
    scan_id: "aws_sdk_inspector2.types.code_security_uuid.CodeSecurityUuid"
    """<p>The unique identifier of the scan to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityScanRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.code_security_resource

    out["resource"] = aws_sdk_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    out["scanId"] = value["scan_id"]
    return out


def deserialize_json(data: dict) -> GetCodeSecurityScanRequest:
    out: GetCodeSecurityScanRequest = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("GetCodeSecurityScanRequest.resource required")
    if "scanId" in data:
        out["scan_id"] = data["scanId"]
    else:
        raise DeserializationError("GetCodeSecurityScanRequest.scan_id required")
    return out
