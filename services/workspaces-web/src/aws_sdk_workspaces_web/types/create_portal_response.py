"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreatePortalResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces_web.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.portal_endpoint

class CreatePortalResponse(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    portal_endpoint: "aws_sdk_workspaces_web.types.portal_endpoint.PortalEndpoint"
    """<p>The endpoint URL of the web portal that users access in order to start streaming sessions.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreatePortalResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["portalEndpoint"] = value["portal_endpoint"]
    return out


def deserialize_json(data: dict) -> CreatePortalResponse:
    out: CreatePortalResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("CreatePortalResponse.portal_arn required")
    if "portalEndpoint" in data:
        out["portal_endpoint"] = data["portalEndpoint"]
    else:
        raise DeserializationError("CreatePortalResponse.portal_endpoint required")
    return out