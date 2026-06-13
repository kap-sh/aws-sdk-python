"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCisScanConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configuration_arn


class DeleteCisScanConfigurationResponse(TypedDict):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The ARN of the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCisScanConfigurationResponse) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCisScanConfigurationResponse:
    out: DeleteCisScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "DeleteCisScanConfigurationResponse.scan_configuration_arn required"
        )
    return out
