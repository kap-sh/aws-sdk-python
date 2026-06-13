"""Generated from Smithy shape ``com.amazonaws.datazone#RuleScope``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_types_for_rule
    import aws_sdk_datazone.types.projects_for_rule


class RuleScope(TypedDict):
    asset_type: NotRequired[
        "aws_sdk_datazone.types.asset_types_for_rule.AssetTypesForRule"
    ]
    """<p>The asset type included in the rule scope.</p>"""
    data_product: NotRequired["bool"]
    """<p>The data product included in the rule scope.</p>"""
    project: NotRequired["aws_sdk_datazone.types.projects_for_rule.ProjectsForRule"]
    """<p>The project included in the rule scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleScope) -> dict:
    out: dict = {}
    if "asset_type" in value:
        import aws_sdk_datazone.types.asset_types_for_rule

        out["assetType"] = aws_sdk_datazone.types.asset_types_for_rule.serialize_json(
            value["asset_type"]
        )
    if "data_product" in value:
        out["dataProduct"] = value["data_product"]
    if "project" in value:
        import aws_sdk_datazone.types.projects_for_rule

        out["project"] = aws_sdk_datazone.types.projects_for_rule.serialize_json(
            value["project"]
        )
    return out


def deserialize_json(data: dict) -> RuleScope:
    out: RuleScope = {}  # type: ignore[typeddict-item]
    if "assetType" in data:
        import aws_sdk_datazone.types.asset_types_for_rule

        out["asset_type"] = (
            aws_sdk_datazone.types.asset_types_for_rule.deserialize_json(
                data["assetType"]
            )
        )
    if "dataProduct" in data:
        out["data_product"] = data["dataProduct"]
    if "project" in data:
        import aws_sdk_datazone.types.projects_for_rule

        out["project"] = aws_sdk_datazone.types.projects_for_rule.deserialize_json(
            data["project"]
        )
    return out
