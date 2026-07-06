"""Generated from Smithy shape ``com.amazonaws.glue#RegisterConnectionTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.glue_resource_arn


class RegisterConnectionTypeResponse(TypedDict, closed=True):
    connection_type_arn: NotRequired[
        "aws_sdk_glue.types.glue_resource_arn.GlueResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the registered connection type. This unique identifier can be used to reference the connection type in other Glue operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterConnectionTypeResponse) -> dict:
    out: dict = {}
    if "connection_type_arn" in value:
        out["ConnectionTypeArn"] = value["connection_type_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterConnectionTypeResponse:
    out: RegisterConnectionTypeResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionTypeArn" in data:
        out["connection_type_arn"] = data["ConnectionTypeArn"]
    return out
