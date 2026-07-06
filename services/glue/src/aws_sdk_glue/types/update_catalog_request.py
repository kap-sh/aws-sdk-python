"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.catalog_input


class UpdateCatalogRequest(TypedDict, closed=True):
    catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog.</p>"""
    catalog_input: "aws_sdk_glue.types.catalog_input.CatalogInput"
    """<p>A <code>CatalogInput</code> object specifying the new properties of an existing catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCatalogRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    import aws_sdk_glue.types.catalog_input

    out["CatalogInput"] = aws_sdk_glue.types.catalog_input.serialize_aws_json_1_1(
        value["catalog_input"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCatalogRequest:
    out: UpdateCatalogRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("UpdateCatalogRequest.catalog_id required")
    if "CatalogInput" in data:
        import aws_sdk_glue.types.catalog_input

        out["catalog_input"] = (
            aws_sdk_glue.types.catalog_input.deserialize_aws_json_1_1(
                data["CatalogInput"]
            )
        )
    else:
        raise DeserializationError("UpdateCatalogRequest.catalog_input required")
    return out
