"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#UpdateManagedThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.brand
    import aws_sdk_iot_managed_integrations.types.capabilities
    import aws_sdk_iot_managed_integrations.types.capability_report
    import aws_sdk_iot_managed_integrations.types.capability_schemas
    import aws_sdk_iot_managed_integrations.types.classification
    import aws_sdk_iot_managed_integrations.types.credential_locker_id
    import aws_sdk_iot_managed_integrations.types.hub_network_mode
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.meta_data
    import aws_sdk_iot_managed_integrations.types.model
    import aws_sdk_iot_managed_integrations.types.name
    import aws_sdk_iot_managed_integrations.types.owner
    import aws_sdk_iot_managed_integrations.types.serial_number
    import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration


class UpdateManagedThingRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The id of the managed thing.</p>"""
    owner: NotRequired["aws_sdk_iot_managed_integrations.types.owner.Owner"]
    """<p>Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.</p>"""
    credential_locker_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.credential_locker_id.CredentialLockerId"
    ]
    """<p>The identifier of the credential for the managed thing.</p>"""
    serial_number: NotRequired[
        "aws_sdk_iot_managed_integrations.types.serial_number.SerialNumber"
    ]
    """<p>The serial number of the device.</p>"""
    wi_fi_simple_setup_configuration: NotRequired[
        "aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.WiFiSimpleSetupConfiguration"
    ]
    """<p>The Wi-Fi Simple Setup configuration for the managed thing, which defines provisioning capabilities and timeout settings.</p>"""
    brand: NotRequired["aws_sdk_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the device.</p>"""
    model: NotRequired["aws_sdk_iot_managed_integrations.types.model.Model"]
    """<p>The model of the device.</p>"""
    name: NotRequired["aws_sdk_iot_managed_integrations.types.name.Name"]
    """<p>The name of the managed thing representing the physical device.</p>"""
    capability_report: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capability_report.CapabilityReport"
    ]
    """<p>A report of the capabilities for the managed thing.</p>"""
    capability_schemas: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
    ]
    """<p>The updated capability schemas that define the functionality and features supported by the managed thing.</p>"""
    capabilities: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capabilities.Capabilities"
    ]
    """<p>The capabilities of the device such as light bulb.</p>"""
    classification: NotRequired[
        "aws_sdk_iot_managed_integrations.types.classification.Classification"
    ]
    """<p>The classification of the managed thing such as light bulb or thermostat.</p>"""
    hub_network_mode: NotRequired[
        "aws_sdk_iot_managed_integrations.types.hub_network_mode.HubNetworkMode"
    ]
    """<p>The network mode for the hub-connected device.</p>"""
    meta_data: NotRequired["aws_sdk_iot_managed_integrations.types.meta_data.MetaData"]
    """<p>The metadata for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateManagedThingRequest) -> dict:
    out: dict = {}
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "credential_locker_id" in value:
        out["CredentialLockerId"] = value["credential_locker_id"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "wi_fi_simple_setup_configuration" in value:
        import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["WiFiSimpleSetupConfiguration"] = (
            aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.serialize_json(
                value["wi_fi_simple_setup_configuration"]
            )
        )
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "model" in value:
        out["Model"] = value["model"]
    if "name" in value:
        out["Name"] = value["name"]
    if "capability_report" in value:
        import aws_sdk_iot_managed_integrations.types.capability_report

        out["CapabilityReport"] = (
            aws_sdk_iot_managed_integrations.types.capability_report.serialize_json(
                value["capability_report"]
            )
        )
    if "capability_schemas" in value:
        import aws_sdk_iot_managed_integrations.types.capability_schemas

        out["CapabilitySchemas"] = (
            aws_sdk_iot_managed_integrations.types.capability_schemas.serialize_json(
                value["capability_schemas"]
            )
        )
    if "capabilities" in value:
        out["Capabilities"] = value["capabilities"]
    if "classification" in value:
        out["Classification"] = value["classification"]
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
    return out


def deserialize_json(data: dict) -> UpdateManagedThingRequest:
    out: UpdateManagedThingRequest = {}  # type: ignore[typeddict-item]
    if "Owner" in data:
        out["owner"] = data["Owner"]
    if "CredentialLockerId" in data:
        out["credential_locker_id"] = data["CredentialLockerId"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "WiFiSimpleSetupConfiguration" in data:
        import aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration

        out["wi_fi_simple_setup_configuration"] = (
            aws_sdk_iot_managed_integrations.types.wi_fi_simple_setup_configuration.deserialize_json(
                data["WiFiSimpleSetupConfiguration"]
            )
        )
    if "Brand" in data:
        out["brand"] = data["Brand"]
    if "Model" in data:
        out["model"] = data["Model"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CapabilityReport" in data:
        import aws_sdk_iot_managed_integrations.types.capability_report

        out["capability_report"] = (
            aws_sdk_iot_managed_integrations.types.capability_report.deserialize_json(
                data["CapabilityReport"]
            )
        )
    if "CapabilitySchemas" in data:
        import aws_sdk_iot_managed_integrations.types.capability_schemas

        out["capability_schemas"] = (
            aws_sdk_iot_managed_integrations.types.capability_schemas.deserialize_json(
                data["CapabilitySchemas"]
            )
        )
    if "Capabilities" in data:
        out["capabilities"] = data["Capabilities"]
    if "Classification" in data:
        out["classification"] = data["Classification"]
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
    return out
