"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagPolicyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.resource_type


class LFTagPolicyResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    resource_type: "capo_lakeformation.types.resource_type.ResourceType"
    """<p>The resource type for which the LF-tag policy applies.</p>"""
    expression: "capo_lakeformation.types.expression.Expression"
    """<p>A list of LF-tag conditions or a saved expression that apply to the resource's LF-tag policy.</p>"""
    expression_name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>If provided, permissions are granted to the Data Catalog resources whose assigned LF-Tags match the expression body of the saved expression under the provided <code>ExpressionName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagPolicyResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.resource_type

    out["ResourceType"] = capo_lakeformation.types.resource_type.serialize_json(
        value["resource_type"]
    )
    import capo_lakeformation.types.expression

    out["Expression"] = capo_lakeformation.types.expression.serialize_json(
        value.get("expression", [])
    )
    if "expression_name" in value:
        out["ExpressionName"] = value["expression_name"]
    return out


def deserialize_json(data: dict) -> LFTagPolicyResource:
    out: LFTagPolicyResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ResourceType" in data:
        import capo_lakeformation.types.resource_type

        out["resource_type"] = capo_lakeformation.types.resource_type.deserialize_json(
            data["ResourceType"]
        )
    else:
        raise DeserializationError("LFTagPolicyResource.resource_type required")
    if "Expression" in data:
        import capo_lakeformation.types.expression

        out["expression"] = capo_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    else:
        out["expression"] = []
    if "ExpressionName" in data:
        out["expression_name"] = data["ExpressionName"]
    return out
