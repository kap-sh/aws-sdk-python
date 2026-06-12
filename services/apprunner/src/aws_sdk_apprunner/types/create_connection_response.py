"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.connection


class CreateConnectionResponse(TypedDict):
    connection: "aws_sdk_apprunner.types.connection.Connection"
    """<p>A description of the App Runner connection that's created by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateConnectionResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.connection

    out["Connection"] = aws_sdk_apprunner.types.connection.serialize_aws_json_1_0(
        value["connection"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateConnectionResponse:
    out: CreateConnectionResponse = {}  # type: ignore[typeddict-item]
    if "Connection" in data:
        import aws_sdk_apprunner.types.connection

        out["connection"] = aws_sdk_apprunner.types.connection.deserialize_aws_json_1_0(
            data["Connection"]
        )
    else:
        raise DeserializationError("CreateConnectionResponse.connection required")
    return out
