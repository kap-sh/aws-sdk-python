"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateIntegrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.client_request_token
    import aws_sdk_wellarchitected.types.integrating_service
    import aws_sdk_wellarchitected.types.workload_id


class UpdateIntegrationInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    client_request_token: NotRequired[
        "aws_sdk_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    integrating_service: NotRequired[
        "aws_sdk_wellarchitected.types.integrating_service.IntegratingService"
    ]
    """<p>Which integrated service to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationInput) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "integrating_service" in value:
        import aws_sdk_wellarchitected.types.integrating_service

        out["IntegratingService"] = (
            aws_sdk_wellarchitected.types.integrating_service.serialize_json(
                value["integrating_service"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIntegrationInput:
    out: UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "IntegratingService" in data:
        import aws_sdk_wellarchitected.types.integrating_service

        out["integrating_service"] = (
            aws_sdk_wellarchitected.types.integrating_service.deserialize_json(
                data["IntegratingService"]
            )
        )
    return out
