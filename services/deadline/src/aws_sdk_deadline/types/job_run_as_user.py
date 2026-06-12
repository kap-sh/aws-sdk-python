"""Generated from Smithy shape ``com.amazonaws.deadline#JobRunAsUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.posix_user
    import aws_sdk_deadline.types.run_as
    import aws_sdk_deadline.types.windows_user


class JobRunAsUser(TypedDict):
    posix: NotRequired["aws_sdk_deadline.types.posix_user.PosixUser"]
    """<p>The user and group that the jobs in the queue run as.</p>"""
    windows: NotRequired["aws_sdk_deadline.types.windows_user.WindowsUser"]
    """<p>Identifies a Microsoft Windows user.</p>"""
    run_as: "aws_sdk_deadline.types.run_as.RunAs"
    """<p>Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunAsUser) -> dict:
    out: dict = {}
    if "posix" in value:
        import aws_sdk_deadline.types.posix_user

        out["posix"] = aws_sdk_deadline.types.posix_user.serialize_json(value["posix"])
    if "windows" in value:
        import aws_sdk_deadline.types.windows_user

        out["windows"] = aws_sdk_deadline.types.windows_user.serialize_json(
            value["windows"]
        )
    import aws_sdk_deadline.types.run_as

    out["runAs"] = aws_sdk_deadline.types.run_as.serialize_json(value["run_as"])
    return out


def deserialize_json(data: dict) -> JobRunAsUser:
    out: JobRunAsUser = {}  # type: ignore[typeddict-item]
    if "posix" in data:
        import aws_sdk_deadline.types.posix_user

        out["posix"] = aws_sdk_deadline.types.posix_user.deserialize_json(data["posix"])
    if "windows" in data:
        import aws_sdk_deadline.types.windows_user

        out["windows"] = aws_sdk_deadline.types.windows_user.deserialize_json(
            data["windows"]
        )
    if "runAs" in data:
        import aws_sdk_deadline.types.run_as

        out["run_as"] = aws_sdk_deadline.types.run_as.deserialize_json(data["runAs"])
    else:
        raise DeserializationError("JobRunAsUser.run_as required")
    return out
