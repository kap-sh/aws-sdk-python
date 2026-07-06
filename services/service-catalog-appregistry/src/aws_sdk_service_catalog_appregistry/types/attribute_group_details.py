"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AttributeGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_arn
    import aws_sdk_service_catalog_appregistry.types.attribute_group_id
    import aws_sdk_service_catalog_appregistry.types.created_by
    import aws_sdk_service_catalog_appregistry.types.name


class AttributeGroupDetails(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_id.AttributeGroupId"
    ]
    """<p>The unique identifier of the attribute group.</p>"""
    arn: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_arn.AttributeGroupArn"
    ]
    """<p>The Amazon resource name (ARN) that specifies the attribute group.</p>"""
    name: NotRequired["aws_sdk_service_catalog_appregistry.types.name.Name"]
    """<important> <p> This field is no longer supported. We recommend you don't use the field when using <code>ListAttributeGroupsForApplication</code>. </p> </important> <p> The name of the attribute group. </p>"""
    created_by: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.created_by.CreatedBy"
    ]
    """<p>The service principal that created the attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeGroupDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> AttributeGroupDetails:
    out: AttributeGroupDetails = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    return out
