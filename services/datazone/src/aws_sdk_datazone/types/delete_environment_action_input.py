"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteEnvironmentActionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class DeleteEnvironmentActionInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which an environment action is deleted.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment where an environment action is deleted.</p>"""
    identifier: "str"
    """<p>The ID of the environment action that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentActionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentActionInput:
    out: DeleteEnvironmentActionInput = {}  # type: ignore[typeddict-item]
    return out
