"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTypesForRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_datazone.types.rule_asset_type_list
    import aws_sdk_datazone.types.rule_scope_selection_mode

class AssetTypesForRule(TypedDict):
    selection_mode: "aws_sdk_datazone.types.rule_scope_selection_mode.RuleScopeSelectionMode"
    """<p>The selection mode for the rule.</p>"""
    specific_asset_types: NotRequired["aws_sdk_datazone.types.rule_asset_type_list.RuleAssetTypeList"]
    """<p>The specific asset types that are included in the rule.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssetTypesForRule) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.rule_scope_selection_mode
    out["selectionMode"] = aws_sdk_datazone.types.rule_scope_selection_mode.serialize_json(value["selection_mode"])
    if "specific_asset_types" in value:
        import aws_sdk_datazone.types.rule_asset_type_list
        out["specificAssetTypes"] = aws_sdk_datazone.types.rule_asset_type_list.serialize_json(value["specific_asset_types"])
    return out


def deserialize_json(data: dict) -> AssetTypesForRule:
    out: AssetTypesForRule = {}  # type: ignore[typeddict-item]
    if "selectionMode" in data:
        import aws_sdk_datazone.types.rule_scope_selection_mode
        out["selection_mode"] = aws_sdk_datazone.types.rule_scope_selection_mode.deserialize_json(data["selectionMode"])
    else:
        raise DeserializationError("AssetTypesForRule.selection_mode required")
    if "specificAssetTypes" in data:
        import aws_sdk_datazone.types.rule_asset_type_list
        out["specific_asset_types"] = aws_sdk_datazone.types.rule_asset_type_list.deserialize_json(data["specificAssetTypes"])
    return out