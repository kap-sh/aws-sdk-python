"""Generated from Smithy shape ``com.amazonaws.ecrpublic#DescribeImagesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.image_identifier_list
    import aws_sdk_ecr_public.types.max_results
    import aws_sdk_ecr_public.types.next_token
    import aws_sdk_ecr_public.types.registry_id
    import aws_sdk_ecr_public.types.repository_name


class DescribeImagesRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry that contains the repository where images are described. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    """<p>The repository that contains the images to describe.</p>"""
    image_ids: NotRequired[
        "aws_sdk_ecr_public.types.image_identifier_list.ImageIdentifierList"
    ]
    """<p>The list of image IDs for the requested repository.</p>"""
    next_token: NotRequired["aws_sdk_ecr_public.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value that's returned from a previous paginated <code>DescribeImages</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. If there are no more results to return, this value is <code>null</code>. If you specify images with <code>imageIds</code>, you can't use this option.</p>"""
    max_results: NotRequired["aws_sdk_ecr_public.types.max_results.MaxResults"]
    """<p>The maximum number of repository results that's returned by <code>DescribeImages</code> in paginated output. When this parameter is used, <code>DescribeImages</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>DescribeImages</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 1000. If this parameter isn't used, then <code>DescribeImages</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. If you specify images with <code>imageIds</code>, you can't use this option.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "image_ids" in value:
        import aws_sdk_ecr_public.types.image_identifier_list

        out["imageIds"] = (
            aws_sdk_ecr_public.types.image_identifier_list.serialize_aws_json_1_1(
                value["image_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesRequest:
    out: DescribeImagesRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("DescribeImagesRequest.repository_name required")
    if "imageIds" in data:
        import aws_sdk_ecr_public.types.image_identifier_list

        out["image_ids"] = (
            aws_sdk_ecr_public.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
