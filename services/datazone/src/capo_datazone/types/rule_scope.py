"""Generated from Smithy shape ``com.amazonaws.datazone#RuleScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_types_for_rule
    import capo_datazone.types.projects_for_rule


class RuleScope(TypedDict, closed=True):
    asset_type: NotRequired[
        "capo_datazone.types.asset_types_for_rule.AssetTypesForRule"
    ]
    """<p>The asset type included in the rule scope.</p>"""
    data_product: NotRequired["bool"]
    """<p>The data product included in the rule scope.</p>"""
    project: NotRequired["capo_datazone.types.projects_for_rule.ProjectsForRule"]
    """<p>The project included in the rule scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleScope) -> dict:
    out: dict = {}
    if "asset_type" in value:
        import capo_datazone.types.asset_types_for_rule

        out["assetType"] = capo_datazone.types.asset_types_for_rule.serialize_json(
            value["asset_type"]
        )
    if "data_product" in value:
        out["dataProduct"] = value["data_product"]
    if "project" in value:
        import capo_datazone.types.projects_for_rule

        out["project"] = capo_datazone.types.projects_for_rule.serialize_json(
            value["project"]
        )
    return out


def deserialize_json(data: dict) -> RuleScope:
    out: RuleScope = {}  # type: ignore[typeddict-item]
    if "assetType" in data:
        import capo_datazone.types.asset_types_for_rule

        out["asset_type"] = capo_datazone.types.asset_types_for_rule.deserialize_json(
            data["assetType"]
        )
    if "dataProduct" in data:
        out["data_product"] = data["dataProduct"]
    if "project" in data:
        import capo_datazone.types.projects_for_rule

        out["project"] = capo_datazone.types.projects_for_rule.deserialize_json(
            data["project"]
        )
    return out
