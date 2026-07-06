"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredDeviceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.auth_material_string
    import aws_sdk_iot_managed_integrations.types.brand
    import aws_sdk_iot_managed_integrations.types.connector_device_id
    import aws_sdk_iot_managed_integrations.types.connector_device_name
    import aws_sdk_iot_managed_integrations.types.device_type_list
    import aws_sdk_iot_managed_integrations.types.discovered_at
    import aws_sdk_iot_managed_integrations.types.discovery_modification
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.model


class DiscoveredDeviceSummary(TypedDict, closed=True):
    connector_device_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device identifier as defined by the connector. This identifier must not contain personal identifiable information (PII).</p>"""
    connector_device_name: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_device_name.ConnectorDeviceName"
    ]
    """<p>The name of the device as defined by the connector or third-party system.</p>"""
    device_types: NotRequired[
        "aws_sdk_iot_managed_integrations.types.device_type_list.DeviceTypeList"
    ]
    """<p>The list of device types or categories that the discovered device belongs to.</p>"""
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing created for this discovered device, if one exists.</p>"""
    modification: NotRequired[
        "aws_sdk_iot_managed_integrations.types.discovery_modification.DiscoveryModification"
    ]
    """<p>The status of the discovered device, indicating whether it has been added, removed, or modified since the last discovery.</p>"""
    discovered_at: NotRequired[
        "aws_sdk_iot_managed_integrations.types.discovered_at.DiscoveredAt"
    ]
    """<p>The timestamp indicating when the device was discovered.</p>"""
    brand: NotRequired["aws_sdk_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the discovered device.</p>"""
    model: NotRequired["aws_sdk_iot_managed_integrations.types.model.Model"]
    """<p>The model of the discovered device.</p>"""
    authentication_material: NotRequired[
        "aws_sdk_iot_managed_integrations.types.auth_material_string.AuthMaterialString"
    ]
    """<p>The authentication material required for connecting to the discovered device, such as credentials or tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredDeviceSummary) -> dict:
    out: dict = {}
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "connector_device_name" in value:
        out["ConnectorDeviceName"] = value["connector_device_name"]
    if "device_types" in value:
        import aws_sdk_iot_managed_integrations.types.device_type_list

        out["DeviceTypes"] = (
            aws_sdk_iot_managed_integrations.types.device_type_list.serialize_json(
                value["device_types"]
            )
        )
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "modification" in value:
        import aws_sdk_iot_managed_integrations.types.discovery_modification

        out["Modification"] = (
            aws_sdk_iot_managed_integrations.types.discovery_modification.serialize_json(
                value["modification"]
            )
        )
    if "discovered_at" in value:
        import aws_sdk_iot_managed_integrations.types.discovered_at

        out["DiscoveredAt"] = (
            aws_sdk_iot_managed_integrations.types.discovered_at.serialize_json(
                value["discovered_at"]
            )
        )
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "model" in value:
        out["Model"] = value["model"]
    if "authentication_material" in value:
        out["AuthenticationMaterial"] = value["authentication_material"]
    return out


def deserialize_json(data: dict) -> DiscoveredDeviceSummary:
    out: DiscoveredDeviceSummary = {}  # type: ignore[typeddict-item]
    if "ConnectorDeviceId" in data:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if "ConnectorDeviceName" in data:
        out["connector_device_name"] = data["ConnectorDeviceName"]
    if "DeviceTypes" in data:
        import aws_sdk_iot_managed_integrations.types.device_type_list

        out["device_types"] = (
            aws_sdk_iot_managed_integrations.types.device_type_list.deserialize_json(
                data["DeviceTypes"]
            )
        )
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "Modification" in data:
        import aws_sdk_iot_managed_integrations.types.discovery_modification

        out["modification"] = (
            aws_sdk_iot_managed_integrations.types.discovery_modification.deserialize_json(
                data["Modification"]
            )
        )
    if "DiscoveredAt" in data:
        import aws_sdk_iot_managed_integrations.types.discovered_at

        out["discovered_at"] = (
            aws_sdk_iot_managed_integrations.types.discovered_at.deserialize_json(
                data["DiscoveredAt"]
            )
        )
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "AuthenticationMaterial" in data:
        out["authentication_material"] = data["AuthenticationMaterial"]
    return out
