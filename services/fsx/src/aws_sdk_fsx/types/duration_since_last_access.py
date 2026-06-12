"""Generated from Smithy shape ``com.amazonaws.fsx#DurationSinceLastAccess``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.unit
    import aws_sdk_fsx.types.value


class DurationSinceLastAccess(TypedDict):
    unit: NotRequired["aws_sdk_fsx.types.unit.Unit"]
    """<p>The unit of time used by the <code>Value</code> parameter to determine if a file can be released, based on when it was last accessed. <code>DAYS</code> is the only supported value. This is a required parameter.</p>"""
    value: NotRequired["aws_sdk_fsx.types.value.Value"]
    """<p>An integer that represents the minimum amount of time (in days) since a file was last accessed in the file system. Only exported files with a <code>MAX(atime, ctime, mtime)</code> timestamp that is more than this amount of time in the past (relative to the task create time) will be released. The default of <code>Value</code> is <code>0</code>. This is a required parameter.</p> <note> <p>If an exported file meets the last accessed time criteria, its file or directory path must also be specified in the <code>Paths</code> parameter of the operation in order for the file to be released.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DurationSinceLastAccess) -> dict:
    out: dict = {}
    if "unit" in value:
        import aws_sdk_fsx.types.unit

        out["Unit"] = aws_sdk_fsx.types.unit.serialize_aws_json_1_1(value["unit"])
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DurationSinceLastAccess:
    out: DurationSinceLastAccess = {}  # type: ignore[typeddict-item]
    if "Unit" in data:
        import aws_sdk_fsx.types.unit

        out["unit"] = aws_sdk_fsx.types.unit.deserialize_aws_json_1_1(data["Unit"])
    if "Value" in data:
        out["value"] = data["Value"]
    return out
