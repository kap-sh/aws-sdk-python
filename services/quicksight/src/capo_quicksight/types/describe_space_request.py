"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.max_contributors
    import capo_quicksight.types.public_space_id


class DescribeSpaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the space.</p>"""
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space that you want to describe.</p>"""
    max_contributors: NotRequired[
        "capo_quicksight.types.max_contributors.MaxContributors"
    ]
    """<p>The maximum number of contributors to include in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSpaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSpaceRequest:
    out: DescribeSpaceRequest = {}  # type: ignore[typeddict-item]
    return out
