"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn
    import aws_sdk_appflow.types.authentication_config
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.connector_description
    import aws_sdk_appflow.types.connector_label
    import aws_sdk_appflow.types.connector_metadata
    import aws_sdk_appflow.types.connector_mode_list
    import aws_sdk_appflow.types.connector_name
    import aws_sdk_appflow.types.connector_owner
    import aws_sdk_appflow.types.connector_provisioning_config
    import aws_sdk_appflow.types.connector_provisioning_type
    import aws_sdk_appflow.types.connector_runtime_setting_list
    import aws_sdk_appflow.types.connector_type
    import aws_sdk_appflow.types.connector_type_list
    import aws_sdk_appflow.types.connector_version
    import aws_sdk_appflow.types.date
    import aws_sdk_appflow.types.logo_url
    import aws_sdk_appflow.types.registered_by
    import aws_sdk_appflow.types.scheduling_frequency_type_list
    import aws_sdk_appflow.types.supported_api_version_list
    import aws_sdk_appflow.types.supported_data_transfer_apis
    import aws_sdk_appflow.types.supported_data_transfer_type_list
    import aws_sdk_appflow.types.supported_operator_list
    import aws_sdk_appflow.types.supported_write_operation_list
    import aws_sdk_appflow.types.trigger_type_list


