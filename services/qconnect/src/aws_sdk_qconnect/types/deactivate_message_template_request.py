"""Generated from Smithy shape ``com.amazonaws.qconnect#DeactivateMessageTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import aws_sdk_qconnect.types.version


class DeactivateMessageTemplateRequest(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    version_number: "aws_sdk_qconnect.types.version.Version"
    """<p>The version number of the message template version to deactivate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeactivateMessageTemplateRequest) -> dict:
    out: dict = {}
    out["versionNumber"] = value["version_number"]
    return out


def deserialize_json(data: dict) -> DeactivateMessageTemplateRequest:
    out: DeactivateMessageTemplateRequest = {}  # type: ignore[typeddict-item]
    if "versionNumber" in data:
        out["version_number"] = data["versionNumber"]
    else:
        raise DeserializationError(
            "DeactivateMessageTemplateRequest.version_number required"
        )
    return out
