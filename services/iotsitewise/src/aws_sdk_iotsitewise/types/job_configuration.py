"""Generated from Smithy shape ``com.amazonaws.iotsitewise#JobConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.file_format


class JobConfiguration(TypedDict):
    file_format: "aws_sdk_iotsitewise.types.file_format.FileFormat"
    """<p>The file format of the data in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.file_format

    out["fileFormat"] = aws_sdk_iotsitewise.types.file_format.serialize_json(
        value["file_format"]
    )
    return out


def deserialize_json(data: dict) -> JobConfiguration:
    out: JobConfiguration = {}  # type: ignore[typeddict-item]
    if "fileFormat" in data:
        import aws_sdk_iotsitewise.types.file_format

        out["file_format"] = aws_sdk_iotsitewise.types.file_format.deserialize_json(
            data["fileFormat"]
        )
    else:
        raise DeserializationError("JobConfiguration.file_format required")
    return out
