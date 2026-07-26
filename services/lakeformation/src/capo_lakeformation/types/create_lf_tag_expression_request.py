"""Generated from Smithy shape ``com.amazonaws.lakeformation#CreateLFTagExpressionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.description_string
    import capo_lakeformation.types.expression
    import capo_lakeformation.types.name_string


class CreateLFTagExpressionRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>A name for the expression.</p>"""
    description: NotRequired[
        "capo_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>A description with information about the LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    expression: "capo_lakeformation.types.expression.Expression"
    """<p>A list of LF-Tag conditions (key-value pairs).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLFTagExpressionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.expression

    out["Expression"] = capo_lakeformation.types.expression.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> CreateLFTagExpressionRequest:
    out: CreateLFTagExpressionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateLFTagExpressionRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Expression" in data:
        import capo_lakeformation.types.expression

        out["expression"] = capo_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("CreateLFTagExpressionRequest.expression required")
    return out
