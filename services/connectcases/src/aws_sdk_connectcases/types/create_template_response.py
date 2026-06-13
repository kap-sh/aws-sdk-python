"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.template_arn
    import aws_sdk_connectcases.types.template_id


class CreateTemplateResponse(TypedDict):
    template_id: "aws_sdk_connectcases.types.template_id.TemplateId"
    """<p>A unique identifier of a template.</p>"""
    template_arn: "aws_sdk_connectcases.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the newly created template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateResponse) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    return out


def deserialize_json(data: dict) -> CreateTemplateResponse:
    out: CreateTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateId" in data:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CreateTemplateResponse.template_id required")
    if "templateArn" in data:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("CreateTemplateResponse.template_arn required")
    return out
