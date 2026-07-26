"""Generated from Smithy shape ``com.amazonaws.ecrpublic#GetRegistryCatalogDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr_public.types.registry_catalog_data


class GetRegistryCatalogDataResponse(TypedDict, closed=True):
    registry_catalog_data: (
        "capo_ecr_public.types.registry_catalog_data.RegistryCatalogData"
    )
    """<p>The catalog metadata for the public registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegistryCatalogDataResponse) -> dict:
    out: dict = {}
    import capo_ecr_public.types.registry_catalog_data

    out["registryCatalogData"] = (
        capo_ecr_public.types.registry_catalog_data.serialize_aws_json_1_1(
            value["registry_catalog_data"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegistryCatalogDataResponse:
    out: GetRegistryCatalogDataResponse = {}  # type: ignore[typeddict-item]
    if "registryCatalogData" in data:
        import capo_ecr_public.types.registry_catalog_data

        out["registry_catalog_data"] = (
            capo_ecr_public.types.registry_catalog_data.deserialize_aws_json_1_1(
                data["registryCatalogData"]
            )
        )
    else:
        raise DeserializationError(
            "GetRegistryCatalogDataResponse.registry_catalog_data required"
        )
    return out
