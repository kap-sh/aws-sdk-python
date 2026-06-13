"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.scan_configuration_arn


class CreateCodeSecurityScanConfigurationResponse(TypedDict):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityScanConfigurationResponse:
    out: CreateCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateCodeSecurityScanConfigurationResponse.scan_configuration_arn required"
        )
    return out
