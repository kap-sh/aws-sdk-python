"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.advertised_product_id
    import aws_sdk_iot_managed_integrations.types.brand
    import aws_sdk_iot_managed_integrations.types.classification
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.connector_device_id
    import aws_sdk_iot_managed_integrations.types.connector_policy_id
    import aws_sdk_iot_managed_integrations.types.created_at
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.device_specific_key
    import aws_sdk_iot_managed_integrations.types.hub_network_mode
    import aws_sdk_iot_managed_integrations.types.international_article_number
    import aws_sdk_iot_managed_integrations.types.mac_address
    import aws_sdk_iot_managed_integrations.types.managed_thing_arn
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.meta_data
    import aws_sdk_iot_managed_integrations.types.model
    import aws_sdk_iot_managed_integrations.types.name
    import aws_sdk_iot_managed_integrations.types.owner
    import aws_sdk_iot_managed_integrations.types.parent_controller_id
    import aws_sdk_iot_managed_integrations.types.provisioning_status
    import aws_sdk_iot_managed_integrations.types.role
    import aws_sdk_iot_managed_integrations.types.serial_number
    import aws_sdk_iot_managed_integrations.types.setup_at
    import aws_sdk_iot_managed_integrations.types.tags_map
    import aws_sdk_iot_managed_integrations.types.universal_product_code
    import aws_sdk_iot_managed_integrations.types.updated_at
    import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class GetManagedThingResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the managed thing.</p>"""
    arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_arn.ManagedThingArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the managed thing.</p>"""
    owner: NotRequired["aws_sdk_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential locker for the managed thing.</p>"""
    advertised_product_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.advertised_product_id.AdvertisedProductId"
    ]
    """<p>The id of the advertised product.</p>"""
    role: NotRequired["aws_sdk_iot_managed_integrations.types.role.Role"]
    """<p>The type of device used. This will be the Amazon Web Services hub controller, cloud device, or IoT device.</p>"""
    provisioning_status: NotRequired[
        "aws_sdk_iot_managed_integrations.types.provisioning_status.ProvisioningStatus"
    ]
    r"""<p>The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations. For more information, see <a href=\"https://docs.aws.amazon.com/iot-mi/latest/devguide/device-provisioning.html\">Device Provisioning</a>.</p>"""
    name: NotRequired["aws_sdk_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    model: NotRequired["aws_sdk_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    brand: NotRequired["aws_sdk_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    serial_number: NotRequired[
        "aws_sdk_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    universal_product_code: NotRequired[
        "aws_sdk_iot_managed_integrations.types.universal_product_code.UniversalProductCode"
    ]
    """<p>The universal product code (UPC) of the device model. The UPC is typically used in the United States of America and Canada.</p>"""
    international_article_number: NotRequired[
        "aws_sdk_iot_managed_integrations.types.international_article_number.InternationalArticleNumber"
    ]
    """<p>The unique 13 digit number that identifies the managed thing.</p>"""
    connector_policy_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_policy_id.ConnectorPolicyId"
    ]
    """<p>The id of the connector policy.</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_destination_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination associated with this managed thing.</p>"""
    connector_device_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device id as defined by the connector. This device id must not contain personal identifiable information (PII).</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    device_specific_key: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_specific_key.DeviceSpecificKey"
    ]
    """<p>A Zwave device-specific key used during device activation.</p> <note> <p>This parameter is used for Zwave devices only.</p> </note>"""
    mac_address: NotRequired[
        "aws_sdk_iot_managed_integrations.types.mac_address.MacAddress"
    ]
    """<p>The media access control (MAC) address for the device represented by the managed thing.</p> <note> <p>This parameter is used for Zigbee devices only.</p> </note>"""
    parent_controller_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.parent_controller_id.ParentControllerId"
    ]
    """<p>Id of the controller device used for the discovery job.</p>"""
    classification: NotRequired[
        "aws_sdk_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    created_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.created_at.CreatedAt"
    ]
    """<p>The timestamp value of when the device creation request occurred.</p>"""
    updated_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.updated_at.UpdatedAt"
    ]
    """<p>The timestamp value of when the managed thing was last updated at.</p>"""
    activated_at: NotRequired["aws_sdk_iot_managed_integrations.types.setup_at.SetupAt"]
    """<p>The timestampe value of when the device was activated.</p>"""
    hub_network_mode: NotRequired[
        "aws_sdk_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
    ]
    """<p>The network mode for the hub-connected device.</p>"""
    meta_data: NotRequired["aws_sdk_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""
    tags: NotRequired["aws_sdk_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the managed thing.</p>"""
    wi_fi_simple_setup_configuration: NotRequired[
        "aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
    ]
    """<p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "advertised_product_id" in value:
        out["AdvertisedProductId"] = value["advertised_product_id"]
    if "role" in value:
        import aws_sdk_iot_managed_integrations.types.role

        out["Role"] = aws_sdk_iot_managed_integrations.types.role.serialize_json(
            value["role"]
        )
    if "provisioning_status" in value:
        import aws_sdk_iot_managed_integrations.types.provisioning_status

        out["ProvisioningStatus"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_status.serialize_json(
                value["provisioning_status"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "model" in value:
        out["Model"] = value["model"]
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "universal_product_code" in value:
        out["UniversalProductCode"] = value["universal_product_code"]
    if "international_article_number" in value:
        out["InternationalArticleNumber"] = value["international_article_number"]
    if "connector_policy_id" in value:
        out["ConnectorPolicyId"] = value["connector_policy_id"]
    if "connector_destination_id" in value:
        out["ConnectorDestinationId"] = value["connector_destination_id"]
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "device_specific_key" in value:
        out["DeviceSpecificKey"] = value["device_specific_key"]
    if "mac_address" in value:
        out["MacAddress"] = value["mac_address"]
    if "parent_controller_id" in value:
        out["ParentControllerId"] = value["parent_controller_id"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "created_at" in value:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["CreatedAt"] = (
            aws_sdk_iot_managed_integrations.types.created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_iot_managed_integrations.types.updated_at

        out["UpdatedAt"] = (
            aws_sdk_iot_managed_integrations.types.updated_at.serialize_json(
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
    if "hub_network_mode" in value:
        import aws_sdk_iot_managed_integrations.types.hub_network_mode

        out["HubNetworkMode"] = (
            aws_sdk_iot_managed_integrations.types.hub_network_mode.serialize_json(
                value["hub_network_mode"]
            )
        )
    if "meta_data" in value:
        import aws_sdk_iot_managed_integrations.types.meta_data

        out["MetaData"] = (
            aws_sdk_iot_managed_integrations.types.meta_data.serialize_json(
                value["meta_data"]
            )
        )
    if "tags" in value:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["Tags"] = aws_sdk_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    if "wi_fi_simple_setup_configuration" in value:
        import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["WiFiSimpleSetupConfiguration"] = (
            aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.serialize_json(
                value["wi_fi_simple_setup_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingResponse:
    out: GetManagedThingResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "CredentialLockerId" in data:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if "AdvertisedProductId" in data:
        out["advertised_product_id"] = data["AdvertisedProductId"]
    if "Role" in data:
        import aws_sdk_iot_managed_integrations.types.role

        out["role"] = aws_sdk_iot_managed_integrations.types.role.deserialize_json(
            data["Role"]
        )
    if "ProvisioningStatus" in data:
        import aws_sdk_iot_managed_integrations.types.provisioning_status

        out["provisioning_status"] = (
            aws_sdk_iot_managed_integrations.types.provisioning_status.deserialize_json(
                data["ProvisioningStatus"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "UniversalProductCode" in data:
        out["universal_product_code"] = data["UniversalProductCode"]
    if "InternationalArticleNumber" in data:
        out["international_article_number"] = data["InternationalArticleNumber"]
    if "ConnectorPolicyId" in data:
        out["connector_policy_id"] = data["ConnectorPolicyId"]
    if "ConnectorDestinationId" in data:
        out["connector_destination_id"] = data["ConnectorDestinationId"]
    if "ConnectorDeviceId" in data:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if "DeviceSpecificKey" in data:
        out["device_specific_key"] = data["DeviceSpecificKey"]
    if "MacAddress" in data:
        out["mac_address"] = data["MacAddress"]
    if "ParentControllerId" in data:
        out["parent_controller_id"] = data["ParentControllerId"]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "CreatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.created_at

        out["created_at"] = (
            aws_sdk_iot_managed_integrations.types.created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_iot_managed_integrations.types.updated_at

        out["updated_at"] = (
            aws_sdk_iot_managed_integrations.types.updated_at.deserialize_json(
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
    if "HubNetworkMode" in data:
        import aws_sdk_iot_managed_integrations.types.hub_network_mode

        out["hub_network_mode"] = (
            aws_sdk_iot_managed_integrations.types.hub_network_mode.deserialize_json(
                data["HubNetworkMode"]
            )
        )
    if "MetaData" in data:
        import aws_sdk_iot_managed_integrations.types.meta_data

        out["meta_data"] = (
            aws_sdk_iot_managed_integrations.types.meta_data.deserialize_json(
                data["MetaData"]
            )
        )
    if "Tags" in data:
        import aws_sdk_iot_managed_integrations.types.tags_map

        out["tags"] = aws_sdk_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    if "WiFiSimpleSetupConfiguration" in data:
        import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["wi_fi_simple_setup_configuration"] = (
            aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.deserialize_json(
                data["WiFiSimpleSetupConfiguration"]
            )
        )
    return out
