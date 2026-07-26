"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociateAttributeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application_arn
    import capo_service_catalog_appregistry.types.attribute_group_arn


class AssociateAttributeGroupResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_service_catalog_appregistry.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon resource name (ARN) of the application that was augmented with attributes.</p>"""
    attribute_group_arn: NotRequired[
        "capo_service_catalog_appregistry.types.attribute_group_arn.AttributeGroupArn"
    ]
    """<p>The Amazon resource name (ARN) of the attribute group that contains the application's new attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAttributeGroupResponse) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "attribute_group_arn" in value:
        out["attributeGroupArn"] = value["attribute_group_arn"]
    return out


def deserialize_json(data: dict) -> AssociateAttributeGroupResponse:
    out: AssociateAttributeGroupResponse = {}  # type: ignore[typeddict-item]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "attributeGroupArn" in data:
        out["attribute_group_arn"] = data["attributeGroupArn"]
    return out
