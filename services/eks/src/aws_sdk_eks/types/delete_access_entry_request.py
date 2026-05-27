"""Generated from Smithy shape ``com.amazonaws.eks#DeleteAccessEntryRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeleteAccessEntryRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "aws_sdk_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessEntryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessEntryRequest:
    out: DeleteAccessEntryRequest = {}  # type: ignore[typeddict-item]
    return out
