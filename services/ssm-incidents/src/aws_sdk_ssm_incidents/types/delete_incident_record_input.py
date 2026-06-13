"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DeleteIncidentRecordInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class DeleteIncidentRecordInput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record you are deleting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIncidentRecordInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DeleteIncidentRecordInput:
    out: DeleteIncidentRecordInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteIncidentRecordInput.arn required")
    return out
