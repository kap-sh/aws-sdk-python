"""Generated from Smithy shape ``com.amazonaws.keyspaces#UpdateKeyspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.arn


class UpdateKeyspaceResponse(TypedDict, closed=True):
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p> The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateKeyspaceResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateKeyspaceResponse:
    out: UpdateKeyspaceResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("UpdateKeyspaceResponse.resource_arn required")
    return out
