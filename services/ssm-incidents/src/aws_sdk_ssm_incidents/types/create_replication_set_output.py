"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateReplicationSetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class CreateReplicationSetOutput(TypedDict, closed=True):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationSetOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateReplicationSetOutput:
    out: CreateReplicationSetOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateReplicationSetOutput.arn required")
    return out
