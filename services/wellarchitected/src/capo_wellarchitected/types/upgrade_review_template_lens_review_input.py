"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpgradeReviewTemplateLensReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.client_request_token
    import capo_wellarchitected.types.lens_alias
    import capo_wellarchitected.types.template_arn


class UpgradeReviewTemplateLensReviewInput(TypedDict, closed=True):
    template_arn: "capo_wellarchitected.types.template_arn.TemplateArn"
    """<p>The ARN of the review template.</p>"""
    lens_alias: "capo_wellarchitected.types.lens_alias.LensAlias"
    client_request_token: NotRequired[
        "capo_wellarchitected.types.client_request_token.ClientRequestToken"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpgradeReviewTemplateLensReviewInput) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> UpgradeReviewTemplateLensReviewInput:
    out: UpgradeReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
