"""Generated from Smithy shape ``com.amazonaws.keyspaces#CreateTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn


class CreateTableResponse(TypedDict, closed=True):
    resource_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The unique identifier of the table in the format of an Amazon Resource Name (ARN).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTableResponse) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTableResponse:
    out: CreateTableResponse = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("CreateTableResponse.resource_arn required")
    return out
