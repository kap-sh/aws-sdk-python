"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeResourceCollectionHealthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.resource_collection_type
    import capo_devops_guru.types.uuid_next_token


class DescribeResourceCollectionHealthRequest(TypedDict, closed=True):
    resource_collection_type: (
        "capo_devops_guru.types.resource_collection_type.ResourceCollectionType"
    )
    """<p> An Amazon Web Services resource collection type. This type specifies how analyzed Amazon Web Services resources are defined. The two types of Amazon Web Services resource collections supported are Amazon Web Services CloudFormation stacks and Amazon Web Services resources that contain the same Amazon Web Services tag. DevOps Guru can be configured to analyze the Amazon Web Services resources that are defined in the stacks or that are tagged using the same tag <i>key</i>. You can specify up to 500 Amazon Web Services CloudFormation stacks. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceCollectionHealthRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeResourceCollectionHealthRequest:
    out: DescribeResourceCollectionHealthRequest = {}  # type: ignore[typeddict-item]
    return out
