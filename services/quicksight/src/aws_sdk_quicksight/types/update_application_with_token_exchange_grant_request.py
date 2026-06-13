"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateApplicationWithTokenExchangeGrantRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace


class UpdateApplicationWithTokenExchangeGrantRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account to be updated with a token exchange grant.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The namespace of the Quick application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationWithTokenExchangeGrantRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UpdateApplicationWithTokenExchangeGrantRequest:
    out: UpdateApplicationWithTokenExchangeGrantRequest = {}  # type: ignore[typeddict-item]
    return out
