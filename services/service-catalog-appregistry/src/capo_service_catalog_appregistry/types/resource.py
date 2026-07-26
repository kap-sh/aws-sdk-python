"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.arn
    import capo_service_catalog_appregistry.types.resource_integrations
    import capo_service_catalog_appregistry.types.resource_specifier
    import capo_service_catalog_appregistry.types.timestamp


class Resource(TypedDict, closed=True):
    name: NotRequired[
        "capo_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    ]
    """<p>The name of the resource.</p>"""
    arn: NotRequired["capo_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) of the resource.</p>"""
    association_time: NotRequired[
        "capo_service_catalog_appregistry.types.timestamp.Timestamp"
    ]
    """<p>The time the resource was associated with the application.</p>"""
    integrations: NotRequired[
        "capo_service_catalog_appregistry.types.resource_integrations.ResourceIntegrations"
    ]
    """<p>The service integration information about the resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "association_time" in value:
        import capo_service_catalog_appregistry.types.timestamp

        out["associationTime"] = (
            capo_service_catalog_appregistry.types.timestamp.serialize_json(
                value["association_time"]
            )
        )
    if "integrations" in value:
        import capo_service_catalog_appregistry.types.resource_integrations

        out["integrations"] = (
            capo_service_catalog_appregistry.types.resource_integrations.serialize_json(
                value["integrations"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "associationTime" in data:
        import capo_service_catalog_appregistry.types.timestamp

        out["association_time"] = (
            capo_service_catalog_appregistry.types.timestamp.deserialize_json(
                data["associationTime"]
            )
        )
    if "integrations" in data:
        import capo_service_catalog_appregistry.types.resource_integrations

        out["integrations"] = (
            capo_service_catalog_appregistry.types.resource_integrations.deserialize_json(
                data["integrations"]
            )
        )
    return out
