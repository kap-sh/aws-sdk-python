"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateLFTagExpressionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.description_string
    import aws_sdk_lakeformation.types.expression
    import aws_sdk_lakeformation.types.name_string


class UpdateLFTagExpressionRequest(TypedDict):
    name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name for the LF-Tag expression.</p>"""
    description: NotRequired[
        "aws_sdk_lakeformation.types.description_string.DescriptionString"
    ]
    """<p>The description with information about the saved LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. </p>"""
    expression: "aws_sdk_lakeformation.types.expression.Expression"
    """<p>The LF-Tag expression body composed of one more LF-Tag key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLFTagExpressionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import aws_sdk_lakeformation.types.expression

    out["Expression"] = aws_sdk_lakeformation.types.expression.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> UpdateLFTagExpressionRequest:
    out: UpdateLFTagExpressionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateLFTagExpressionRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Expression" in data:
        import aws_sdk_lakeformation.types.expression

        out["expression"] = aws_sdk_lakeformation.types.expression.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("UpdateLFTagExpressionRequest.expression required")
    return out
