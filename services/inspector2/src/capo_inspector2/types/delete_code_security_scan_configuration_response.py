"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scan_configuration_arn


class DeleteCodeSecurityScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: NotRequired[
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
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
