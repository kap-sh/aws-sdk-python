"""Generated from Smithy shape ``com.amazonaws.ecrpublic#CreateRepositoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.repository
    import aws_sdk_ecr_public.types.repository_catalog_data


class CreateRepositoryResponse(TypedDict):
    repository: NotRequired["aws_sdk_ecr_public.types.repository.Repository"]
    """<p>The repository that was created.</p>"""
    catalog_data: NotRequired[
        "aws_sdk_ecr_public.types.repository_catalog_data.RepositoryCatalogData"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryResponse) -> dict:
    out: dict = {}
    if "repository" in value:
        import aws_sdk_ecr_public.types.repository

        out["repository"] = aws_sdk_ecr_public.types.repository.serialize_aws_json_1_1(
            value["repository"]
        )
    if "catalog_data" in value:
        import aws_sdk_ecr_public.types.repository_catalog_data

        out["catalogData"] = (
            aws_sdk_ecr_public.types.repository_catalog_data.serialize_aws_json_1_1(
                value["catalog_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryResponse:
    out: CreateRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_ecr_public.types.repository

        out["repository"] = (
            aws_sdk_ecr_public.types.repository.deserialize_aws_json_1_1(
                data["repository"]
            )
        )
    if "catalogData" in data:
        import aws_sdk_ecr_public.types.repository_catalog_data

        out["catalog_data"] = (
            aws_sdk_ecr_public.types.repository_catalog_data.deserialize_aws_json_1_1(
                data["catalogData"]
            )
        )
    return out
