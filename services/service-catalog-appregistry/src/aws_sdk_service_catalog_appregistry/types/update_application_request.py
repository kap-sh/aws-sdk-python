"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_specifier
    import aws_sdk_service_catalog_appregistry.types.description
    import aws_sdk_service_catalog_appregistry.types.name


class UpdateApplicationRequest(TypedDict, closed=True):
    application: "aws_sdk_service_catalog_appregistry.types.application_specifier.ApplicationSpecifier"
    """<p> The name, ID, or ARN of the application that will be updated. </p>"""
    name: NotRequired["aws_sdk_service_catalog_appregistry.types.name.Name"]
    """<p>Deprecated: The new name of the application. The name must be unique in the region in which you are updating the application. Please do not use this field as we have stopped supporting name updates.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.description.Description"
    ]
    """<p>The new description of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    return out
