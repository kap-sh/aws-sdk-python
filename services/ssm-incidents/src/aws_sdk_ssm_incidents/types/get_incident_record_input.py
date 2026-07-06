"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetIncidentRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class GetIncidentRecordInput(TypedDict, closed=True):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIncidentRecordInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIncidentRecordInput:
    out: GetIncidentRecordInput = {}  # type: ignore[typeddict-item]
    return out
