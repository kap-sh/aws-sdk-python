"""Generated from Smithy shape ``com.amazonaws.backup#UpdateFrameworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.framework_name
    import aws_sdk_backup.types.timestamp


class UpdateFrameworkOutput(TypedDict, closed=True):
    framework_name: NotRequired["aws_sdk_backup.types.framework_name.FrameworkName"]
    """<p>The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).</p>"""
    framework_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN depends on the resource type.</p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that a framework is created, in ISO 8601 representation. The value of <code>CreationTime</code> is accurate to milliseconds. For example, 2020-07-10T15:00:00.000-08:00 represents the 10th of July 2020 at 3:00 PM 8 hours behind UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFrameworkOutput) -> dict:
    out: dict = {}
    if "framework_name" in value:
        out["FrameworkName"] = value["framework_name"]
    if "framework_arn" in value:
        out["FrameworkArn"] = value["framework_arn"]
    if "creation_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFrameworkOutput:
    out: UpdateFrameworkOutput = {}  # type: ignore[typeddict-item]
    if "FrameworkName" in data:
        out["framework_name"] = data["FrameworkName"]
    if "FrameworkArn" in data:
        out["framework_arn"] = data["FrameworkArn"]
    if "CreationTime" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    return out
