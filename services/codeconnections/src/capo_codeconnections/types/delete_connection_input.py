"""Generated from Smithy shape ``com.amazonaws.codeconnections#DeleteConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.connection_arn


class DeleteConnectionInput(TypedDict, closed=True):
    connection_arn: "capo_codeconnections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to be deleted.</p> <note> <p>The ARN is never reused if the connection is deleted.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionInput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionInput:
    out: DeleteConnectionInput = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("DeleteConnectionInput.connection_arn required")
    return out
