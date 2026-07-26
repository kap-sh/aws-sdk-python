"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DeleteRepositoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.repository


class DeleteRepositoryResponse(TypedDict, closed=True):
    repository: NotRequired["capo_ecr_public.types.repository.Repository"]
    """<p>The repository that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRepositoryResponse) -> dict:
    out: dict = {}
    if "repository" in value:
        import capo_ecr_public.types.repository

        out["repository"] = capo_ecr_public.types.repository.serialize_aws_json_1_1(
            value["repository"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRepositoryResponse:
    out: DeleteRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import capo_ecr_public.types.repository

        out["repository"] = capo_ecr_public.types.repository.deserialize_aws_json_1_1(
            data["repository"]
        )
    return out
