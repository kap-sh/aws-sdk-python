"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateTemplateShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.share_id
    import aws_sdk_wellarchitected.types.template_arn


class CreateTemplateShareOutput(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_wellarchitected.types.template_arn.TemplateArn"]
    """<p>The review template ARN.</p>"""
    share_id: NotRequired["aws_sdk_wellarchitected.types.share_id.ShareId"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateShareOutput) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    if "share_id" in value:
        out["ShareId"] = value["share_id"]
    return out


def deserialize_json(data: dict) -> CreateTemplateShareOutput:
    out: CreateTemplateShareOutput = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    if "ShareId" in data:
        out["share_id"] = data["ShareId"]
    return out
