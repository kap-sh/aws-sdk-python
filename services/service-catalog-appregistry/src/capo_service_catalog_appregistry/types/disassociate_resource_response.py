"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DisassociateResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_arn
    import capo_service_catalog_appregistry.types.arn


class DisassociateResourceResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the application.</p>"""
    resource_arn: NotRequired["capo_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateResourceResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateResourceResponse:
    out: DisassociateResourceResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    return out
