"""Generated from Smithy shape ``com.amazonaws.ecr#CreateRepositoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.repository


class CreateRepositoryResponse(TypedDict, closed=True):
    repository: NotRequired["capo_ecr.types.repository.Repository"]
    """<p>The repository that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryResponse) -> dict:
    out: dict = {}
    if "repository" in value:
        import capo_ecr.types.repository

        out["repository"] = capo_ecr.types.repository.serialize_aws_json_1_1(
            value["repository"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryResponse:
    out: CreateRepositoryResponse = {}  # type: ignore[typeddict-item]
    if "repository" in data:
        import capo_ecr.types.repository

        out["repository"] = capo_ecr.types.repository.deserialize_aws_json_1_1(
            data["repository"]
        )
    return out
