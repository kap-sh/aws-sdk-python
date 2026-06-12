"""Generated from Smithy shape ``com.amazonaws.devopsguru#GetResourceCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.resource_collection_type
    import aws_sdk_devops_guru.types.uuid_next_token


class GetResourceCollectionRequest(TypedDict):
    resource_collection_type: (
        "aws_sdk_devops_guru.types.resource_collection_type.ResourceCollectionType"
    )
    """<p> The type of Amazon Web Services resource collections to return. The one valid value is <code>CLOUD_FORMATION</code> for Amazon Web Services CloudFormation stacks. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceCollectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetResourceCollectionRequest:
    out: GetResourceCollectionRequest = {}  # type: ignore[typeddict-item]
    return out
