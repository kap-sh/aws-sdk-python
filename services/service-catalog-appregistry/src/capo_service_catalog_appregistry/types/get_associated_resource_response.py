"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#GetAssociatedResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_tag_result
    import capo_service_catalog_appregistry.types.options
    import capo_service_catalog_appregistry.types.resource


class GetAssociatedResourceResponse(TypedDict, closed=True):
    resource: NotRequired["capo_service_catalog_appregistry.types.resource.Resource"]
    """<p>The resource associated with the application.</p>"""
    options: NotRequired["capo_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""
    application_tag_result: NotRequired[
        "capo_service_catalog_appregistry.types.application_tag_result.ApplicationTagResult"
    ]
    """<p> The result of the application that's tag applied to a resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedResourceResponse) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_service_catalog_appregistry.types.resource

        out["resource"] = (
            capo_service_catalog_appregistry.types.resource.serialize_json(
                value["resource"]
            )
        )
    if "options" in value:
        import capo_service_catalog_appregistry.types.options

        out["options"] = capo_service_catalog_appregistry.types.options.serialize_json(
            value["options"]
        )
    if "application_tag_result" in value:
        import capo_service_catalog_appregistry.types.application_tag_result

        out["applicationTagResult"] = (
            capo_service_catalog_appregistry.types.application_tag_result.serialize_json(
                value["application_tag_result"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetAssociatedResourceResponse:
    out: GetAssociatedResourceResponse = {}  # type: ignore[typeddict-item]
    if "resource" in data:
        import capo_service_catalog_appregistry.types.resource

        out["resource"] = (
            capo_service_catalog_appregistry.types.resource.deserialize_json(
                data["resource"]
            )
        )
    if "options" in data:
        import capo_service_catalog_appregistry.types.options

        out["options"] = (
            capo_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    if "applicationTagResult" in data:
        import capo_service_catalog_appregistry.types.application_tag_result

        out["application_tag_result"] = (
            capo_service_catalog_appregistry.types.application_tag_result.deserialize_json(
                data["applicationTagResult"]
            )
        )
    return out
