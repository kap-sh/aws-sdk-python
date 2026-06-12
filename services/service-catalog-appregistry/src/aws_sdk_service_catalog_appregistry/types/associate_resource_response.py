"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociateResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_arn
    import aws_sdk_service_catalog_appregistry.types.arn
    import aws_sdk_service_catalog_appregistry.types.options


class AssociateResourceResponse(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) of the application that was augmented with attributes.</p>"""
    resource_arn: NotRequired["aws_sdk_service_catalog_appregistry.types.arn.Arn"]
    """<p>The Amazon resource name (ARN) that specifies the resource.</p>"""
    options: NotRequired["aws_sdk_service_catalog_appregistry.types.options.Options"]
    """<p> Determines whether an application tag is applied or skipped. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "options" in value:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.serialize_json(
                value["options"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateResourceResponse:
    out: AssociateResourceResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    if "options" in data:
        import aws_sdk_service_catalog_appregistry.types.options

        out["options"] = (
            aws_sdk_service_catalog_appregistry.types.options.deserialize_json(
                data["options"]
            )
        )
    return out
