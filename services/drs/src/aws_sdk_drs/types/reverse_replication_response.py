"""Generated from Smithy shape ``com.amazonaws.drs#ReverseReplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.source_server_arn


class ReverseReplicationResponse(TypedDict, closed=True):
    reversed_direction_source_server_arn: NotRequired[
        "aws_sdk_drs.types.source_server_arn.SourceServerARN"
    ]
    """<p>ARN of created SourceServer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReverseReplicationResponse) -> dict:
    out: dict = {}
    if "reversed_direction_source_server_arn" in value:
        out["reversedDirectionSourceServerArn"] = value[
            "reversed_direction_source_server_arn"
        ]
    return out


def deserialize_json(data: dict) -> ReverseReplicationResponse:
    out: ReverseReplicationResponse = {}  # type: ignore[typeddict-item]
    if "reversedDirectionSourceServerArn" in data:
        out["reversed_direction_source_server_arn"] = data[
            "reversedDirectionSourceServerArn"
        ]
    return out
