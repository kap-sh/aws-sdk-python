"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Application``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_arn
    import capo_service_catalog_appregistry.types.application_id
    import capo_service_catalog_appregistry.types.application_tag_definition
    import capo_service_catalog_appregistry.types.description
    import capo_service_catalog_appregistry.types.name
    import capo_service_catalog_appregistry.types.tags
    import capo_service_catalog_appregistry.types.timestamp


class Application(TypedDict, closed=True):
    id: NotRequired[
        "capo_service_catalog_appregistry.types.application_id.ApplicationId"
    ]
    """<p>The identifier of the application.</p>"""
    arn: NotRequired[
        "capo_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the application across services.</p>"""
    name: NotRequired["capo_service_catalog_appregistry.types.name.Name"]
    """<p>The name of the application. The name must be unique in the region in which you are creating the application.</p>"""
    description: NotRequired[
        "capo_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the application.</p>"""
    creation_time: NotRequired[
        "capo_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The ISO-8601 formatted timestamp of the moment when the application was created.</p>"""
    last_update_time: NotRequired[
        "capo_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p> The ISO-8601 formatted timestamp of the moment when the application was last updated.</p>"""
    tags: NotRequired["capo_service_catalog_appregistry.types.tags.Tags"]
    """<p>Key-value pairs you can use to associate with the application.</p>"""
    application_tag: NotRequired[
        "capo_service_catalog_appregistry.types.application_tag_definition.ApplicationTagDefinition"
    ]
    """<p> A key-value pair that identifies an associated resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
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
        import capo_service_catalog_appregistry.types.timestamp

        out["creationTime"] = (
            capo_service_catalog_appregistry.types.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "last_update_time" in value:
        import capo_service_catalog_appregistry.types.timestamp

        out["lastUpdateTime"] = (
            capo_service_catalog_appregistry.types.timestamp.serialize_json(
                value["last_update_time"]
            )
        )
    if "tags" in value:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    if "application_tag" in value:
        import capo_service_catalog_appregistry.types.application_tag_definition

        out["applicationTag"] = (
            capo_service_catalog_appregistry.types.application_tag_definition.serialize_json(
                value["application_tag"]
            )
        )
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import capo_service_catalog_appregistry.types.timestamp

        out["creation_time"] = (
            capo_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "lastUpdateTime" in data:
        import capo_service_catalog_appregistry.types.timestamp

        out["last_update_time"] = (
            capo_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    if "tags" in data:
        import capo_service_catalog_appregistry.types.tags

        out["tags"] = capo_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    if "applicationTag" in data:
        import capo_service_catalog_appregistry.types.application_tag_definition

        out["application_tag"] = (
            capo_service_catalog_appregistry.types.application_tag_definition.deserialize_json(
                data["applicationTag"]
            )
        )
    return out
