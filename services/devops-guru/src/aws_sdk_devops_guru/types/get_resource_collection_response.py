"""Generated from Smithy shape ``com.amazonaws.devopsguru#GetResourceCollectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.resource_collection_filter
    import aws_sdk_devops_guru.types.uuid_next_token


class GetResourceCollectionResponse(TypedDict):
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection_filter.ResourceCollectionFilter"
    ]
    """<p> The requested list of Amazon Web Services resource collections. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceCollectionResponse) -> dict:
    out: dict = {}
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection_filter

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection_filter.serialize_json(
                value["resource_collection"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourceCollectionResponse:
    out: GetResourceCollectionResponse = {}  # type: ignore[typeddict-item]
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection_filter

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection_filter.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
