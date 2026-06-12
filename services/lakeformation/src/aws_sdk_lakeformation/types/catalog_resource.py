"""Generated from Smithy shape ``com.amazonaws.lakeformation#CatalogResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string


class CatalogResource(TypedDict):
    id: NotRequired["aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"]
    """<p>An identifier for the catalog resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CatalogResource) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CatalogResource:
    out: CatalogResource = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
