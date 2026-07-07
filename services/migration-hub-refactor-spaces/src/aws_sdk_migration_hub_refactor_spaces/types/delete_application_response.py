"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.application_name
    import aws_sdk_migration_hub_refactor_spaces.types.application_state
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.resource_arn
    import aws_sdk_migration_hub_refactor_spaces.types.timestamp


class DeleteApplicationResponse(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_name.ApplicationName"
    ]
    """<p>The name of the application.</p>"""
    arn: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    ]
    """<p>The ID of the application.</p>"""
    environment_id: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the application’s environment.</p>"""
    state: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_state.ApplicationState"
    ]
    """<p>The current state of the application. </p>"""
    last_updated_time: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the environment was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_time" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApplicationResponse:
    out: DeleteApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "State" in data:
        out["state"] = data["State"]
    if "LastUpdatedTime" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
