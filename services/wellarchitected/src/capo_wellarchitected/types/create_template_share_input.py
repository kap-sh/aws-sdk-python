"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateTemplateShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.shared_with
    import capo_wellarchitected.types.template_arn


class CreateTemplateShareInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    shared_with: NotRequired["capo_wellarchitected.types.shared_with.SharedWith"]
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateShareInput) -> dict:
    out: dict = {}
    if "shared_with" in value:
        out["SharedWith"] = value["shared_with"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateTemplateShareInput:
    out: CreateTemplateShareInput = {}  # type: ignore[typeddict-item]
    if "SharedWith" in data:
        out["shared_with"] = data["SharedWith"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
