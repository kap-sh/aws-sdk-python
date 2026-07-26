"""Generated from Smithy shape ``com.amazonaws.m2#ListBatchJobRestartPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.auth_secrets_manager_arn
    import capo_m2.types.identifier


class ListBatchJobRestartPointsRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""
    execution_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the batch job execution.</p>"""
    auth_secrets_manager_arn: NotRequired[
        "capo_m2.types.auth_secrets_manager_arn.AuthSecretsManagerArn"
    ]
    """<p>The Amazon Web Services Secrets Manager containing user's credentials for authentication and authorization for List Batch Job Restart Points operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBatchJobRestartPointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBatchJobRestartPointsRequest:
    out: ListBatchJobRestartPointsRequest = {}  # type: ignore[typeddict-item]
    return out
