"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DeleteReviewTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.template_arn


class DeleteReviewTemplateInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReviewTemplateInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteReviewTemplateInput:
    out: DeleteReviewTemplateInput = {}  # type: ignore[typeddict-item]
    return out
