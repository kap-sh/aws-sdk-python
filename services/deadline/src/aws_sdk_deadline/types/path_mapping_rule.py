"""Generated from Smithy shape ``com.amazonaws.deadline#PathMappingRule``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.path_format
    import aws_sdk_deadline.types.string


class PathMappingRule(TypedDict):
    source_path_format: "aws_sdk_deadline.types.path_format.PathFormat"
    """<p>The source path format.</p>"""
    source_path: "aws_sdk_deadline.types.string.String"
    """<p>The source path.</p>"""
    destination_path: "aws_sdk_deadline.types.string.String"
    """<p>The destination path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathMappingRule) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.path_format

    out["sourcePathFormat"] = aws_sdk_deadline.types.path_format.serialize_json(
        value["source_path_format"]
    )
    out["sourcePath"] = value["source_path"]
    out["destinationPath"] = value["destination_path"]
    return out


def deserialize_json(data: dict) -> PathMappingRule:
    out: PathMappingRule = {}  # type: ignore[typeddict-item]
    if "sourcePathFormat" in data:
        import aws_sdk_deadline.types.path_format

        out["source_path_format"] = aws_sdk_deadline.types.path_format.deserialize_json(
            data["sourcePathFormat"]
        )
    else:
        raise DeserializationError("PathMappingRule.source_path_format required")
    if "sourcePath" in data:
        out["source_path"] = data["sourcePath"]
    else:
        raise DeserializationError("PathMappingRule.source_path required")
    if "destinationPath" in data:
        out["destination_path"] = data["destinationPath"]
    else:
        raise DeserializationError("PathMappingRule.destination_path required")
    return out
