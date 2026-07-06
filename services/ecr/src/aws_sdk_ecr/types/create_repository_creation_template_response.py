"""Generated from Smithy shape ``com.amazonaws.ecr#CreateRepositoryCreationTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_creation_template


class CreateRepositoryCreationTemplateResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_creation_template: NotRequired[
        "aws_sdk_ecr.types.repository_creation_template.RepositoryCreationTemplate"
    ]
    """<p>The details of the repository creation template associated with the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryCreationTemplateResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_creation_template" in value:
        import aws_sdk_ecr.types.repository_creation_template

        out["repositoryCreationTemplate"] = (
            aws_sdk_ecr.types.repository_creation_template.serialize_aws_json_1_1(
                value["repository_creation_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryCreationTemplateResponse:
    out: CreateRepositoryCreationTemplateResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryCreationTemplate" in data:
        import aws_sdk_ecr.types.repository_creation_template

        out["repository_creation_template"] = (
            aws_sdk_ecr.types.repository_creation_template.deserialize_aws_json_1_1(
                data["repositoryCreationTemplate"]
            )
        )
    return out
