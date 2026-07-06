"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#CreateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.client_token
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.name
    import aws_sdk_service_catalog_appregistry.types.tags


class CreateApplicationRequest(TypedDict, closed=True):
    name: "aws_sdk_service_catalog_appregistry.types.name.Name"
    """<p>The name of the application. The name must be unique in the region in which you are creating the application.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The description of the application.</p>"""
    tags: NotRequired["aws_sdk_service_catalog_appregistry.types.tags.Tags"]
    """<p>Key-value pairs you can use to associate with the application.</p>"""
    client_token: "aws_sdk_service_catalog_appregistry.types.client_token.ClientToken"
    """<p>A unique identifier that you provide to ensure idempotency. If you retry a request that completed successfully using the same client token and the same parameters, the retry succeeds without performing any further actions. If you retry a successful request using the same client token, but one or more of the parameters are different, the retry fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.serialize_json(
            value["tags"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateApplicationRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_service_catalog_appregistry.types.tags

        out["tags"] = aws_sdk_service_catalog_appregistry.types.tags.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateApplicationRequest.client_token required")
    return out
