"""Generated from Smithy shape ``com.amazonaws.datazone#LineageNodeTypeItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.forms_output_map
    import aws_sdk_datazone.types.revision
    import aws_sdk_datazone.types.updated_at
    import aws_sdk_datazone.types.updated_by


class LineageNodeTypeItem(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the data lineage node type lives.</p>"""
    name: NotRequired["str"]
    """<p>The name of the data lineage node type.</p>"""
    description: NotRequired["str"]
    """<p>The description of the data lineage node type.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data lineage node type was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The user who created the data lineage node type.</p>"""
    updated_at: NotRequired["aws_sdk_datazone.types.updated_at.UpdatedAt"]
    """<p>The timestamp at which the data lineage node type was updated.</p>"""
    updated_by: NotRequired["aws_sdk_datazone.types.updated_by.UpdatedBy"]
    """<p>The user who updated the data lineage node type.</p>"""
    revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the data lineage node type.</p>"""
    forms_output: "aws_sdk_datazone.types.forms_output_map.FormsOutputMap"
    """<p>The forms output of the data lineage node type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageNodeTypeItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_datazone.types.updated_at

        out["updatedAt"] = aws_sdk_datazone.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    out["revision"] = value["revision"]
    import aws_sdk_datazone.types.forms_output_map

    out["formsOutput"] = aws_sdk_datazone.types.forms_output_map.serialize_json(
        value["forms_output"]
    )
    return out


def deserialize_json(data: dict) -> LineageNodeTypeItem:
    out: LineageNodeTypeItem = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("LineageNodeTypeItem.domain_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "updatedAt" in data:
        import aws_sdk_datazone.types.updated_at

        out["updated_at"] = aws_sdk_datazone.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        raise DeserializationError("LineageNodeTypeItem.revision required")
    if "formsOutput" in data:
        import aws_sdk_datazone.types.forms_output_map

        out["forms_output"] = aws_sdk_datazone.types.forms_output_map.deserialize_json(
            data["formsOutput"]
        )
    else:
        raise DeserializationError("LineageNodeTypeItem.forms_output required")
    return out
