"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListExecutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.max_results
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.resolve_to_resource_type
    import aws_sdk_iotsitewise.types.target_resource_type


class ListExecutionsRequest(TypedDict):
    target_resource_type: (
        "aws_sdk_iotsitewise.types.target_resource_type.TargetResourceType"
    )
    """<p>The type of the target resource.</p>"""
    target_resource_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the target resource.</p>"""
    resolve_to_resource_type: NotRequired[
        "aws_sdk_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
    ]
    """<p>The type of the resolved resource.</p>"""
    resolve_to_resource_id: NotRequired["aws_sdk_iotsitewise.types.id.ID"]
    """<p>The ID of the resolved resource.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token used for the next set of paginated results.</p>"""
    max_results: NotRequired["aws_sdk_iotsitewise.types.max_results.MaxResults"]
    """<p>The maximum number of results returned for each paginated request.</p>"""
    action_type: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The type of action exectued.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExecutionsRequest:
    out: ListExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
