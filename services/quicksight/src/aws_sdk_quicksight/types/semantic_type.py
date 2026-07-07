"""Generated from Smithy shape ``com.amazonaws.quicksight#SemanticType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.limited_string
    import aws_sdk_quicksight.types.sensitive_string
    import aws_sdk_quicksight.types.sensitive_string_list
    import aws_sdk_quicksight.types.type_parameters


class SemanticType(TypedDict, closed=True):
    type_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic type name.</p>"""
    sub_type_name: NotRequired["aws_sdk_quicksight.types.limited_string.LimitedString"]
    """<p>The semantic type sub type name.</p>"""
    type_parameters: NotRequired[
        "aws_sdk_quicksight.types.type_parameters.TypeParameters"
    ]
    """<p>The semantic type parameters.</p>"""
    truthy_cell_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The semantic type truthy cell value.</p>"""
    truthy_cell_value_synonyms: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>The other names or aliases for the true cell value.</p>"""
    falsey_cell_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The semantic type falsey cell value.</p>"""
    falsey_cell_value_synonyms: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string_list.SensitiveStringList"
    ]
    """<p>The other names or aliases for the false cell value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SemanticType) -> dict:
    out: dict = {}
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "sub_type_name" in value:
        out["SubTypeName"] = value["sub_type_name"]
    if "type_parameters" in value:
        import aws_sdk_quicksight.types.type_parameters

        out["TypeParameters"] = aws_sdk_quicksight.types.type_parameters.serialize_json(
            value["type_parameters"]
        )
    if "truthy_cell_value" in value:
        out["TruthyCellValue"] = value["truthy_cell_value"]
    if "truthy_cell_value_synonyms" in value:
        import aws_sdk_quicksight.types.sensitive_string_list

        out["TruthyCellValueSynonyms"] = (
            aws_sdk_quicksight.types.sensitive_string_list.serialize_json(
                value["truthy_cell_value_synonyms"]
            )
        )
    if "falsey_cell_value" in value:
        out["FalseyCellValue"] = value["falsey_cell_value"]
    if "falsey_cell_value_synonyms" in value:
        import aws_sdk_quicksight.types.sensitive_string_list

        out["FalseyCellValueSynonyms"] = (
            aws_sdk_quicksight.types.sensitive_string_list.serialize_json(
                value["falsey_cell_value_synonyms"]
            )
        )
    return out


def deserialize_json(data: dict) -> SemanticType:
    out: SemanticType = {}  # type: ignore[typeddict-item]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "SubTypeName" in data:
        out["sub_type_name"] = data["SubTypeName"]
    if "TypeParameters" in data:
        import aws_sdk_quicksight.types.type_parameters

        out["type_parameters"] = (
            aws_sdk_quicksight.types.type_parameters.deserialize_json(
                data["TypeParameters"]
            )
        )
    if "TruthyCellValue" in data:
        out["truthy_cell_value"] = data["TruthyCellValue"]
    if "TruthyCellValueSynonyms" in data:
        import aws_sdk_quicksight.types.sensitive_string_list

        out["truthy_cell_value_synonyms"] = (
            aws_sdk_quicksight.types.sensitive_string_list.deserialize_json(
                data["TruthyCellValueSynonyms"]
            )
        )
    if "FalseyCellValue" in data:
        out["falsey_cell_value"] = data["FalseyCellValue"]
    if "FalseyCellValueSynonyms" in data:
        import aws_sdk_quicksight.types.sensitive_string_list

        out["falsey_cell_value_synonyms"] = (
            aws_sdk_quicksight.types.sensitive_string_list.deserialize_json(
                data["FalseyCellValueSynonyms"]
            )
        )
    return out
