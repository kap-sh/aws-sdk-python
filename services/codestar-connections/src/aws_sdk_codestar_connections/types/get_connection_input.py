"""Generated from Smithy shape ``com.amazonaws.codestarconnections#GetConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.connection_arn


class GetConnectionInput(TypedDict, closed=True):
    connection_arn: "aws_sdk_codestar_connections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of a connection.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionInput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionInput:
    out: GetConnectionInput = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("GetConnectionInput.connection_arn required")
    return out
