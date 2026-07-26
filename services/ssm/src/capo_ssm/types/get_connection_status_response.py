"""Generated from Smithy shape ``com.amazonaws.ssm#GetConnectionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.connection_status
    import capo_ssm.types.session_target


class GetConnectionStatusResponse(TypedDict, closed=True):
    target: NotRequired["capo_ssm.types.session_target.SessionTarget"]
    """<p>The ID of the managed node to check connection status. </p>"""
    status: NotRequired["capo_ssm.types.connection_status.ConnectionStatus"]
    """<p>The status of the connection to the managed node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetConnectionStatusResponse) -> dict:
    out: dict = {}
    if "target" in value:
        out["Target"] = value["target"]
    if "status" in value:
        import capo_ssm.types.connection_status

        out["Status"] = capo_ssm.types.connection_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetConnectionStatusResponse:
    out: GetConnectionStatusResponse = {}  # type: ignore[typeddict-item]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Status" in data:
        import capo_ssm.types.connection_status

        out["status"] = capo_ssm.types.connection_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
