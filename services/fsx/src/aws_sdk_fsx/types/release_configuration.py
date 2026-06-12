"""Generated from Smithy shape ``com.amazonaws.fsx#ReleaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.duration_since_last_access


class ReleaseConfiguration(TypedDict):
    duration_since_last_access: NotRequired[
        "aws_sdk_fsx.types.duration_since_last_access.DurationSinceLastAccess"
    ]
    """<p>Defines the point-in-time since an exported file was last accessed, in order for that file to be eligible for release. Only files that were last accessed before this point-in-time are eligible to be released from the file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseConfiguration) -> dict:
    out: dict = {}
    if "duration_since_last_access" in value:
        import aws_sdk_fsx.types.duration_since_last_access

        out["DurationSinceLastAccess"] = (
            aws_sdk_fsx.types.duration_since_last_access.serialize_aws_json_1_1(
                value["duration_since_last_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseConfiguration:
    out: ReleaseConfiguration = {}  # type: ignore[typeddict-item]
    if "DurationSinceLastAccess" in data:
        import aws_sdk_fsx.types.duration_since_last_access

        out["duration_since_last_access"] = (
            aws_sdk_fsx.types.duration_since_last_access.deserialize_aws_json_1_1(
                data["DurationSinceLastAccess"]
            )
        )
    return out
