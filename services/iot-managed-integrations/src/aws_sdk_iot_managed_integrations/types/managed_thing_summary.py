"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ManagedThingSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.advertised_product_id
    import aws_sdk_iot_managed_integrations.types.brand
    import aws_sdk_iot_managed_integrations.types.classification
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.connector_device_id
    import aws_sdk_iot_managed_integrations.types.connector_policy_id
    import aws_sdk_iot_managed_integrations.types.created_at
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_arn
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.model
    import aws_sdk_iot_managed_integrations.types.name
    import aws_sdk_iot_managed_integrations.types.owner
    import aws_sdk_iot_managed_integrations.types.parent_controller_id
    import aws_sdk_iot_managed_integrations.types.provisioning_status
    import aws_sdk_iot_managed_integrations.types.role
    import aws_sdk_iot_managed_integrations.types.serial_number
    import aws_sdk_iot_managed_integrations.types.setup_at


class ManagedThingSummary(TypedDict):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the device.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_arn.ManagedThingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the managed thing.</p>"""
    advertised_product_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.advertised_product_id.AdvertisedProductId"
    ]
    """<p>The id of the advertised product.</p>"""
    brand: NotRequired["aws_sdk_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    classification: NotRequired[
        "aws_sdk_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    connector_device_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_policy_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
    ]
    """<p>The id of the connector policy.</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_destination_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination associated with this managed thing, if applicable.</p>"""
    model: NotRequired["aws_sdk_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    name: NotRequired["aws_sdk_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    owner: NotRequired["aws_sdk_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker for the managed thing.</p>"""
    parent_controller_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
    ]
    """<p>Id of the controller device used for the discovery job.</p>"""
    provisioning_status: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
    ]
    """<p>The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see <a href=\"https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html\">Device Provisioning</a>.</p>"""
    role: NotRequired["aws_sdk_iot_managed_integrations.types.role.Role"]
    """<p>The type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>"""
    serial_number: NotRequired[
        "aws_sdk_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the device creation request occurred.</p>"""
    updated_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the managed thing was last updated at.</p>"""
    activated_at: NotRequired["aws_sdk_iot_managed_integrations.types.setup_at.SetupAt"]
    """<p>The timestampe value of when the managed thing was activated at.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedThingSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "advertised_product_id" in value:
        out["AdvertisedProductId"] = value["advertised_product_id"]
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "connector_policy_id" in value:
        out["ConnectorPolicyId"] = value["connector_policy_id"]
    if "connector_destination_id" in value:
        out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "parent_controller_id" in value:
        out["ParentControllerId"] = value["parent_controller_id"]
    if "provisioning_status" in value:
        import aws_sdk_iot_managed_integrations.types.provisioning_status

        out["ProvisioningStatus"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_status.serialize_json(
                value["provisioning_status"]
            )
        )
    if "role" in value:
        import aws_sdk_iot_managed_integrations.types.role

        out["Role"] = aws_sdk_iot_managed_integrations.types.role.serialize_json(
            value["role"]
        )
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["UpdatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["updated_at"]
            )
        )
    if "activated_at" in value:
        import aws_sdk_iot_managed_integrations.types.setup_at

        out["ActivatedAt"] = (
            aws_sdk_iot_managed_integrations.types.setup_at.serialize_json(
                value["activated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedThingSummary:
    out: ManagedThingSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AdvertisedProductId" in data:
        out["advertised_product_id"] = data["AdvertisedProductId"]
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "ConnectorDeviceId" in data:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if "ConnectorPolicyId" in data:
        out["connector_policy_id"] = data["ConnectorPolicyId"]
    if "ConnectorDestinationId" in data:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "CredentialLockerId" in data:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if "ParentControllerId" in data:
        out["parent_controller_id"] = data["ParentControllerId"]
    if "ProvisioningStatus" in data:
        import aws_sdk_iot_managed_integrations.types.provisioning_status

        out["provisioning_status"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_status.deserialize_json(
                data["ProvisioningStatus"]
            )
        )
    if "Role" in data:
        import aws_sdk_iot_managed_integrations.types.role

        out["role"] = aws_sdk_iot_managed_integrations.types.role.deserialize_json(
            data["Role"]
        )
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["updated_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if "ActivatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.setup_at

        out["activated_at"] = (
            aws_sdk_iot_managed_integrations.types.setup_at.deserialize_json(
                data["ActivatedAt"]
            )
        )
    return out
