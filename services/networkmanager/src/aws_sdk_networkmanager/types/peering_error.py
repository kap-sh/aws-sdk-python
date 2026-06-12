"""Generated from Smithy shape ``com.amazonaws.networkmanager#PeeringError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.peering_error_code
    import aws_sdk_networkmanager.types.permissions_error_context
    import aws_sdk_networkmanager.types.resource_arn
    import aws_sdk_networkmanager.types.server_side_string


class PeeringError(TypedDict):
    code: NotRequired[
        "aws_sdk_networkmanager.types.peering_error_code.PeeringErrorCode"
    ]
    """<p>The error code for the peering request.</p>"""
    message: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The message associated with the error <code>code</code>.</p>"""
    resource_arn: NotRequired["aws_sdk_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The ARN of the requested peering resource.</p>"""
    request_id: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The ID of the Peering request.</p>"""
    missing_permissions_context: NotRequired[
        "aws_sdk_networkmanager.types.permissions_error_context.PermissionsErrorContext"
    ]
    """<p>Provides additional information about missing permissions for the peering error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PeeringError) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_networkmanager.types.peering_error_code

        out["Code"] = aws_sdk_networkmanager.types.peering_error_code.serialize_json(
            value["code"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "missing_permissions_context" in value:
        import aws_sdk_networkmanager.types.permissions_error_context

        out["MissingPermissionsContext"] = (
            aws_sdk_networkmanager.types.permissions_error_context.serialize_json(
                value["missing_permissions_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> PeeringError:
    out: PeeringError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_networkmanager.types.peering_error_code

        out["code"] = aws_sdk_networkmanager.types.peering_error_code.deserialize_json(
            data["Code"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "MissingPermissionsContext" in data:
        import aws_sdk_networkmanager.types.permissions_error_context

        out["missing_permissions_context"] = (
            aws_sdk_networkmanager.types.permissions_error_context.deserialize_json(
                data["MissingPermissionsContext"]
            )
        )
    return out
