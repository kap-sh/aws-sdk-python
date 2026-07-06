"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CreateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.template_arn


class CreateTemplateResponse(TypedDict, closed=True):
    template_arn: NotRequired["aws_sdk_pca_connector_ad.types.template_arn.TemplateArn"]
    """<p>If successful, the Amazon Resource Name (ARN) of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateResponse) -> dict:
    out: dict = {}
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> CreateTemplateResponse:
    out: CreateTemplateResponse = {}  # type: ignore[typeddict-item]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
    return out
