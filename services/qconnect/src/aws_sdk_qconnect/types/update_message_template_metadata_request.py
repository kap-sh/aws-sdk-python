"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateMessageTemplateMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.description
    import aws_sdk_qconnect.types.grouping_configuration
    import aws_sdk_qconnect.types.name
    import aws_sdk_qconnect.types.uuid_or_arn
    import aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier


class UpdateMessageTemplateMetadataRequest(TypedDict):
    knowledge_base_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "aws_sdk_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    name: NotRequired["aws_sdk_qconnect.types.name.Name"]
    """<p>The name of the message template.</p>"""
    description: NotRequired["aws_sdk_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    grouping_configuration: NotRequired[
        "aws_sdk_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMessageTemplateMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "grouping_configuration" in value:
        import aws_sdk_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            aws_sdk_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMessageTemplateMetadataRequest:
    out: UpdateMessageTemplateMetadataRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "groupingConfiguration" in data:
        import aws_sdk_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            aws_sdk_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    return out
