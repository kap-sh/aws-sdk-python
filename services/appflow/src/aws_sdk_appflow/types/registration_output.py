"""Generated from Smithy shape ``com.amazonaws.appflow#RegistrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_status
    import aws_sdk_appflow.types.string


class RegistrationOutput(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p>Explains the status of the registration attempt from Amazon AppFlow. If the attempt fails, the message explains why.</p>"""
    result: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p>Indicates the number of resources that Amazon AppFlow created or updated. Possible resources include metadata tables and data partitions.</p>"""
    status: NotRequired["aws_sdk_appflow.types.execution_status.ExecutionStatus"]
    """<p>Indicates the status of the registration attempt from Amazon AppFlow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationOutput) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "result" in value:
        out["result"] = value["result"]
    if "status" in value:
        import aws_sdk_appflow.types.execution_status

        out["status"] = aws_sdk_appflow.types.execution_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RegistrationOutput:
    out: RegistrationOutput = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "result" in data:
        out["result"] = data["result"]
    if "status" in data:
        import aws_sdk_appflow.types.execution_status

        out["status"] = aws_sdk_appflow.types.execution_status.deserialize_json(
            data["status"]
        )
    return out
