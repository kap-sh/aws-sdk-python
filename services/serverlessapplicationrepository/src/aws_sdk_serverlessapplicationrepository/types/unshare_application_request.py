"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#UnshareApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class UnshareApplicationRequest(TypedDict):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    organization_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The AWS Organization ID to unshare the application from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnshareApplicationRequest) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    return out


def deserialize_json(data: dict) -> UnshareApplicationRequest:
    out: UnshareApplicationRequest = {}  # type: ignore[typeddict-item]
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    return out
