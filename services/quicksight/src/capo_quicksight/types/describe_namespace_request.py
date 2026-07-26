"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class DescribeNamespaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that contains the Quick Sight namespace that you want to describe.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNamespaceRequest:
    out: DescribeNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
