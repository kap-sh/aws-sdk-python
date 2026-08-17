"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeRepositoryCreationTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_creation_template_list


class DescribeRepositoryCreationTemplatesResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_creation_templates: NotRequired[
        "capo_ecr.types.repository_creation_template_list.RepositoryCreationTemplateList"
    ]
    """<p>The details of the repository creation templates.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeRepositoryCreationTemplates</code> request. When the results of a <code>DescribeRepositoryCreationTemplates</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRepositoryCreationTemplatesResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_creation_templates" in value:
        import capo_ecr.types.repository_creation_template_list

        out["repositoryCreationTemplates"] = (
            capo_ecr.types.repository_creation_template_list.serialize_aws_json_1_1(
                value["repository_creation_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRepositoryCreationTemplatesResponse:
    out: DescribeRepositoryCreationTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryCreationTemplates") is not None:
        import capo_ecr.types.repository_creation_template_list

        out["repository_creation_templates"] = (
            capo_ecr.types.repository_creation_template_list.deserialize_aws_json_1_1(
                data["repositoryCreationTemplates"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
