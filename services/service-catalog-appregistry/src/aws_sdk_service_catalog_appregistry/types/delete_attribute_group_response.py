"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DeleteAttributeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.attribute_group_summary


class DeleteAttributeGroupResponse(TypedDict, closed=True):
    attribute_group: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.attribute_group_summary.AttributeGroupSummary"
    ]
    """<p>Information about the deleted attribute group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAttributeGroupResponse) -> dict:
    out: dict = {}
    if "attribute_group" in value:
        import aws_sdk_service_catalog_appregistry.types.attribute_group_summary

        out["attributeGroup"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group_summary.serialize_json(
                value["attribute_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteAttributeGroupResponse:
    out: DeleteAttributeGroupResponse = {}  # type: ignore[typeddict-item]
    if "attributeGroup" in data:
        import aws_sdk_service_catalog_appregistry.types.attribute_group_summary

        out["attribute_group"] = (
            aws_sdk_service_catalog_appregistry.types.attribute_group_summary.deserialize_json(
                data["attributeGroup"]
            )
        )
    return out
