"""Generated from Smithy shape ``com.amazonaws.ecrpublic#PutRegistryCatalogDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.registry_catalog_data


class PutRegistryCatalogDataResponse(TypedDict):
    registry_catalog_data: (
        "aws_sdk_ecr_public.types.registry_catalog_data.RegistryCatalogData"
    )
    """<p>The catalog data for the public registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryCatalogDataResponse) -> dict:
    out: dict = {}
    import aws_sdk_ecr_public.types.registry_catalog_data

    out["registryCatalogData"] = (
        aws_sdk_ecr_public.types.registry_catalog_data.serialize_aws_json_1_1(
            value["registry_catalog_data"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryCatalogDataResponse:
    out: PutRegistryCatalogDataResponse = {}  # type: ignore[typeddict-item]
    if "registryCatalogData" in data:
        import aws_sdk_ecr_public.types.registry_catalog_data

        out["registry_catalog_data"] = (
            aws_sdk_ecr_public.types.registry_catalog_data.deserialize_aws_json_1_1(
                data["registryCatalogData"]
            )
        )
    else:
        raise DeserializationError(
            "PutRegistryCatalogDataResponse.registry_catalog_data required"
        )
    return out
