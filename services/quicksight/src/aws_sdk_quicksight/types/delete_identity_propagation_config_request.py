"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteIdentityPropagationConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.service_type


class DeleteIdentityPropagationConfigRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that you want to delete an identity propagation configuration from.</p>"""
    service: "aws_sdk_quicksight.types.service_type.ServiceType"
    """<p>The name of the Amazon Web Services service that you want to delete the associated access scopes and authorized targets from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdentityPropagationConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdentityPropagationConfigRequest:
    out: DeleteIdentityPropagationConfigRequest = {}  # type: ignore[typeddict-item]
    return out
