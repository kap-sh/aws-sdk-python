"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#GetServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_id
    import aws_sdk_migration_hub_refactor_spaces.types.environment_id
    import aws_sdk_migration_hub_refactor_spaces.types.service_id


class GetServiceRequest(TypedDict, closed=True):
    environment_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment.</p>"""
    application_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>The ID of the application.</p>"""
    service_identifier: (
        "aws_sdk_migration_hub_refactor_spaces.types.service_id.ServiceId"
    )
    """<p>The ID of the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetServiceRequest:
    out: GetServiceRequest = {}  # type: ignore[typeddict-item]
    return out
