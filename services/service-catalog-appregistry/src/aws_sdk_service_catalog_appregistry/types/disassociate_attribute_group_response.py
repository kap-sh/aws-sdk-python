"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DisassociateAttributeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_arn
    import aws_sdk_service_catalog_appregistry.types.attribute_group_arn


class DisassociateAttributeGroupResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the application.</p>"""
    attribute_group_arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_arn.AttributeGroupArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateAttributeGroupResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "attribute_group_arn" in value:
        out["attributeGroupArn"] = value["attribute_group_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateAttributeGroupResponse:
    out: DisassociateAttributeGroupResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "attributeGroupArn" in data:
        out["attribute_group_arn"] = data["attributeGroupArn"]
    return out
