"""Generated from Smithy shape ``com.amazonaws.lakeformation#DescribeLakeFormationIdentityCenterConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string


class DescribeLakeFormationIdentityCenterConfigurationRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: DescribeLakeFormationIdentityCenterConfigurationRequest,
) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_json(
    data: dict,
) -> DescribeLakeFormationIdentityCenterConfigurationRequest:
    out: DescribeLakeFormationIdentityCenterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out
