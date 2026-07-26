"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.application_type
    import capo_appflow.types.connector_description
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_mode_list
    import capo_appflow.types.connector_name
    import capo_appflow.types.connector_owner
    import capo_appflow.types.connector_provisioning_type
    import capo_appflow.types.connector_type
    import capo_appflow.types.connector_version
    import capo_appflow.types.date
    import capo_appflow.types.registered_by
    import capo_appflow.types.supported_data_transfer_type_list


class ConnectorDetail(TypedDict, closed=True):
    connector_description: NotRequired[
        "capo_appflow.types.connector_description.ConnectorDescription"
    ]
    """<p>A description about the registered connector.</p>"""
    connector_name: NotRequired["capo_appflow.types.connector_name.ConnectorName"]
    """<p>The name of the connector.</p>"""
    connector_owner: NotRequired["capo_appflow.types.connector_owner.ConnectorOwner"]
    """<p>The owner of the connector.</p>"""
    connector_version: NotRequired[
        "capo_appflow.types.connector_version.ConnectorVersion"
    ]
    """<p>The connector version.</p>"""
    application_type: NotRequired["capo_appflow.types.application_type.ApplicationType"]
    """<p>The application type of the connector.</p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p>The connector type.</p>"""
    connector_label: NotRequired["capo_appflow.types.connector_label.ConnectorLabel"]
    """<p>A label used for the connector.</p>"""
    registered_at: NotRequired["capo_appflow.types.date.Date"]
    """<p>The time at which the connector was registered.</p>"""
    registered_by: NotRequired["capo_appflow.types.registered_by.RegisteredBy"]
    """<p>The user who registered the connector.</p>"""
    connector_provisioning_type: NotRequired[
        "capo_appflow.types.connector_provisioning_type.ConnectorProvisioningType"
    ]
    """<p>The provisioning type that the connector uses.</p>"""
    connector_modes: NotRequired[
        "capo_appflow.types.connector_mode_list.ConnectorModeList"
    ]
    """<p>The connection mode that the connector supports.</p>"""
    supported_data_transfer_types: NotRequired[
        "capo_appflow.types.supported_data_transfer_type_list.SupportedDataTransferTypeList"
    ]
    """<p>The data transfer types that the connector supports.</p> <dl> <dt>RECORD</dt> <dd> <p>Structured records.</p> </dd> <dt>FILE</dt> <dd> <p>Files or binary data.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorDetail) -> dict:
    out: dict = {}
    if "connector_description" in value:
        out["connectorDescription"] = value["connector_description"]
    if "connector_name" in value:
        out["connectorName"] = value["connector_name"]
    if "connector_owner" in value:
        out["connectorOwner"] = value["connector_owner"]
    if "connector_version" in value:
        out["connectorVersion"] = value["connector_version"]
    if "application_type" in value:
        out["applicationType"] = value["application_type"]
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    if "registered_at" in value:
        import capo_appflow.types.date

        out["registeredAt"] = capo_appflow.types.date.serialize_json(
            value["registered_at"]
        )
    if "registered_by" in value:
        out["registeredBy"] = value["registered_by"]
    if "connector_provisioning_type" in value:
        import capo_appflow.types.connector_provisioning_type

        out["connectorProvisioningType"] = (
            capo_appflow.types.connector_provisioning_type.serialize_json(
                value["connector_provisioning_type"]
            )
        )
    if "connector_modes" in value:
        import capo_appflow.types.connector_mode_list

        out["connectorModes"] = capo_appflow.types.connector_mode_list.serialize_json(
            value["connector_modes"]
        )
    if "supported_data_transfer_types" in value:
        import capo_appflow.types.supported_data_transfer_type_list

        out["supportedDataTransferTypes"] = (
            capo_appflow.types.supported_data_transfer_type_list.serialize_json(
                value["supported_data_transfer_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorDetail:
    out: ConnectorDetail = {}  # type: ignore[typeddict-item]
    if "connectorDescription" in data:
        out["connector_description"] = data["connectorDescription"]
    if "connectorName" in data:
        out["connector_name"] = data["connectorName"]
    if "connectorOwner" in data:
        out["connector_owner"] = data["connectorOwner"]
    if "connectorVersion" in data:
        out["connector_version"] = data["connectorVersion"]
    if "applicationType" in data:
        out["application_type"] = data["applicationType"]
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    if "registeredAt" in data:
        import capo_appflow.types.date

        out["registered_at"] = capo_appflow.types.date.deserialize_json(
            data["registeredAt"]
        )
    if "registeredBy" in data:
        out["registered_by"] = data["registeredBy"]
    if "connectorProvisioningType" in data:
        import capo_appflow.types.connector_provisioning_type

        out["connector_provisioning_type"] = (
            capo_appflow.types.connector_provisioning_type.deserialize_json(
                data["connectorProvisioningType"]
            )
        )
    if "connectorModes" in data:
        import capo_appflow.types.connector_mode_list

        out["connector_modes"] = (
            capo_appflow.types.connector_mode_list.deserialize_json(
                data["connectorModes"]
            )
        )
    if "supportedDataTransferTypes" in data:
        import capo_appflow.types.supported_data_transfer_type_list

        out["supported_data_transfer_types"] = (
            capo_appflow.types.supported_data_transfer_type_list.deserialize_json(
                data["supportedDataTransferTypes"]
            )
        )
    return out