class ConnectorConfiguration(TypedDict):
    can_use_as_source: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Specifies whether the connector can be used as a source. </p>"""
    can_use_as_destination: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Specifies whether the connector can be used as a destination. </p>"""
    supported_destination_connectors: NotRequired[
        "aws_sdk_appflow.types.connector_type_list.ConnectorTypeList"
    ]
    """<p> Lists the connectors that are available for use as destinations. </p>"""
    supported_scheduling_frequencies: NotRequired[
        "aws_sdk_appflow.types.scheduling_frequency_type_list.SchedulingFrequencyTypeList"
    ]
    """<p> Specifies the supported flow frequency for that connector. </p>"""
    is_private_link_enabled: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Specifies if PrivateLink is enabled for that connector. </p>"""
    is_private_link_endpoint_url_required: "aws_sdk_appflow.types.boolean.Boolean"
    """<p> Specifies if a PrivateLink endpoint URL is required. </p>"""
    supported_trigger_types: NotRequired[
        "aws_sdk_appflow.types.trigger_type_list.TriggerTypeList"
    ]
    """<p> Specifies the supported trigger types for the flow. </p>"""
    connector_metadata: NotRequired[
        "aws_sdk_appflow.types.connector_metadata.ConnectorMetadata"
    ]
    """<p> Specifies connector-specific metadata such as <code>oAuthScopes</code>, <code>supportedRegions</code>, <code>privateLinkServiceUrl</code>, and so on. </p>"""
    connector_type: NotRequired["aws_sdk_appflow.types.connector_type.ConnectorType"]
    """<p>The connector type.</p>"""
    connector_label: NotRequired["aws_sdk_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label used for registering the connector.</p>"""
    connector_description: NotRequired[
        "aws_sdk_appflow.types.connector_description.ConnectorDescription"
    ]
    """<p>A description about the connector.</p>"""
    connector_owner: NotRequired["aws_sdk_appflow.types.connector_owner.ConnectorOwner"]
    """<p>The owner who developed the connector.</p>"""
    connector_name: NotRequired["aws_sdk_appflow.types.connector_name.ConnectorName"]
    """<p>The connector name.</p>"""
    connector_version: NotRequired[
        "aws_sdk_appflow.types.connector_version.ConnectorVersion"
    ]
    """<p>The connector version.</p>"""
    connector_arn: NotRequired["aws_sdk_appflow.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for the registered connector.</p>"""
    connector_modes: NotRequired[
        "aws_sdk_appflow.types.connector_mode_list.ConnectorModeList"
    ]
    """<p>The connection modes that the connector supports.</p>"""
    authentication_config: NotRequired[
        "aws_sdk_appflow.types.authentication_config.AuthenticationConfig"
    ]
    """<p>The authentication config required for the connector.</p>"""
    connector_runtime_settings: NotRequired[
        "aws_sdk_appflow.types.connector_runtime_setting_list.ConnectorRuntimeSettingList"
    ]
    """<p>The required connector runtime settings.</p>"""
    supported_api_versions: NotRequired[
        "aws_sdk_appflow.types.supported_api_version_list.SupportedApiVersionList"
    ]
    """<p>A list of API versions that are supported by the connector.</p>"""
    supported_operators: NotRequired[
        "aws_sdk_appflow.types.supported_operator_list.SupportedOperatorList"
    ]
    """<p>A list of operators supported by the connector.</p>"""
    supported_write_operations: NotRequired[
        "aws_sdk_appflow.types.supported_write_operation_list.SupportedWriteOperationList"
    ]
    """<p>A list of write operations supported by the connector.</p>"""
    connector_provisioning_type: NotRequired[
        "aws_sdk_appflow.types.connector_provisioning_type.ConnectorProvisioningType"
    ]
    """<p>The provisioning type used to register the connector.</p>"""
    connector_provisioning_config: NotRequired[
        "aws_sdk_appflow.types.connector_provisioning_config.ConnectorProvisioningConfig"
    ]
    """<p>The configuration required for registering the connector.</p>"""
    logo_url: NotRequired["aws_sdk_appflow.types.logo_url.LogoURL"]
    """<p>Logo URL of the connector.</p>"""
    registered_at: NotRequired["aws_sdk_appflow.types.date.Date"]
    """<p>The date on which the connector was registered.</p>"""
    registered_by: NotRequired["aws_sdk_appflow.types.registered_by.RegisteredBy"]
    """<p>Information about who registered the connector.</p>"""
    supported_data_transfer_types: NotRequired[
        "aws_sdk_appflow.types.supported_data_transfer_type_list.SupportedDataTransferTypeList"
    ]
    """<p>The data transfer types that the connector supports.</p> <dl> <dt>RECORD</dt> <dd> <p>Structured records.</p> </dd> <dt>FILE</dt> <dd> <p>Files or binary data.</p> </dd> </dl>"""
    supported_data_transfer_apis: NotRequired[
        "aws_sdk_appflow.types.supported_data_transfer_apis.SupportedDataTransferApis"
    ]
    """<p>The APIs of the connector application that Amazon AppFlow can use to transfer your data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfiguration) -> dict:
    out: dict = {}
    out["canUseAsSource"] = value.get("can_use_as_source", False)
    out["canUseAsDestination"] = value.get("can_use_as_destination", False)
    if "supported_destination_connectors" in value:
        import aws_sdk_appflow.types.connector_type_list

        out["supportedDestinationConnectors"] = (
            aws_sdk_appflow.types.connector_type_list.serialize_json(
                value["supported_destination_connectors"]
            )
        )
    if "supported_scheduling_frequencies" in value:
        import aws_sdk_appflow.types.scheduling_frequency_type_list

        out["supportedSchedulingFrequencies"] = (
            aws_sdk_appflow.types.scheduling_frequency_type_list.serialize_json(
                value["supported_scheduling_frequencies"]
            )
        )
    out["isPrivateLinkEnabled"] = value.get("is_private_link_enabled", False)
    out["isPrivateLinkEndpointUrlRequired"] = value.get(
        "is_private_link_endpoint_url_required", False
    )
    if "supported_trigger_types" in value:
        import aws_sdk_appflow.types.trigger_type_list

        out["supportedTriggerTypes"] = (
            aws_sdk_appflow.types.trigger_type_list.serialize_json(
                value["supported_trigger_types"]
            )
        )
    if "connector_metadata" in value:
        import aws_sdk_appflow.types.connector_metadata

        out["connectorMetadata"] = (
            aws_sdk_appflow.types.connector_metadata.serialize_json(
                value["connector_metadata"]
            )
        )
    if "connector_type" in value:
        import aws_sdk_appflow.types.connector_type

        out["connectorType"] = aws_sdk_appflow.types.connector_type.serialize_json(
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
        import aws_sdk_appflow.types.connector_mode_list

        out["connectorModes"] = (
            aws_sdk_appflow.types.connector_mode_list.serialize_json(
                value["connector_modes"]
            )
        )
    if "authentication_config" in value:
        import aws_sdk_appflow.types.authentication_config

        out["authenticationConfig"] = (
            aws_sdk_appflow.types.authentication_config.serialize_json(
                value["authentication_config"]
            )
        )
    if "connector_runtime_settings" in value:
        import aws_sdk_appflow.types.connector_runtime_setting_list

        out["connectorRuntimeSettings"] = (
            aws_sdk_appflow.types.connector_runtime_setting_list.serialize_json(
                value["connector_runtime_settings"]
            )
        )
    if "supported_api_versions" in value:
        import aws_sdk_appflow.types.supported_api_version_list

        out["supportedApiVersions"] = (
            aws_sdk_appflow.types.supported_api_version_list.serialize_json(
                value["supported_api_versions"]
            )
        )
    if "supported_operators" in value:
        import aws_sdk_appflow.types.supported_operator_list

        out["supportedOperators"] = (
            aws_sdk_appflow.types.supported_operator_list.serialize_json(
                value["supported_operators"]
            )
        )
    if "supported_write_operations" in value:
        import aws_sdk_appflow.types.supported_write_operation_list

        out["supportedWriteOperations"] = (
            aws_sdk_appflow.types.supported_write_operation_list.serialize_json(
                value["supported_write_operations"]
            )
        )
    if "connector_provisioning_type" in value:
        import aws_sdk_appflow.types.connector_provisioning_type

        out["connectorProvisioningType"] = (
            aws_sdk_appflow.types.connector_provisioning_type.serialize_json(
                value["connector_provisioning_type"]
            )
        )
    if "connector_provisioning_config" in value:
        import aws_sdk_appflow.types.connector_provisioning_config

        out["connectorProvisioningConfig"] = (
            aws_sdk_appflow.types.connector_provisioning_config.serialize_json(
                value["connector_provisioning_config"]
            )
        )
    if "logo_url" in value:
        out["logoURL"] = value["logo_url"]
    if "registered_at" in value:
        import aws_sdk_appflow.types.date

        out["registeredAt"] = aws_sdk_appflow.types.date.serialize_json(
            value["registered_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "supported_data_transfer_types" in value:
        import aws_sdk_appflow.types.supported_data_transfer_type_list

        out["supportedDataTransferTypes"] = (
            aws_sdk_appflow.types.supported_data_transfer_type_list.serialize_json(
                value["supported_data_transfer_types"]
            )
        )
    if "supported_data_transfer_apis" in value:
        import aws_sdk_appflow.types.supported_data_transfer_apis

        out["supportedDataTransferApis"] = (
            aws_sdk_appflow.types.supported_data_transfer_apis.serialize_json(
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
        import aws_sdk_appflow.types.connector_type_list

        out["supported_destination_connectors"] = (
            aws_sdk_appflow.types.connector_type_list.deserialize_json(
                data["supportedDestinationConnectors"]
            )
        )
    if "supportedSchedulingFrequencies" in data:
        import aws_sdk_appflow.types.scheduling_frequency_type_list

        out["supported_scheduling_frequencies"] = (
            aws_sdk_appflow.types.scheduling_frequency_type_list.deserialize_json(
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
        import aws_sdk_appflow.types.trigger_type_list

        out["supported_trigger_types"] = (
            aws_sdk_appflow.types.trigger_type_list.deserialize_json(
                data["supportedTriggerTypes"]
            )
        )
    if "connectorMetadata" in data:
        import aws_sdk_appflow.types.connector_metadata

        out["connector_metadata"] = (
            aws_sdk_appflow.types.connector_metadata.deserialize_json(
                data["connectorMetadata"]
            )
        )
    if "connectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["connector_type"] = aws_sdk_appflow.types.connector_type.deserialize_json(
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
        import aws_sdk_appflow.types.connector_mode_list

        out["connector_modes"] = (
            aws_sdk_appflow.types.connector_mode_list.deserialize_json(
                data["connectorModes"]
            )
        )
    if "authenticationConfig" in data:
        import aws_sdk_appflow.types.authentication_config

        out["authentication_config"] = (
            aws_sdk_appflow.types.authentication_config.deserialize_json(
                data["authenticationConfig"]
            )
        )
    if "connectorRuntimeSettings" in data:
        import aws_sdk_appflow.types.connector_runtime_setting_list

        out["connector_runtime_settings"] = (
            aws_sdk_appflow.types.connector_runtime_setting_list.deserialize_json(
                data["connectorRuntimeSettings"]
            )
        )
    if "supportedApiVersions" in data:
        import aws_sdk_appflow.types.supported_api_version_list

        out["supported_api_versions"] = (
            aws_sdk_appflow.types.supported_api_version_list.deserialize_json(
                data["supportedApiVersions"]
            )
        )
    if "supportedOperators" in data:
        import aws_sdk_appflow.types.supported_operator_list

        out["supported_operators"] = (
            aws_sdk_appflow.types.supported_operator_list.deserialize_json(
                data["supportedOperators"]
            )
        )
    if "supportedWriteOperations" in data:
        import aws_sdk_appflow.types.supported_write_operation_list

        out["supported_write_operations"] = (
            aws_sdk_appflow.types.supported_write_operation_list.deserialize_json(
                data["supportedWriteOperations"]
            )
        )
    if "connectorProvisioningType" in data:
        import aws_sdk_appflow.types.connector_provisioning_type

        out["connector_provisioning_type"] = (
            aws_sdk_appflow.types.connector_provisioning_type.deserialize_json(
                data["connectorProvisioningType"]
            )
        )
    if "connectorProvisioningConfig" in data:
        import aws_sdk_appflow.types.connector_provisioning_config

        out["connector_provisioning_config"] = (
            aws_sdk_appflow.types.connector_provisioning_config.deserialize_json(
                data["connectorProvisioningConfig"]
            )
        )
    if "logoURL" in data:
        out["logo_url"] = data["logoURL"]
    if "registeredAt" in data:
        import aws_sdk_appflow.types.date

        out["registered_at"] = aws_sdk_appflow.types.date.deserialize_json(
            data["registeredAt"]
        )
    if "registeredBy" in data:
        out["registered_by"] = data["registeredBy"]
    if "supportedDataTransferTypes" in data:
        import aws_sdk_appflow.types.supported_data_transfer_type_list

        out["supported_data_transfer_types"] = (
            aws_sdk_appflow.types.supported_data_transfer_type_list.deserialize_json(
                data["supportedDataTransferTypes"]
            )
        )
    if "supportedDataTransferApis" in data:
        import aws_sdk_appflow.types.supported_data_transfer_apis

        out["supported_data_transfer_apis"] = (
            aws_sdk_appflow.types.supported_data_transfer_apis.deserialize_json(
                data["supportedDataTransferApis"]
            )
        )
    return out
