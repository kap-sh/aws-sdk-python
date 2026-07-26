"""Generated from Smithy shape ``com.amazonaws.lakeformation#PutDataLakeSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.data_lake_settings


class PutDataLakeSettingsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    data_lake_settings: "capo_lakeformation.types.data_lake_settings.DataLakeSettings"
    """<p>A structure representing a list of Lake Formation principals designated as data lake administrators.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDataLakeSettingsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.data_lake_settings

    out["DataLakeSettings"] = (
        capo_lakeformation.types.data_lake_settings.serialize_json(
            value["data_lake_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutDataLakeSettingsRequest:
    out: PutDataLakeSettingsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DataLakeSettings" in data:
        import capo_lakeformation.types.data_lake_settings

        out["data_lake_settings"] = (
            capo_lakeformation.types.data_lake_settings.deserialize_json(
                data["DataLakeSettings"]
            )
        )
    else:
        raise DeserializationError(
            "PutDataLakeSettingsRequest.data_lake_settings required"
        )
    return out
