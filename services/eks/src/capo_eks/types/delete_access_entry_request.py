"""Generated from Smithy shape ``com.amazonaws.eks#DeleteAccessEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DeleteAccessEntryRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "capo_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessEntryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessEntryRequest:
    out: DeleteAccessEntryRequest = {}  # type: ignore[typeddict-item]
    return out
