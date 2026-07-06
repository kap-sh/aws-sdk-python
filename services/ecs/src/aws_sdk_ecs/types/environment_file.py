"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentFile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.environment_file_type
    import aws_sdk_ecs.types.string


class EnvironmentFile(TypedDict, closed=True):
    value: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 object containing the environment variable file.</p>"""
    type: "aws_sdk_ecs.types.environment_file_type.EnvironmentFileType"
    """<p>The file type to use. Environment files are objects in Amazon S3. The only supported value is <code>s3</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentFile) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import aws_sdk_ecs.types.environment_file_type

    out["type"] = aws_sdk_ecs.types.environment_file_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentFile:
    out: EnvironmentFile = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnvironmentFile.value required")
    if "type" in data:
        import aws_sdk_ecs.types.environment_file_type

        out["type"] = aws_sdk_ecs.types.environment_file_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("EnvironmentFile.type required")
    return out
