"""Generated from Smithy shape ``com.amazonaws.licensemanager#OrganizationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.boolean


class OrganizationConfiguration(TypedDict):
    enable_integration: "aws_sdk_license_manager.types.boolean.Boolean"
    """<p>Enables Organizations integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConfiguration) -> dict:
    out: dict = {}
    out["EnableIntegration"] = value.get("enable_integration", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> OrganizationConfiguration:
    out: OrganizationConfiguration = {}  # type: ignore[typeddict-item]
    if "EnableIntegration" in data:
        out["enable_integration"] = data["EnableIntegration"]
    else:
        out["enable_integration"] = False
    return out
