"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog


class GetCatalogResponse(TypedDict):
    catalog: NotRequired["aws_sdk_glue.types.catalog.Catalog"]
    """<p>A <code>Catalog</code> object. The definition of the specified catalog in the Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogResponse) -> dict:
    out: dict = {}
    if "catalog" in value:
        import aws_sdk_glue.types.catalog

        out["Catalog"] = aws_sdk_glue.types.catalog.serialize_aws_json_1_1(
            value["catalog"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogResponse:
    out: GetCatalogResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        import aws_sdk_glue.types.catalog

        out["catalog"] = aws_sdk_glue.types.catalog.deserialize_aws_json_1_1(
            data["Catalog"]
        )
    return out
