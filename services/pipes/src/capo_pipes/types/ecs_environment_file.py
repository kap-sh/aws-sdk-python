"""Generated from Smithy shape ``com.amazonaws.pipes#EcsEnvironmentFile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.ecs_environment_file_type
    import capo_pipes.types.string


class EcsEnvironmentFile(TypedDict, closed=True):
    type: "capo_pipes.types.ecs_environment_file_type.EcsEnvironmentFileType"
    """<p>The file type to use. The only supported value is <code>s3</code>.</p>"""
    value: "capo_pipes.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsEnvironmentFile) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EcsEnvironmentFile:
    out: EcsEnvironmentFile = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("EcsEnvironmentFile.type required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EcsEnvironmentFile.value required")
    return out
