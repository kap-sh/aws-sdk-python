"""Generated from Smithy shape ``com.amazonaws.appflow#ResetConnectorMetadataCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_version
    import aws_sdk_appflow.types.connector_profile_name
    import aws_sdk_appflow.types.connector_type
    import aws_sdk_appflow.types.entities_path
    import aws_sdk_appflow.types.entity_name


class ResetConnectorMetadataCacheRequest(TypedDict):
    connector_profile_name: NotRequired[
        "aws_sdk_appflow.types.connector_profile_name.ConnectorProfileName"
    ]
    """<p>The name of the connector profile that you want to reset cached metadata for.</p> <p>You can omit this parameter if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you must include this parameter in your request.</p>"""
    connector_type: NotRequired["aws_sdk_appflow.types.connector_type.ConnectorType"]
    """<p>The type of connector to reset cached metadata for.</p> <p>You must include this parameter in your request if you're resetting the cache for any of the following connectors: Connect Customer, Amazon EventBridge, Amazon Lookout for Metrics, Amazon S3, or Upsolver. If you're resetting the cache for any other connector, you can omit this parameter from your request. </p>"""
    connector_entity_name: NotRequired["aws_sdk_appflow.types.entity_name.EntityName"]
    """<p>Use this parameter if you want to reset cached metadata about the details for an individual entity.</p> <p>If you don't include this parameter in your request, Amazon AppFlow only resets cached metadata about entity names, not entity details.</p>"""
    entities_path: NotRequired["aws_sdk_appflow.types.entities_path.EntitiesPath"]
    """<p>Use this parameter only if you’re resetting the cached metadata about a nested entity. Only some connectors support nested entities. A nested entity is one that has another entity as a parent. To use this parameter, specify the name of the parent entity.</p> <p>To look up the parent-child relationship of entities, you can send a ListConnectorEntities request that omits the entitiesPath parameter. Amazon AppFlow will return a list of top-level entities. For each one, it indicates whether the entity has nested entities. Then, in a subsequent ListConnectorEntities request, you can specify a parent entity name for the entitiesPath parameter. Amazon AppFlow will return a list of the child entities for that parent.</p>"""
    api_version: NotRequired["aws_sdk_appflow.types.api_version.ApiVersion"]
    """<p>The API version that you specified in the connector profile that you’re resetting cached metadata for. You must use this parameter only if the connector supports multiple API versions or if the connector type is CustomConnector.</p> <p>To look up how many versions a connector supports, use the DescribeConnectors action. In the response, find the value that Amazon AppFlow returns for the connectorVersion parameter.</p> <p>To look up the connector type, use the DescribeConnectorProfiles action. In the response, find the value that Amazon AppFlow returns for the connectorType parameter.</p> <p>To look up the API version that you specified in a connector profile, use the DescribeConnectorProfiles action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetConnectorMetadataCacheRequest) -> dict:
    out: dict = {}
    if "connector_profile_name" in value:
        out["connectorProfileName"] = value["connector_profile_name"]
    if "connector_type" in value:
        import aws_sdk_appflow.types.connector_type

        out["connectorType"] = aws_sdk_appflow.types.connector_type.serialize_json(
            value["connector_type"]
        )
    if "connector_entity_name" in value:
        out["connectorEntityName"] = value["connector_entity_name"]
    if "entities_path" in value:
        out["entitiesPath"] = value["entities_path"]
    if "api_version" in value:
        out["apiVersion"] = value["api_version"]
    return out


def deserialize_json(data: dict) -> ResetConnectorMetadataCacheRequest:
    out: ResetConnectorMetadataCacheRequest = {}  # type: ignore[typeddict-item]
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    if "connectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["connector_type"] = aws_sdk_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    if "connectorEntityName" in data:
        out["connector_entity_name"] = data["connectorEntityName"]
    if "entitiesPath" in data:
        out["entities_path"] = data["entitiesPath"]
    if "apiVersion" in data:
        out["api_version"] = data["apiVersion"]
    return out
