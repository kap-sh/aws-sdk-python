"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.scan_configuration_arn


class DeleteCodeSecurityScanConfigurationResponse(TypedDict):
    scan_configuration_arn: NotRequired[
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    if "scan_configuration_arn" in value:
        out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCodeSecurityScanConfigurationResponse:
    out: DeleteCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    return out
