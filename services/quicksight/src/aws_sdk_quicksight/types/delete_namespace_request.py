"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace


class DeleteNamespaceRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to delete the Quick Sight namespace from.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
