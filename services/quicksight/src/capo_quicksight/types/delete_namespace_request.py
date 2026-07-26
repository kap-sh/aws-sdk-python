"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class DeleteNamespaceRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to delete the Quick Sight namespace from.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNamespaceRequest:
    out: DeleteNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
