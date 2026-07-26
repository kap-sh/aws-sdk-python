"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.arn
    import capo_appflow.types.connection_mode
    import capo_appflow.types.connector_label
    import capo_appflow.types.connector_profile_arn
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_profile_properties
    import capo_appflow.types.connector_type
    import capo_appflow.types.date
    import capo_appflow.types.private_connection_provisioning_state


class ConnectorProfile(TypedDict, closed=True):
    connector_profile_arn: NotRequired[
        "capo_appflow.types.connector_profile_arn.ConnectorProfileArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the connector profile. </p>"""
    connector_profile_name: NotRequired[
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    connector_label: NotRequired["capo_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label for the connector profile being created.</p>"""
    connection_mode: NotRequired["capo_appflow.types.connection_mode.ConnectionMode"]
    """<p> Indicates the connection mode and if it is public or private. </p>"""
    credentials_arn: NotRequired["capo_appflow.types.arn.ARN"]
    """<p> The Amazon Resource Name (ARN) of the connector profile credentials. </p>"""
    connector_profile_properties: NotRequired[
        "capo_appflow.types.connector_profile_properties.ConnectorProfileProperties"
    ]
    """<p> The connector-specific properties of the profile configuration. </p>"""
    created_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies when the connector profile was created. </p>"""
    last_updated_at: NotRequired["capo_appflow.types.date.Date"]
    """<p> Specifies when the connector profile was last updated. </p>"""
    private_connection_provisioning_state: NotRequired[
        "capo_appflow.types.private_connection_provisioning_state.PrivateConnectionProvisioningState"
    ]
    """<p> Specifies the private connection provisioning state. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorProfile) -> dict:
    out: dict = {}
    if "connector_profile_arn" in value:
        out["connectorProfileArn"] = value["connector_profile_arn"]
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    if "connection_mode" in value:
        import capo_appflow.types.connection_mode

        out["connectionMode"] = capo_appflow.types.connection_mode.serialize_json(
            value["connection_mode"]
        )
    if "credentials_arn" in value:
        out["credentialsArn"] = value["credentials_arn"]
    if "connector_profile_properties" in value:
        import capo_appflow.types.connector_profile_properties

        out["connectorProfileProperties"] = (
            capo_appflow.types.connector_profile_properties.serialize_json(
                value["connector_profile_properties"]
            )
        )
    if "created_at" in value:
        import capo_appflow.types.date

        out["createdAt"] = capo_appflow.types.date.serialize_json(value["created_at"])
    if "last_updated_at" in value:
        import capo_appflow.types.date

        out["lastUpdatedAt"] = capo_appflow.types.date.serialize_json(
            value["last_updated_at"]
        )
    if "private_connection_provisioning_state" in value:
        import capo_appflow.types.private_connection_provisioning_state

        out["privateConnectionProvisioningState"] = (
            capo_appflow.types.private_connection_provisioning_state.serialize_json(
                value["private_connection_provisioning_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorProfile:
    out: ConnectorProfile = {}  # type: ignore[typeddict-item]
    if "connectorProfileArn" in data:
        out["connector_profile_arn"] = data["connectorProfileArn"]
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    if "connectionMode" in data:
        import capo_appflow.types.connection_mode

        out["connection_mode"] = capo_appflow.types.connection_mode.deserialize_json(
            data["connectionMode"]
        )
    if "credentialsArn" in data:
        out["credentials_arn"] = data["credentialsArn"]
    if "connectorProfileProperties" in data:
        import capo_appflow.types.connector_profile_properties

        out["connector_profile_properties"] = (
            capo_appflow.types.connector_profile_properties.deserialize_json(
                data["connectorProfileProperties"]
            )
        )
    if "createdAt" in data:
        import capo_appflow.types.date

        out["created_at"] = capo_appflow.types.date.deserialize_json(data["createdAt"])
    if "lastUpdatedAt" in data:
        import capo_appflow.types.date

        out["last_updated_at"] = capo_appflow.types.date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "privateConnectionProvisioningState" in data:
        import capo_appflow.types.private_connection_provisioning_state

        out["private_connection_provisioning_state"] = (
            capo_appflow.types.private_connection_provisioning_state.deserialize_json(
                data["privateConnectionProvisioningState"]
            )
        )
    return out
