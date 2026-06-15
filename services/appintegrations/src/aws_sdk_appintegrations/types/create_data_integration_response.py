"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateDataIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.file_configuration
    import aws_sdk_appintegrations.types.idempotency_token
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.non_blank_string
    import aws_sdk_appintegrations.types.object_configuration
    import aws_sdk_appintegrations.types.schedule_configuration
    import aws_sdk_appintegrations.types.source_uri
    import aws_sdk_appintegrations.types.tag_map
    import aws_sdk_appintegrations.types.uuid


class CreateDataIntegrationResponse(TypedDict):
    arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN)</p>"""
    id: NotRequired["aws_sdk_appintegrations.types.uuid.UUID"]
    """<p>A unique identifier.</p>"""
    name: NotRequired["aws_sdk_appintegrations.types.name.Name"]
    """<p>The name of the DataIntegration.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>A description of the DataIntegration.</p>"""
    kms_key: NotRequired[
        "aws_sdk_appintegrations.types.non_blank_string.NonBlankString"
    ]
    """<p>The KMS key ARN for the DataIntegration.</p>"""
    source_uri: NotRequired["aws_sdk_appintegrations.types.source_uri.SourceURI"]
    """<p>The URI of the data source.</p>"""
    schedule_configuration: NotRequired[
        "aws_sdk_appintegrations.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The name of the data and how often it should be pulled from the source.</p>"""
    tags: NotRequired["aws_sdk_appintegrations.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    client_token: NotRequired[
        "aws_sdk_appintegrations.types.idempotency_token.IdempotencyToken"
    ]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    file_configuration: NotRequired[
        "aws_sdk_appintegrations.types.file_configuration.FileConfiguration"
    ]
    """<p>The configuration for what files should be pulled from the source.</p>"""
    object_configuration: NotRequired[
        "aws_sdk_appintegrations.types.object_configuration.ObjectConfiguration"
    ]
    """<p>The configuration for what data should be pulled from the source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataIntegrationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key" in value:
        out["KmsKey"] = value["kms_key"]
    if "source_uri" in value:
        out["SourceURI"] = value["source_uri"]
    if "schedule_configuration" in value:
        import aws_sdk_appintegrations.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            aws_sdk_appintegrations.types.schedule_configuration.serialize_json(
                value["schedule_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_appintegrations.types.tag_map

        out["Tags"] = aws_sdk_appintegrations.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "file_configuration" in value:
        import aws_sdk_appintegrations.types.file_configuration

        out["FileConfiguration"] = (
            aws_sdk_appintegrations.types.file_configuration.serialize_json(
                value["file_configuration"]
            )
        )
    if "object_configuration" in value:
        import aws_sdk_appintegrations.types.object_configuration

        out["ObjectConfiguration"] = (
            aws_sdk_appintegrations.types.object_configuration.serialize_json(
                value["object_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataIntegrationResponse:
    out: CreateDataIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "KmsKey" in data:
        out["kms_key"] = data["KmsKey"]
    if "SourceURI" in data:
        out["source_uri"] = data["SourceURI"]
    if "ScheduleConfiguration" in data:
        import aws_sdk_appintegrations.types.schedule_configuration

        out["schedule_configuration"] = (
            aws_sdk_appintegrations.types.schedule_configuration.deserialize_json(
                data["ScheduleConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_appintegrations.types.tag_map

        out["tags"] = aws_sdk_appintegrations.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "FileConfiguration" in data:
        import aws_sdk_appintegrations.types.file_configuration

        out["file_configuration"] = (
            aws_sdk_appintegrations.types.file_configuration.deserialize_json(
                data["FileConfiguration"]
            )
        )
    if "ObjectConfiguration" in data:
        import aws_sdk_appintegrations.types.object_configuration

        out["object_configuration"] = (
            aws_sdk_appintegrations.types.object_configuration.deserialize_json(
                data["ObjectConfiguration"]
            )
        )
    return out
