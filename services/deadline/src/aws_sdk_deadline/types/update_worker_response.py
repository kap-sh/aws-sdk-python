"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateWorkerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.host_configuration
    import aws_sdk_deadline.types.log_configuration


class UpdateWorkerResponse(TypedDict, closed=True):
    log: NotRequired["aws_sdk_deadline.types.log_configuration.LogConfiguration"]
    """<p>The worker log to update.</p>"""
    host_configuration: NotRequired[
        "aws_sdk_deadline.types.host_configuration.HostConfiguration"
    ]
    """<p>The script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkerResponse) -> dict:
    out: dict = {}
    if "log" in value:
        import aws_sdk_deadline.types.log_configuration

        out["log"] = aws_sdk_deadline.types.log_configuration.serialize_json(
            value["log"]
        )
    if "host_configuration" in value:
        import aws_sdk_deadline.types.host_configuration

        out["hostConfiguration"] = (
            aws_sdk_deadline.types.host_configuration.serialize_json(
                value["host_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateWorkerResponse:
    out: UpdateWorkerResponse = {}  # type: ignore[typeddict-item]
    if "log" in data:
        import aws_sdk_deadline.types.log_configuration

        out["log"] = aws_sdk_deadline.types.log_configuration.deserialize_json(
            data["log"]
        )
    if "hostConfiguration" in data:
        import aws_sdk_deadline.types.host_configuration

        out["host_configuration"] = (
            aws_sdk_deadline.types.host_configuration.deserialize_json(
                data["hostConfiguration"]
            )
        )
    return out
