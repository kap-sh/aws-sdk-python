"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentCredentialsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_id


class GetEnvironmentCredentialsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this environment and its credentials exist.</p>"""
    environment_identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The ID of the environment whose credentials this operation gets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentCredentialsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentCredentialsInput:
    out: GetEnvironmentCredentialsInput = {}  # type: ignore[typeddict-item]
    return out
