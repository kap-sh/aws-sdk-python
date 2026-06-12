"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DeleteRepositoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.repository


class DeleteRepositoryResponse(TypedDict):
    repository: NotRequired["aws_sdk_ecr_public.types.repository.Repository"]
    """<p>The repository that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryResponse) -> dict:
    out: dict = {}
    if "repository" in value:
        import aws_sdk_ecr_public.types.repository

        out["repository"] = aws_sdk_ecr_public.types.repository.serialize_aws_json_1_1(
            value["repository"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryResponse:
    out: DeleteRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import aws_sdk_ecr_public.types.repository

        out["repository"] = (
            aws_sdk_ecr_public.types.repository.deserialize_aws_json_1_1(
                data["repository"]
            )
        )
    return out
