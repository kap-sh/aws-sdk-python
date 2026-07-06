"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_arn
    import aws_sdk_service_catalog_appregistry.types.application_id
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.name
    import aws_sdk_service_catalog_appregistry.types.timestamp


class ApplicationSummary(TypedDict, closed=True):
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
    """<p> The ISO-8601 formatted timestamp of the moment when the application was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
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
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
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
    return out
