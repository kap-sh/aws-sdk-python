"""Generated from Smithy shape ``com.amazonaws.backup#CreateTieringConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.creator_request_id
    import aws_sdk_backup.types.tags
    import aws_sdk_backup.types.tiering_configuration_input_for_create


class CreateTieringConfigurationInput(TypedDict, closed=True):
    tiering_configuration: "aws_sdk_backup.types.tiering_configuration_input_for_create.TieringConfigurationInputForCreate"
    """<p>A tiering configuration must contain a unique <code>TieringConfigurationName</code> string you create and must contain a <code>BackupVaultName</code> and <code>ResourceSelection</code>. You may optionally include a <code>CreatorRequestId</code> string.</p> <p>The <code>TieringConfigurationName</code> is a unique string that is the name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tiering_configuration_tags: NotRequired["aws_sdk_backup.types.tags.Tags"]
    """<p>The tags to assign to the tiering configuration.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_backup.types.creator_request_id.CreatorRequestId"
    ]
    """<p>This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTieringConfigurationInput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.tiering_configuration_input_for_create

    out["TieringConfiguration"] = (
        aws_sdk_backup.types.tiering_configuration_input_for_create.serialize_json(
            value["tiering_configuration"]
        )
    )
    if "tiering_configuration_tags" in value:
        import aws_sdk_backup.types.tags

        out["TieringConfigurationTags"] = aws_sdk_backup.types.tags.serialize_json(
            value["tiering_configuration_tags"]
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateTieringConfigurationInput:
    out: CreateTieringConfigurationInput = {}  # type: ignore[typeddict-item]
    if "TieringConfiguration" in data:
        import aws_sdk_backup.types.tiering_configuration_input_for_create

        out["tiering_configuration"] = (
            aws_sdk_backup.types.tiering_configuration_input_for_create.deserialize_json(
                data["TieringConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTieringConfigurationInput.tiering_configuration required"
        )
    if "TieringConfigurationTags" in data:
        import aws_sdk_backup.types.tags

        out["tiering_configuration_tags"] = aws_sdk_backup.types.tags.deserialize_json(
            data["TieringConfigurationTags"]
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out
