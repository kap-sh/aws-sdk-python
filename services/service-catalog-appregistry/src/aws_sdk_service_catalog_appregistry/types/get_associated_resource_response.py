"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAssociatedResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_tag_result
    import aws_sdk_service_catalog_appregistry.types.options
    import aws_sdk_service_catalog_appregistry.types.resource


class GetAssociatedResourceResponse(TypedDict):
    resource: NotRequired["aws_sdk_service_catalog_appregistry.types.resource.Resource"]
    """<p>The resource associated with the application.</p>"""
    options: NotRequired["aws_sdk_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""
    application_tag_result: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_tag_result.ApplicationTagResult"
    ]
    """<p> The result of the application that's tag applied to a resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedResourceResponse) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_service_catalog_appregistry.types.resource

        out["resource"] = (
            aws_sdk_service_catalog_appregistry.types.resource.serialize_json(
                value["resource"]
            )
        )
    if "options" in value:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.serialize_json(
                value["options"]
            )
        )
    if "application_tag_result" in value:
        import aws_sdk_service_catalog_appregistry.types.application_tag_result

        out["applicationTagResult"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_result.serialize_json(
                value["application_tag_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssociatedResourceResponse:
    out: GetAssociatedResourceResponse = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import aws_sdk_service_catalog_appregistry.types.resource

        out["resource"] = (
            aws_sdk_service_catalog_appregistry.types.resource.deserialize_json(
                data["resource"]
            )
        )
    if "options" in data:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    if "applicationTagResult" in data:
        import aws_sdk_service_catalog_appregistry.types.application_tag_result

        out["application_tag_result"] = (
            aws_sdk_service_catalog_appregistry.types.application_tag_result.deserialize_json(
                data["applicationTagResult"]
            )
        )
    return out
