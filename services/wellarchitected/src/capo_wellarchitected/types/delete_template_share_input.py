"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteTemplateShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.share_id
    import capo_wellarchitected.types.template_arn


class DeleteTemplateShareInput(TypedDict, closed=True):
    share_id: "capo_wellarchitected.types.share_id.ShareId"
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTemplateShareInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTemplateShareInput:
    out: DeleteTemplateShareInput = {}  # type: ignore[typeddict-item]
    return out
