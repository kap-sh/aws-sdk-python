"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class GetEnvironmentInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where the environment exists.</p>"""
    identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the Amazon DataZone environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentInput:
    out: GetEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
