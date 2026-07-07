"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataRelationshipType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.associated_fields_list
    import aws_sdk_amplifyuibuilder.types.generic_data_relationship_type
    import aws_sdk_amplifyuibuilder.types.related_model_fields_list


class CodegenGenericDataRelationshipType(TypedDict, closed=True):
    type: "aws_sdk_amplifyuibuilder.types.generic_data_relationship_type.GenericDataRelationshipType"
    """<p>The data relationship type.</p>"""
    related_model_name: "str"
    """<p>The name of the related model in the data relationship.</p>"""
    related_model_fields: NotRequired[
        "aws_sdk_amplifyuibuilder.types.related_model_fields_list.RelatedModelFieldsList"
    ]
    """<p>The related model fields in the data relationship.</p>"""
    can_unlink_associated_model: NotRequired["bool"]
    """<p>Specifies whether the relationship can unlink the associated model.</p>"""
    related_join_field_name: NotRequired["str"]
    """<p>The name of the related join field in the data relationship.</p>"""
    related_join_table_name: NotRequired["str"]
    """<p>The name of the related join table in the data relationship.</p>"""
    belongs_to_field_on_related_model: NotRequired["str"]
    """<p>The value of the <code>belongsTo</code> field on the related data model. </p>"""
    associated_fields: NotRequired[
        "aws_sdk_amplifyuibuilder.types.associated_fields_list.AssociatedFieldsList"
    ]
    """<p>The associated fields of the data relationship.</p>"""
    is_has_many_index: NotRequired["bool"]
    """<p>Specifies whether the <code>@index</code> directive is supported for a <code>hasMany</code> data relationship.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenGenericDataRelationshipType) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.generic_data_relationship_type

    out["type"] = (
        aws_sdk_amplifyuibuilder.types.generic_data_relationship_type.serialize_json(
            value["type"]
        )
    )
    out["relatedModelName"] = value["related_model_name"]
    if "related_model_fields" in value:
        import aws_sdk_amplifyuibuilder.types.related_model_fields_list

        out["relatedModelFields"] = (
            aws_sdk_amplifyuibuilder.types.related_model_fields_list.serialize_json(
                value["related_model_fields"]
            )
        )
    if "can_unlink_associated_model" in value:
        out["canUnlinkAssociatedModel"] = value["can_unlink_associated_model"]
    if "related_join_field_name" in value:
        out["relatedJoinFieldName"] = value["related_join_field_name"]
    if "related_join_table_name" in value:
        out["relatedJoinTableName"] = value["related_join_table_name"]
    if "belongs_to_field_on_related_model" in value:
        out["belongsToFieldOnRelatedModel"] = value["belongs_to_field_on_related_model"]
    if "associated_fields" in value:
        import aws_sdk_amplifyuibuilder.types.associated_fields_list

        out["associatedFields"] = (
            aws_sdk_amplifyuibuilder.types.associated_fields_list.serialize_json(
                value["associated_fields"]
            )
        )
    if "is_has_many_index" in value:
        out["isHasManyIndex"] = value["is_has_many_index"]
    return out


def deserialize_json(data: dict) -> CodegenGenericDataRelationshipType:
    out: CodegenGenericDataRelationshipType = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_amplifyuibuilder.types.generic_data_relationship_type

        out["type"] = (
            aws_sdk_amplifyuibuilder.types.generic_data_relationship_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("CodegenGenericDataRelationshipType.type required")
    if "relatedModelName" in data:
        out["related_model_name"] = data["relatedModelName"]
    else:
        raise DeserializationError(
            "CodegenGenericDataRelationshipType.related_model_name required"
        )
    if "relatedModelFields" in data:
        import aws_sdk_amplifyuibuilder.types.related_model_fields_list

        out["related_model_fields"] = (
            aws_sdk_amplifyuibuilder.types.related_model_fields_list.deserialize_json(
                data["relatedModelFields"]
            )
        )
    if "canUnlinkAssociatedModel" in data:
        out["can_unlink_associated_model"] = data["canUnlinkAssociatedModel"]
    if "relatedJoinFieldName" in data:
        out["related_join_field_name"] = data["relatedJoinFieldName"]
    if "relatedJoinTableName" in data:
        out["related_join_table_name"] = data["relatedJoinTableName"]
    if "belongsToFieldOnRelatedModel" in data:
        out["belongs_to_field_on_related_model"] = data["belongsToFieldOnRelatedModel"]
    if "associatedFields" in data:
        import aws_sdk_amplifyuibuilder.types.associated_fields_list

        out["associated_fields"] = (
            aws_sdk_amplifyuibuilder.types.associated_fields_list.deserialize_json(
                data["associatedFields"]
            )
        )
    if "isHasManyIndex" in data:
        out["is_has_many_index"] = data["isHasManyIndex"]
    return out
