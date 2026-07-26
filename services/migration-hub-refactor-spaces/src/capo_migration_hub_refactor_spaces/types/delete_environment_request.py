"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.environment_id


class DeleteEnvironmentRequest(TypedDict, closed=True):
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentRequest:
    out: DeleteEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
