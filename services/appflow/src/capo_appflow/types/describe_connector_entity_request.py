"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeConnectorEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_version
    import capo_appflow.types.connector_profile_name
    import capo_appflow.types.connector_type
    import capo_appflow.types.entity_name


class DescribeConnectorEntityRequest(TypedDict, closed=True):
    connector_entity_name: "capo_appflow.types.entity_name.EntityName"
    """<p> The entity name for that connector. </p>"""
    connector_type: NotRequired["capo_appflow.types.connector_type.ConnectorType"]
    """<p> The type of connector application, such as Salesforce, Amplitude, and so on. </p>"""
    connector_profile_name: NotRequired[
        "capo_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. </p>"""
    api_version: NotRequired["capo_appflow.types.api_version.ApiVersion"]
    """<p>The version of the API that's used by the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorEntityRequest) -> dict:
    out: dict = {}
    out["connectorEntityName"] = value["connector_entity_name"]
    if "connector_type" in value:
        import capo_appflow.types.connector_type

        out["connectorType"] = capo_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    return out


def deserialize_json(data: dict) -> DescribeConnectorEntityRequest:
    out: DescribeConnectorEntityRequest = {}  # type: ignore[typeddict-item]
    if "connectorEntityName" in data:
        out["connector_entity_name"] = data["connectorEntityName"]
    else:
        raise DeserializationError(
            "DescribeConnectorEntityRequest.connector_entity_name required"
        )
    if "connectorType" in data:
        import capo_appflow.types.connector_type

        out["connector_type"] = capo_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    if "apiVersion" in data:
        out["api_version"] = data["apiVersion"]
    return out
