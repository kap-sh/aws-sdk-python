"""Generated from Smithy shape ``com.amazonaws.databrew#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.format_options
    import aws_sdk_databrew.types.input
    import aws_sdk_databrew.types.input_format
    import aws_sdk_databrew.types.path_options
    import aws_sdk_databrew.types.tag_map


class CreateDatasetRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    format: NotRequired["aws_sdk_databrew.types.input_format.InputFormat"]
    """<p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>"""
    format_options: NotRequired["aws_sdk_databrew.types.format_options.FormatOptions"]
    input: "aws_sdk_databrew.types.input.Input"
    path_options: NotRequired["aws_sdk_databrew.types.path_options.PathOptions"]
    """<p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "format" in value:
        import aws_sdk_databrew.types.input_format

        out["Format"] = aws_sdk_databrew.types.input_format.serialize_json(
            value["format"]
        )
    if "format_options" in value:
        import aws_sdk_databrew.types.format_options

        out["FormatOptions"] = aws_sdk_databrew.types.format_options.serialize_json(
            value["format_options"]
        )
    import aws_sdk_databrew.types.input

    out["Input"] = aws_sdk_databrew.types.input.serialize_json(value["input"])
    if "path_options" in value:
        import aws_sdk_databrew.types.path_options

        out["PathOptions"] = aws_sdk_databrew.types.path_options.serialize_json(
            value["path_options"]
        )
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDatasetRequest.name required")
    if "Format" in data:
        import aws_sdk_databrew.types.input_format

        out["format"] = aws_sdk_databrew.types.input_format.deserialize_json(
            data["Format"]
        )
    if "FormatOptions" in data:
        import aws_sdk_databrew.types.format_options

        out["format_options"] = aws_sdk_databrew.types.format_options.deserialize_json(
            data["FormatOptions"]
        )
    if "Input" in data:
        import aws_sdk_databrew.types.input

        out["input"] = aws_sdk_databrew.types.input.deserialize_json(data["Input"])
    else:
        raise DeserializationError("CreateDatasetRequest.input required")
    if "PathOptions" in data:
        import aws_sdk_databrew.types.path_options

        out["path_options"] = aws_sdk_databrew.types.path_options.deserialize_json(
            data["PathOptions"]
        )
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
