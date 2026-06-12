"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#GetCloudFormationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__string


class GetCloudFormationTemplateRequest(TypedDict):
    application_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    template_id: "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    """<p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCloudFormationTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCloudFormationTemplateRequest:
    out: GetCloudFormationTemplateRequest = {}  # type: ignore[typeddict-item]
    return out
