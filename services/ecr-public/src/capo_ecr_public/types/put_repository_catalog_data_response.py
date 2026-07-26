"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutRepositoryCatalogDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.repository_catalog_data


class PutRepositoryCatalogDataResponse(TypedDict, closed=True):
    catalog_data: NotRequired[
        "capo_ecr_public.types.repository_catalog_data.RepositoryCatalogData"
    ]
    """<p>The catalog data for the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRepositoryCatalogDataResponse) -> dict:
    out: dict = {}
    if "catalog_data" in value:
        import capo_ecr_public.types.repository_catalog_data

        out["catalogData"] = (
            capo_ecr_public.types.repository_catalog_data.serialize_aws_json_1_1(
                value["catalog_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRepositoryCatalogDataResponse:
    out: PutRepositoryCatalogDataResponse = {}  # type: ignore[typeddict-item]
    if "catalogData" in data:
        import capo_ecr_public.types.repository_catalog_data

        out["catalog_data"] = (
            capo_ecr_public.types.repository_catalog_data.deserialize_aws_json_1_1(
                data["catalogData"]
            )
        )
    return out
