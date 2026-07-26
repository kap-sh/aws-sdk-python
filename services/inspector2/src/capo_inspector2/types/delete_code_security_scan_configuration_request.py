"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.scan_configuration_arn


class DeleteCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCodeSecurityScanConfigurationRequest:
    out: DeleteCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteCodeSecurityScanConfigurationRequest.scan_configuration_arn required"
        )
    return out
