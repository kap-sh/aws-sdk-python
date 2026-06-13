"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteEnvironmentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class DeleteEnvironmentInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment that is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentInput:
    out: DeleteEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
