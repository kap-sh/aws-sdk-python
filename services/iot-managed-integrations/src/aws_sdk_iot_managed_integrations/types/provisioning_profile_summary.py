"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProvisioningProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_arn
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_id
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_name
    import aws_sdk_iot_managed_integrations.types.provisioning_profile_status
    import aws_sdk_iot_managed_integrations.types.provisioning_type


class ProvisioningProfileSummary(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_profile_name.ProvisioningProfileName"
    ]
    """<p>The name of the provisioning profile.</p>"""
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_profile_id.ProvisioningProfileId"
    ]
    """<p>The identifier of the provisioning profile.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_profile_arn.ProvisioningProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the provisioning profile.</p>"""
    provisioning_type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_type.ProvisioningType"
    ]
    """<p>The type of provisioning workflow the device uses for onboarding to IoT managed integrations.</p>"""
    status: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_profile_status.ProvisioningProfileStatus"
    ]
    """<p>The status of a provisioning profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningProfileSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "provisioning_type" in value:
        import aws_sdk_iot_managed_integrations.types.provisioning_type

        out["ProvisioningType"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_type.serialize_json(
                value["provisioning_type"]
            )
        )
    if "status" in value:
        import aws_sdk_iot_managed_integrations.types.provisioning_profile_status

        out["Status"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_profile_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProvisioningProfileSummary:
    out: ProvisioningProfileSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ProvisioningType" in data:
        import aws_sdk_iot_managed_integrations.types.provisioning_type

        out["provisioning_type"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_type.deserialize_json(
                data["ProvisioningType"]
            )
        )
    if "Status" in data:
        import aws_sdk_iot_managed_integrations.types.provisioning_profile_status

        out["status"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_profile_status.deserialize_json(
                data["Status"]
            )
        )
    return out
