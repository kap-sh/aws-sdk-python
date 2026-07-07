"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id


class GetEnvironmentRequest(TypedDict, closed=True):
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentRequest:
    out: GetEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
