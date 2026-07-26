"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.description_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.name_string


class LFTagExpression(TypedDict, closed=True):
    name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name for saved the LF-Tag expression.</p>"""
    description: NotRequired[
        "capo_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>A structure that contains information about the LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. </p>"""
    expression: NotRequired["capo_lakeformation.types.expression.Expression"]
    """<p>A logical expression composed of one or more LF-Tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagExpression) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "expression" in value:
        import capo_lakeformation.types.expression

        out["Expression"] = capo_lakeformation.types.expression.serialize_json(
            value["expression"]
        )
    return out


def deserialize_json(data: dict) -> LFTagExpression:
    out: LFTagExpression = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Expression" in data:
        import capo_lakeformation.types.expression

        out["expression"] = capo_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    return out
