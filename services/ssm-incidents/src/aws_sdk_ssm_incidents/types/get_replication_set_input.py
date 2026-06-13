"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetReplicationSetInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class GetReplicationSetInput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReplicationSetInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetReplicationSetInput:
    out: GetReplicationSetInput = {}  # type: ignore[typeddict-item]
    return out
