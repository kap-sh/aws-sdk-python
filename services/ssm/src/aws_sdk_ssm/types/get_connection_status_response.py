"""Generated from Smithy shape ``com.amazonaws.ssm#GetConnectionStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.connection_status
    import aws_sdk_ssm.types.session_target


class GetConnectionStatusResponse(TypedDict):
    target: NotRequired["aws_sdk_ssm.types.session_target.SessionTarget"]
    """<p>The ID of the managed node to check connection status. </p>"""
    status: NotRequired["aws_sdk_ssm.types.connection_status.ConnectionStatus"]
    """<p>The status of the connection to the managed node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionStatusResponse) -> dict:
    out: dict = {}
    if "target" in value:
        out["Target"] = value["target"]
    if "status" in value:
        import aws_sdk_ssm.types.connection_status

        out["Status"] = aws_sdk_ssm.types.connection_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionStatusResponse:
    out: GetConnectionStatusResponse = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Status" in data:
        import aws_sdk_ssm.types.connection_status

        out["status"] = aws_sdk_ssm.types.connection_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
