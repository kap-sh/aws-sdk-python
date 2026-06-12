"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetLFTagExpressionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.description_string
    import aws_sdk_lakeformation.types.expression
    import aws_sdk_lakeformation.types.name_string


class GetLFTagExpressionResponse(TypedDict):
    name: NotRequired["aws_sdk_lakeformation.types.name_string.NameString"]
    """<p>The name for the LF-Tag expression. </p>"""
    description: NotRequired[
        "aws_sdk_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>The description with information about the LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID in which the LF-Tag expression is saved.</p>"""
    expression: NotRequired["aws_sdk_lakeformation.types.expression.Expression"]
    """<p>The body of the LF-Tag expression. It is composed of one or more LF-Tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLFTagExpressionResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "expression" in value:
        import aws_sdk_lakeformation.types.expression

        out["Expression"] = aws_sdk_lakeformation.types.expression.serialize_json(
            value["expression"]
        )
    return out


def deserialize_json(data: dict) -> GetLFTagExpressionResponse:
    out: GetLFTagExpressionResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Expression" in data:
        import aws_sdk_lakeformation.types.expression

        out["expression"] = aws_sdk_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    return out
