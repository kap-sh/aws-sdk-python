"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeTemplatePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class DescribeTemplatePermissionsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template that you're describing.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTemplatePermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTemplatePermissionsRequest:
    out: DescribeTemplatePermissionsRequest = {}  # type: ignore[typeddict-item]
    return out
