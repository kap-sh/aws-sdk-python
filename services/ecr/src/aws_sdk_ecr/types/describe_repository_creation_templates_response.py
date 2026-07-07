"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRepositoryCreationTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.next_token
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_creation_template_list


class DescribeRepositoryCreationTemplatesResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_creation_templates: NotRequired[
        "aws_sdk_ecr.types.repository_creation_template_list.RepositoryCreationTemplateList"
    ]
    """<p>The details of the repository creation templates.</p>"""
    next_token: NotRequired["aws_sdk_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeRepositoryCreationTemplates</code> request. When the results of a <code>DescribeRepositoryCreationTemplates</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRepositoryCreationTemplatesResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_creation_templates" in value:
        import aws_sdk_ecr.types.repository_creation_template_list

        out["repositoryCreationTemplates"] = (
            aws_sdk_ecr.types.repository_creation_template_list.serialize_aws_json_1_1(
                value["repository_creation_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRepositoryCreationTemplatesResponse:
    out: DescribeRepositoryCreationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryCreationTemplates" in data:
        import aws_sdk_ecr.types.repository_creation_template_list

        out["repository_creation_templates"] = (
            aws_sdk_ecr.types.repository_creation_template_list.deserialize_aws_json_1_1(
                data["repositoryCreationTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
