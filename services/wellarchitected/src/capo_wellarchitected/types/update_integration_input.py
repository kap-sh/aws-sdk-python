"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.integrating_service
    import capo_wellarchitected.types.workload_id


class UpdateIntegrationInput(TypedDict, closed=True):
    workload_id: "capo_wellarchitected.types.workload_id.WorkloadId"
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]
    integrating_service: NotRequired[
        "capo_wellarchitected.types.integrating_service.IntegratingService"
    ]
    """<p>Which integrated service to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationInput) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "integrating_service" in value:
        import capo_wellarchitected.types.integrating_service

        out["IntegratingService"] = (
            capo_wellarchitected.types.integrating_service.serialize_json(
                value["integrating_service"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateIntegrationInput:
    out: UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "IntegratingService" in data:
        import capo_wellarchitected.types.integrating_service

        out["integrating_service"] = (
            capo_wellarchitected.types.integrating_service.deserialize_json(
                data["IntegratingService"]
            )
        )
    return out
