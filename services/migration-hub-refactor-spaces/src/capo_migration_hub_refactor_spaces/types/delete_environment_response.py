"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.environment_name
    import capo_migration_hub_refactor_spaces.types.environment_state
    import capo_migration_hub_refactor_spaces.types.resource_arn
    import capo_migration_hub_refactor_spaces.types.timestamp


class DeleteEnvironmentResponse(TypedDict, closed=True):
    name: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment.</p>"""
    arn: NotRequired[
        "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the environment.</p>"""
    environment_id: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    ]
    """<p>The unique identifier of the environment.</p>"""
    state: NotRequired[
        "capo_migration_hub_refactor_spaces.types.environment_state.EnvironmentState"
    ]
    """<p>The current state of the environment. </p>"""
    last_updated_time: NotRequired[
        "capo_migration_hub_refactor_spaces.types.timestamp.Timestamp"
    ]
    """<p>A timestamp that indicates when the environment was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "state" in value:
        out["State"] = value["state"]
    if "last_updated_time" in value:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["LastUpdatedTime"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentResponse:
    out: DeleteEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "State" in data:
        out["state"] = data["State"]
    if "LastUpdatedTime" in data:
        import capo_migration_hub_refactor_spaces.types.timestamp

        out["last_updated_time"] = (
            capo_migration_hub_refactor_spaces.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    return out
