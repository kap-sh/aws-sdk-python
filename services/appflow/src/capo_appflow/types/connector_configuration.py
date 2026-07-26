"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.arn
    import capo_appflow.types.authentication_config
    import capo_appflow.types.boolean
    import capo_appflow.types.connector_description
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_metadata
    import capo_appflow.types.connector_mode_list
    import capo_appflow.types.connector_name
    import capo_appflow.types.connector_owner
    import capo_appflow.types.connector_provisioning_config
    import capo_appflow.types.connector_provisioning_type
    import capo_appflow.types.connector_runtime_setting_list
    import capo_appflow.types.connector_type
    import capo_appflow.types.connector_type_list
    import capo_appflow.types.connector_version
    import capo_appflow.types.date
    import capo_appflow.types.logo_url
    import capo_appflow.types.registered_by
    import capo_appflow.types.scheduling_frequency_type_list
    import capo_appflow.types.supported_api_version_list
    import capo_appflow.types.supported_data_transfer_apis
    import capo_appflow.types.supported_data_transfer_type_list
    import capo_appflow.types.supported_operator_list
    import capo_appflow.types.supported_write_operation_list
    import capo_appflow.types.trigger_type_list


class ConnectorConfiguration(TypedDict, closed=True):
    can_use_as_source: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies whether the connector can be used as a source. </p>"""
    can_use_as_destination: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies whether the connector can be used as a destination. </p>"""
    supported_destination_connectors: NotRequired[
        "capo_appflow.types.connector_type_list.ConnectorTypeList"
    ]
    """<p> Lists the connectors that are available for use as destinations. </p>"""
    supported_scheduling_frequencies: NotRequired[
        "capo_appflow.types.scheduling_frequency_type_list.SchedulingFrequencyTypeList"
    ]
    """<p> Specifies the supported flow frequency for that connector. </p>"""
    is_private_link_enabled: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if PrivateLink is enabled for that connector. </p>"""
    is_private_link_endpoint_url_required: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if a PrivateLink endpoint URL is required. </p>"""
    supported_trigger_types: NotRequired[
        "capo_appflow.types.trigger_type_list.TriggerTypeList"
    ]
    """<p> Specifies the supported trigger types for the flow. </p>"""
    connector_metadata: NotRequired[
        "capo_appflow.types.connector_metadata.ConnectorMetadata"
    ]
    """<p> Specifies connector-specific metadata such as <code>oAuthScopes</code>, <code>supportedRegions</code>, <code>privateLinkServiceUrl</code>, and so on. </p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p>The connector type.</p>"""
    connector_label: NotRequired["capo_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label used for registering the connector.</p>"""
    connector_description: NotRequired[
        "capo_appflow.types.connector_description.ConnectorDescription"
    ]
    """<p>A description about the connector.</p>"""
    connector_owner: NotRequired["capo_appflow.types.connector_owner.ConnectorOwner"]
    """<p>The owner who developed the connector.</p>"""
    connector_name: NotRequired["capo_appflow.types.connector_name.ConnectorName"]
    """<p>The connector name.</p>"""
    connector_version: NotRequired[
        "capo_appflow.types.connector_version.ConnectorVersion"
    ]
    """<p>The connector version.</p>"""
    connector_arn: NotRequired["capo_appflow.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the registered connector.</p>"""
    connector_modes: NotRequired[
        "capo_appflow.types.connector_mode_list.ConnectorModeList"
    ]
    """<p>The connection modes that the connector supports.</p>"""
    authentication_config: NotRequired[
        "capo_appflow.types.authentication_config.AuthenticationConfig"
    ]
    """<p>The authentication config required for the connector.</p>"""
    connector_runtime_settings: NotRequired[
        "capo_appflow.types.connector_runtime_setting_list.ConnectorRuntimeSettingList"
    ]
    """<p>The required connector runtime settings.</p>"""
    supported_api_versions: NotRequired[
        "capo_appflow.types.supported_api_version_list.SupportedApiVersionList"
    ]
    """<p>A list of API versions that are supported by the connector.</p>"""
    supported_operators: NotRequired[
        "capo_appflow.types.supported_operator_list.SupportedOperatorList"
    ]
    """<p>A list of operators supported by the connector.</p>"""
    supported_write_operations: NotRequired[
        "capo_appflow.types.supported_write_operation_list.SupportedWriteOperationList"
    ]
    """<p>A list of write operations supported by the connector.</p>"""
    connector_provisioning_type: NotRequired[
        "capo_appflow.types.connector_provisioning_type.ConnectorProvisioningType"
    ]
    """<p>The provisioning type used to register the connector.</p>"""
    connector_provisioning_config: NotRequired[
        "capo_appflow.types.connector_provisioning_config.ConnectorProvisioningConfig"
    ]
    """<p>The configuration required for registering the connector.</p>"""
    logo_url: NotRequired["capo_appflow.types.logo_url.LogoURL"]
    """<p>Logo URL of the connector.</p>"""
    registered_at: NotRequired["capo_appflow.types.date.Date"]
    """<p>The date on which the connector was registered.</p>"""
    registered_by: NotRequired["capo_appflow.types.registered_by.RegisteredBy"]
    """<p>Information about who registered the connector.</p>"""
    supported_data_transfer_types: NotRequired[
        "capo_appflow.types.supported_data_transfer_type_list.SupportedDataTransferTypeList"
    ]
    """<p>The data transfer types that the connector supports.</p> <dl> <dt>RECORD</dt> <dd> <p>Structured records.</p> </dd> <dt>FILE</dt> <dd> <p>Files or binary data.</p> </dd> </dl>"""
    supported_data_transfer_apis: NotRequired[
        "capo_appflow.types.supported_data_transfer_apis.SupportedDataTransferApis"
    ]
    """<p>The APIs of the connector application that Amazon AppFlow can use to transfer your data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfiguration) -> dict:
    out: dict = {}
    out["canUseAsSource"] = value.get("can_use_as_source", False)
    out["canUseAsDestination"] = value.get("can_use_as_destination", False)
    if "supported_destination_connectors" in value:
        import capo_appflow.types.connector_type_list

        out["supportedDestinationConnectors"] = (
            capo_appflow.types.connector_type_list.serialize_json(
                value["supported_destination_connectors"]
            )
        )
    if "supported_scheduling_frequencies" in value:
        import capo_appflow.types.scheduling_frequency_type_list

        out["supportedSchedulingFrequencies"] = (
            capo_appflow.types.scheduling_frequency_type_list.serialize_json(
                value["supported_scheduling_frequencies"]
            )
        )
    out["isPrivateLinkEnabled"] = value.get("is_private_link_enabled", False)
    out["isPrivateLinkEndpointUrlRequired"] = value.get(
        "is_private_link_endpoint_url_required", False
    )
    if "supported_trigger_types" in value:
        import capo_appflow.types.trigger_type_list

        out["supportedTriggerTypes"] = (
            capo_appflow.types.trigger_type_list.serialize_json(
                value["supported_trigger_types"]
            )
        )
    if "connector_metadata" in value:
        import capo_appflow.types.connector_metadata

        out["connectorMetadata"] = capo_appflow.types.connector_metadata.serialize_json(
            value["connector_metadata"]
        )
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    if "connector_description" in value:
        out["connectorDescription"] = value["connector_description"]
    if "connector_owner" in value:
        out["connectorOwner"] = value["connector_owner"]
    if "connector_name" in value:
        out["connectorName"] = value["connector_name"]
    if "connector_version" in value:
        out["connectorVersion"] = value["connector_version"]
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_modes" in value:
        import capo_appflow.types.connector_mode_list

        out["connectorModes"] = capo_appflow.types.connector_mode_list.serialize_json(
            value["connector_modes"]
        )
    if "authentication_config" in value:
        import capo_appflow.types.authentication_config

        out["authenticationConfig"] = (
            capo_appflow.types.authentication_config.serialize_json(
                value["authentication_config"]
            )
        )
    if "connector_runtime_settings" in value:
        import capo_appflow.types.connector_runtime_setting_list

        out["connectorRuntimeSettings"] = (
            capo_appflow.types.connector_runtime_setting_list.serialize_json(
                value["connector_runtime_settings"]
            )
        )
    if "supported_api_versions" in value:
        import capo_appflow.types.supported_api_version_list

        out["supportedApiVersions"] = (
            capo_appflow.types.supported_api_version_list.serialize_json(
                value["supported_api_versions"]
            )
        )
    if "supported_operators" in value:
        import capo_appflow.types.supported_operator_list

        out["supportedOperators"] = (
            capo_appflow.types.supported_operator_list.serialize_json(
                value["supported_operators"]
            )
        )
    if "supported_write_operations" in value:
        import capo_appflow.types.supported_write_operation_list

        out["supportedWriteOperations"] = (
            capo_appflow.types.supported_write_operation_list.serialize_json(
                value["supported_write_operations"]
            )
        )
    if "connector_provisioning_type" in value:
        import capo_appflow.types.connector_provisioning_type

        out["connectorProvisioningType"] = (
            capo_appflow.types.connector_provisioning_type.serialize_json(
                value["connector_provisioning_type"]
            )
        )
    if "connector_provisioning_config" in value:
        import capo_appflow.types.connector_provisioning_config

        out["connectorProvisioningConfig"] = (
            capo_appflow.types.connector_provisioning_config.serialize_json(
                value["connector_provisioning_config"]
            )
        )
    if "logo_url" in value:
        out["logoURL"] = value["logo_url"]
    if "registered_at" in value:
        import capo_appflow.types.date

        out["registeredAt"] = capo_appflow.types.date.serialize_json(
            value["registered_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "supported_data_transfer_types" in value:
        import capo_appflow.types.supported_data_transfer_type_list

        out["supportedDataTransferTypes"] = (
            capo_appflow.types.supported_data_transfer_type_list.serialize_json(
                value["supported_data_transfer_types"]
            )
        )
    if "supported_data_transfer_apis" in value:
        import capo_appflow.types.supported_data_transfer_apis

        out["supportedDataTransferApis"] = (
            capo_appflow.types.supported_data_transfer_apis.serialize_json(
                value["supported_data_transfer_apis"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorConfiguration:
    out: ConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if "canUseAsSource" in data:
        out["can_use_as_source"] = data["canUseAsSource"]
    else:
        out["can_use_as_source"] = False
    if "canUseAsDestination" in data:
        out["can_use_as_destination"] = data["canUseAsDestination"]
    else:
        out["can_use_as_destination"] = False
    if "supportedDestinationConnectors" in data:
        import capo_appflow.types.connector_type_list

        out["supported_destination_connectors"] = (
            capo_appflow.types.connector_type_list.deserialize_json(
                data["supportedDestinationConnectors"]
            )
        )
    if "supportedSchedulingFrequencies" in data:
        import capo_appflow.types.scheduling_frequency_type_list

        out["supported_scheduling_frequencies"] = (
            capo_appflow.types.scheduling_frequency_type_list.deserialize_json(
                data["supportedSchedulingFrequencies"]
            )
        )
    if "isPrivateLinkEnabled" in data:
        out["is_private_link_enabled"] = data["isPrivateLinkEnabled"]
    else:
        out["is_private_link_enabled"] = False
    if "isPrivateLinkEndpointUrlRequired" in data:
        out["is_private_link_endpoint_url_required"] = data[
            "isPrivateLinkEndpointUrlRequired"
        ]
    else:
        out["is_private_link_endpoint_url_required"] = False
    if "supportedTriggerTypes" in data:
        import capo_appflow.types.trigger_type_list

        out["supported_trigger_types"] = (
            capo_appflow.types.trigger_type_list.deserialize_json(
                data["supportedTriggerTypes"]
            )
        )
    if "connectorMetadata" in data:
        import capo_appflow.types.connector_metadata

        out["connector_metadata"] = (
            capo_appflow.types.connector_metadata.deserialize_json(
                data["connectorMetadata"]
            )
        )
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    if "connectorDescription" in data:
        out["connector_description"] = data["connectorDescription"]
    if "connectorOwner" in data:
        out["connector_owner"] = data["connectorOwner"]
    if "connectorName" in data:
        out["connector_name"] = data["connectorName"]
    if "connectorVersion" in data:
        out["connector_version"] = data["connectorVersion"]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorModes" in data:
        import capo_appflow.types.connector_mode_list

        out["connector_modes"] = (
            capo_appflow.types.connector_mode_list.deserialize_json(
                data["connectorModes"]
            )
        )
    if "authenticationConfig" in data:
        import capo_appflow.types.authentication_config

        out["authentication_config"] = (
            capo_appflow.types.authentication_config.deserialize_json(
                data["authenticationConfig"]
            )
        )
    if "connectorRuntimeSettings" in data:
        import capo_appflow.types.connector_runtime_setting_list

        out["connector_runtime_settings"] = (
            capo_appflow.types.connector_runtime_setting_list.deserialize_json(
                data["connectorRuntimeSettings"]
            )
        )
    if "supportedApiVersions" in data:
        import capo_appflow.types.supported_api_version_list

        out["supported_api_versions"] = (
            capo_appflow.types.supported_api_version_list.deserialize_json(
                data["supportedApiVersions"]
            )
        )
    if "supportedOperators" in data:
        import capo_appflow.types.supported_operator_list

        out["supported_operators"] = (
            capo_appflow.types.supported_operator_list.deserialize_json(
                data["supportedOperators"]
            )
        )
    if "supportedWriteOperations" in data:
        import capo_appflow.types.supported_write_operation_list

        out["supported_write_operations"] = (
            capo_appflow.types.supported_write_operation_list.deserialize_json(
                data["supportedWriteOperations"]
            )
        )
    if "connectorProvisioningType" in data:
        import capo_appflow.types.connector_provisioning_type

        out["connector_provisioning_type"] = (
            capo_appflow.types.connector_provisioning_type.deserialize_json(
                data["connectorProvisioningType"]
            )
        )
    if "connectorProvisioningConfig" in data:
        import capo_appflow.types.connector_provisioning_config

        out["connector_provisioning_config"] = (
            capo_appflow.types.connector_provisioning_config.deserialize_json(
                data["connectorProvisioningConfig"]
            )
        )
    if "logoURL" in data:
        out["logo_url"] = data["logoURL"]
    if "registeredAt" in data:
        import capo_appflow.types.date

        out["registered_at"] = capo_appflow.types.date.deserialize_json(
            data["registeredAt"]
        )
    if "registeredBy" in data:
        out["registered_by"] = data["registeredBy"]
    if "supportedDataTransferTypes" in data:
        import capo_appflow.types.supported_data_transfer_type_list

        out["supported_data_transfer_types"] = (
            capo_appflow.types.supported_data_transfer_type_list.deserialize_json(
                data["supportedDataTransferTypes"]
            )
        )
    if "supportedDataTransferApis" in data:
        import capo_appflow.types.supported_data_transfer_apis

        out["supported_data_transfer_apis"] = (
            capo_appflow.types.supported_data_transfer_apis.deserialize_json(
                data["supportedDataTransferApis"]
            )
        )
    return out
