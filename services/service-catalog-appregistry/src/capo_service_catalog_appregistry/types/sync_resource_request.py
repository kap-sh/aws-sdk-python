"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#SyncResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.resource_specifier
    import capo_service_catalog_appregistry.types.resource_type


class SyncResourceRequest(TypedDict, closed=True):
    resource_type: "capo_service_catalog_appregistry.types.resource_type.ResourceType"
    """<p>The type of resource of which the application will be associated.</p>"""
    resource: (
        "capo_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SyncResourceRequest:
    out: SyncResourceRequest = {}  # type: ignore[typeddict-item]
    return out
