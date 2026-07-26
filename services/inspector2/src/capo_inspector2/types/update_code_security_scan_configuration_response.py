"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scan_configuration_arn


class UpdateCodeSecurityScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: NotRequired[
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the updated scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    if "scan_configuration_arn" in value:
        out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityScanConfigurationResponse:
    out: UpdateCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    return out
