"""Generated from Smithy shape ``com.amazonaws.mq#UpdateConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__list_of_sanitization_warning
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.__timestamp_iso8601
    import aws_sdk_mq.types.configuration_revision


class UpdateConfigurationResponse(TypedDict):
    arn: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the configuration.</p>"""
    created: NotRequired["aws_sdk_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>Required. The date and time of the configuration.</p>"""
    id: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The unique ID that Amazon MQ generates for the configuration.</p>"""
    latest_revision: NotRequired[
        "aws_sdk_mq.types.configuration_revision.ConfigurationRevision"
    ]
    """<p>The latest revision of the configuration.</p>"""
    name: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.</p>"""
    warnings: NotRequired[
        "aws_sdk_mq.types.__list_of_sanitization_warning.__listOfSanitizationWarning"
    ]
    """<p>The list of the first 20 warnings about the configuration elements or attributes that were sanitized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created" in value:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "id" in value:
        out["id"] = value["id"]
    if "latest_revision" in value:
        import aws_sdk_mq.types.configuration_revision

        out["latestRevision"] = aws_sdk_mq.types.configuration_revision.serialize_json(
            value["latest_revision"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "warnings" in value:
        import aws_sdk_mq.types.__list_of_sanitization_warning

        out["warnings"] = (
            aws_sdk_mq.types.__list_of_sanitization_warning.serialize_json(
                value["warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationResponse:
    out: UpdateConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "created" in data:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "id" in data:
        out["id"] = data["id"]
    if "latestRevision" in data:
        import aws_sdk_mq.types.configuration_revision

        out["latest_revision"] = (
            aws_sdk_mq.types.configuration_revision.deserialize_json(
                data["latestRevision"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "warnings" in data:
        import aws_sdk_mq.types.__list_of_sanitization_warning

        out["warnings"] = (
            aws_sdk_mq.types.__list_of_sanitization_warning.deserialize_json(
                data["warnings"]
            )
        )
    return out
