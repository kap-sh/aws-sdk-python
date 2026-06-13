"""Generated from Smithy shape ``com.amazonaws.datazone#GetJobRunInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.run_identifier


class GetJobRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain.</p>"""
    identifier: "aws_sdk_datazone.types.run_identifier.RunIdentifier"
    """<p>The ID of the job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobRunInput:
    out: GetJobRunInput = {}  # type: ignore[typeddict-item]
    return out
