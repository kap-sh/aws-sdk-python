"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#DeleteServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.application_id
    import capo_migration_hub_refactor_spaces.types.environment_id
    import capo_migration_hub_refactor_spaces.types.service_id


class DeleteServiceRequest(TypedDict, closed=True):
    environment_identifier: (
        "capo_migration_hub_refactor_spaces.types.environment_id.EnvironmentId"
    )
    """<p>The ID of the environment that the service is in.</p>"""
    application_identifier: (
        "capo_migration_hub_refactor_spaces.types.application_id.ApplicationId"
    )
    """<p>Deletes a Refactor Spaces service.</p> <note> <p>The <code>RefactorSpacesSecurityGroup</code> security group must be removed from all Amazon Web Services resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.</p> </note>"""
    service_identifier: "capo_migration_hub_refactor_spaces.types.service_id.ServiceId"
    """<p>The ID of the service to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceRequest:
    out: DeleteServiceRequest = {}  # type: ignore[typeddict-item]
    return out
