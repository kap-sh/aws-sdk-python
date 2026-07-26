"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCisScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration_arn


class CreateCisScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: NotRequired[
        "capo_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    ]
    """<p>The scan configuration ARN for the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCisScanConfigurationResponse) -> dict:
    out: dict = {}
    if "scan_configuration_arn" in value:
        out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateCisScanConfigurationResponse:
    out: CreateCisScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    return out
