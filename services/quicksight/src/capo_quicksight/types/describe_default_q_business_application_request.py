"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDefaultQBusinessApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class DescribeDefaultQBusinessApplicationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Quick Sight account that is linked to the Amazon Q Business application that you want described.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The Quick Sight namespace that contains the linked Amazon Q Business application. If this field is left blank, the default namespace is used. Currently, the default namespace is the only valid value for this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDefaultQBusinessApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDefaultQBusinessApplicationRequest:
    out: DescribeDefaultQBusinessApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
