"""Generated from Smithy shape ``com.amazonaws.keyspaces#CreateKeyspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_keyspaces.types.arn


class CreateKeyspaceResponse(TypedDict, closed=True):
    resource_arn: "capo_keyspaces.types.arn.ARN"
    """<p>The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateKeyspaceResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateKeyspaceResponse:
    out: CreateKeyspaceResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("CreateKeyspaceResponse.resource_arn required")
    return out
