"""Generated from Smithy shape ``com.amazonaws.glue#CreateConnectionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_status


class CreateConnectionResponse(TypedDict, closed=True):
    create_connection_status: NotRequired[
        "aws_sdk_glue.types.connection_status.ConnectionStatus"
    ]
    """<p>The status of the connection creation request. The request can take some time for certain authentication types, for example when creating an OAuth connection with token exchange over VPC.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionResponse) -> dict:
    out: dict = {}
    if "create_connection_status" in value:
        import aws_sdk_glue.types.connection_status

        out["CreateConnectionStatus"] = (
            aws_sdk_glue.types.connection_status.serialize_aws_json_1_1(
                value["create_connection_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionResponse:
    out: CreateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "CreateConnectionStatus" in data:
        import aws_sdk_glue.types.connection_status

        out["create_connection_status"] = (
            aws_sdk_glue.types.connection_status.deserialize_aws_json_1_1(
                data["CreateConnectionStatus"]
            )
        )
    return out
