"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecyclePoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_summary_list
    import aws_sdk_imagebuilder.types.pagination_token


class ListLifecyclePoliciesResponse(TypedDict):
    lifecycle_policy_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_summary_list.LifecyclePolicySummaryList"
    ]
    """<p>A list of lifecycle policies in your Amazon Web Services account that meet the criteria specified in the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecyclePoliciesResponse) -> dict:
    out: dict = {}
    if "lifecycle_policy_summary_list" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_summary_list

        out["lifecyclePolicySummaryList"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_summary_list.serialize_json(
                value["lifecycle_policy_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLifecyclePoliciesResponse:
    out: ListLifecyclePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "lifecyclePolicySummaryList" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_summary_list

        out["lifecycle_policy_summary_list"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_summary_list.deserialize_json(
                data["lifecyclePolicySummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
