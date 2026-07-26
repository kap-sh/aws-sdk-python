"""Generated from Smithy shape ``com.amazonaws.iot#UpdateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.role_arn
    import capo_iot.types.stream_description
    import capo_iot.types.stream_files
    import capo_iot.types.stream_id


class UpdateStreamRequest(TypedDict, closed=True):
    stream_id: "capo_iot.types.stream_id.StreamId"
    """<p>The stream ID.</p>"""
    description: NotRequired["capo_iot.types.stream_description.StreamDescription"]
    """<p>The description of the stream.</p>"""
    files: NotRequired["capo_iot.types.stream_files.StreamFiles"]
    """<p>The files associated with the stream.</p>"""
    role_arn: NotRequired["capo_iot.types.role_arn.RoleArn"]
    """<p>An IAM role that allows the IoT service principal assumes to access your S3 files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStreamRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "files" in value:
        import capo_iot.types.stream_files

        out["files"] = capo_iot.types.stream_files.serialize_json(value["files"])
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateStreamRequest:
    out: UpdateStreamRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "files" in data:
        import capo_iot.types.stream_files

        out["files"] = capo_iot.types.stream_files.deserialize_json(data["files"])
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
