"""Generated from Smithy shape ``com.amazonaws.grafana#DisassociateLicenseRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_grafana.types.license_type
    import aws_sdk_grafana.types.workspace_id


class DisassociateLicenseRequest(TypedDict):
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to remove the Grafana Enterprise license from.</p>"""
    license_type: "aws_sdk_grafana.types.license_type.LicenseType"
    """<p>The type of license to remove from the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateLicenseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateLicenseRequest:
    out: DisassociateLicenseRequest = {}  # type: ignore[typeddict-item]
    return out
