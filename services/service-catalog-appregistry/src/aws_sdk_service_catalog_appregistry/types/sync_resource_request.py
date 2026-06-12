"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#SyncResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.resource_specifier
    import aws_sdk_service_catalog_appregistry.types.resource_type


class SyncResourceRequest(TypedDict):
    resource_type: (
        "aws_sdk_service_catalog_appregistry.types.resource_type.ResourceType"
    )
    """<p>The type of resource of which the application will be associated.</p>"""
    resource: (
        "aws_sdk_service_catalog_appregistry.types.resource_specifier.ResourceSpecifier"
    )
    """<p>An entity you can work with and specify with a name or ID. Examples include an Amazon EC2 instance, an Amazon Web Services CloudFormation stack, or an Amazon S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SyncResourceRequest:
    out: SyncResourceRequest = {}  # type: ignore[typeddict-item]
    return out
