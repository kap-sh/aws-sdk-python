"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListTemplateSharesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.list_template_shares_max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.share_status
    import aws_sdk_wellarchitected.types.shared_with_prefix
    import aws_sdk_wellarchitected.types.template_arn


class ListTemplateSharesInput(TypedDict):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    shared_with_prefix: NotRequired[
        "aws_sdk_wellarchitected.types.shared_with_prefix.SharedWithPrefix"
    ]
    """<p>The Amazon Web Services account ID, organization ID, or organizational unit (OU) ID with which the profile is shared.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired[
        "aws_sdk_wellarchitected.types.list_template_shares_max_results.ListTemplateSharesMaxResults"
    ]
    """<p>The maximum number of results to return for this request.</p>"""
    status: NotRequired["aws_sdk_wellarchitected.types.share_status.ShareStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplateSharesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplateSharesInput:
    out: ListTemplateSharesInput = {}  # type: ignore[typeddict-item]
    return out
