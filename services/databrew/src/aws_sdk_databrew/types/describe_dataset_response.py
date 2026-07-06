"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.arn
    import aws_sdk_databrew.types.created_by
    import aws_sdk_databrew.types.dataset_name
    import aws_sdk_databrew.types.date
    import aws_sdk_databrew.types.format_options
    import aws_sdk_databrew.types.input
    import aws_sdk_databrew.types.input_format
    import aws_sdk_databrew.types.last_modified_by
    import aws_sdk_databrew.types.path_options
    import aws_sdk_databrew.types.source
    import aws_sdk_databrew.types.tag_map


class DescribeDatasetResponse(TypedDict, closed=True):
    created_by: NotRequired["aws_sdk_databrew.types.created_by.CreatedBy"]
    """<p>The identifier (user name) of the user who created the dataset.</p>"""
    create_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the dataset was created.</p>"""
    name: "aws_sdk_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset.</p>"""
    format: NotRequired["aws_sdk_databrew.types.input_format.InputFormat"]
    """<p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>"""
    format_options: NotRequired["aws_sdk_databrew.types.format_options.FormatOptions"]
    input: "aws_sdk_databrew.types.input.Input"
    last_modified_date: NotRequired["aws_sdk_databrew.types.date.Date"]
    """<p>The date and time that the dataset was last modified.</p>"""
    last_modified_by: NotRequired[
        "aws_sdk_databrew.types.last_modified_by.LastModifiedBy"
    ]
    """<p>The identifier (user name) of the user who last modified the dataset.</p>"""
    source: NotRequired["aws_sdk_databrew.types.source.Source"]
    """<p>The location of the data for this dataset, Amazon S3 or the Glue Data Catalog.</p>"""
    path_options: NotRequired["aws_sdk_databrew.types.path_options.PathOptions"]
    """<p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>"""
    tags: NotRequired["aws_sdk_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags associated with this dataset.</p>"""
    resource_arn: NotRequired["aws_sdk_databrew.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import aws_sdk_databrew.types.date

        out["CreateDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["create_date"]
        )
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
    if "last_modified_date" in value:
        import aws_sdk_databrew.types.date

        out["LastModifiedDate"] = aws_sdk_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "source" in value:
        import aws_sdk_databrew.types.source

        out["Source"] = aws_sdk_databrew.types.source.serialize_json(value["source"])
    if "path_options" in value:
        import aws_sdk_databrew.types.path_options

        out["PathOptions"] = aws_sdk_databrew.types.path_options.serialize_json(
            value["path_options"]
        )
    if "tags" in value:
        import aws_sdk_databrew.types.tag_map

        out["Tags"] = aws_sdk_databrew.types.tag_map.serialize_json(value["tags"])
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "CreateDate" in data:
        import aws_sdk_databrew.types.date

        out["create_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeDatasetResponse.name required")
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
        raise DeserializationError("DescribeDatasetResponse.input required")
    if "LastModifiedDate" in data:
        import aws_sdk_databrew.types.date

        out["last_modified_date"] = aws_sdk_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    if "Source" in data:
        import aws_sdk_databrew.types.source

        out["source"] = aws_sdk_databrew.types.source.deserialize_json(data["Source"])
    if "PathOptions" in data:
        import aws_sdk_databrew.types.path_options

        out["path_options"] = aws_sdk_databrew.types.path_options.deserialize_json(
            data["PathOptions"]
        )
    if "Tags" in data:
        import aws_sdk_databrew.types.tag_map

        out["tags"] = aws_sdk_databrew.types.tag_map.deserialize_json(data["Tags"])
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    return out
