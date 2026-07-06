"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_arn
    import aws_sdk_service_catalog_appregistry.types.application_id
    import aws_sdk_service_catalog_appregistry.types.application_tag_definition
    import aws_sdk_service_catalog_appregistry.types.association_count
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.integrations
    import aws_sdk_service_catalog_appregistry.types.name
    import aws_sdk_service_catalog_appregistry.types.tags
    import aws_sdk_service_catalog_appregistry.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_id.ApplicationId"
    ]
    """<p>The identifier of the application.</p>"""
    arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the application across services.</p>"""
    name: NotRequired["aws_sdk_service_catalog_appregistry.types.name.Name"]
    """<p>The name of the application. The name must be unique in the region in which you are creating the application.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the application.</p>"""
    creation_time: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment when the application was created.</p>"""
    last_update_time: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment when the application was last updated.</p>"""
    associated_resource_count: (
        "aws_sdk_service_catalog_appregistry.types.association_count.AssociationCount"
    )
    """<p>The number of top-level resources that were registered as part of this application.</p>"""
    tags: NotRequired["aws_sdk_service_catalog_appregistry.types.tags.Tags"]
    """<p>Key-value pairs associated with the application.</p>"""
    integrations: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.integrations.Integrations"
    ]
    """<p> The information about the integration of the application with other services, such as Resource Groups. </p>"""
    application_tag: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_tag_definition.ApplicationTagDefinition"
    ]
    """<p> A key-value pair that identifies an associated resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_time" in value:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["creationTime"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_update_time" in value:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["lastUpdateTime"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.serialize_json(
                value["last_update_time"]
            )
        )
    out["associatedResourceCount"] = value.get("associated_resource_count", 0)
    if "tags" in value:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    if "integrations" in value:
        import aws_sdk_service_catalog_appregistry.types.integrations

        out["integrations"] = (
            aws_sdk_service_catalog_appregistry.types.integrations.serialize_json(
                value["integrations"]
            )
        )
    if "application_tag" in value:
        import aws_sdk_service_catalog_appregistry.types.application_tag_definition

        out["applicationTag"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_definition.serialize_json(
                value["application_tag"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["creation_time"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastUpdateTime" in data:
        import aws_sdk_service_catalog_appregistry.types.timestamp

        out["last_update_time"] = (
            aws_sdk_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    if "associatedResourceCount" in data:
        out["associated_resource_count"] = data["associatedResourceCount"]
    else:
        out["associated_resource_count"] = 0
    if "tags" in data:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    if "integrations" in data:
        import aws_sdk_service_catalog_appregistry.types.integrations

        out["integrations"] = (
            aws_sdk_service_catalog_appregistry.types.integrations.deserialize_json(
                data["integrations"]
            )
        )
    if "applicationTag" in data:
        import aws_sdk_service_catalog_appregistry.types.application_tag_definition

        out["application_tag"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_definition.deserialize_json(
                data["applicationTag"]
            )
        )
    return out
