"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCodeSecurityScanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_client_token
    import aws_sdk_inspector2.types.code_security_resource


class StartCodeSecurityScanRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_inspector2.types.code_security_client_token.CodeSecurityClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    resource: "aws_sdk_inspector2.types.code_security_resource.CodeSecurityResource"
    """<p>The resource identifier for the code repository to scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCodeSecurityScanRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import aws_sdk_inspector2.types.code_security_resource

    out["resource"] = aws_sdk_inspector2.types.code_security_resource.serialize_json(
        value["resource"]
    )
    return out


def deserialize_json(data: dict) -> StartCodeSecurityScanRequest:
    out: StartCodeSecurityScanRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "resource" in data:
        import aws_sdk_inspector2.types.code_security_resource

        out["resource"] = (
            aws_sdk_inspector2.types.code_security_resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        raise DeserializationError("StartCodeSecurityScanRequest.resource required")
    return out
