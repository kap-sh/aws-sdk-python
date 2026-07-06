"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCisScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configuration_arn


class UpdateCisScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The CIS scan configuration ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCisScanConfigurationResponse) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCisScanConfigurationResponse:
    out: UpdateCisScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateCisScanConfigurationResponse.scan_configuration_arn required"
        )
    return out
