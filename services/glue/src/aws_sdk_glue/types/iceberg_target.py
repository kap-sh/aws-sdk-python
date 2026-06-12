"""Generated from Smithy shape ``com.amazonaws.glue#IcebergTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_name
    import aws_sdk_glue.types.nullable_integer
    import aws_sdk_glue.types.path_list


class IcebergTarget(TypedDict):
    paths: NotRequired["aws_sdk_glue.types.path_list.PathList"]
    """<p>One or more Amazon S3 paths that contains Iceberg metadata folders as <code>s3://bucket/prefix</code>.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the Iceberg target.</p>"""
    exclusions: NotRequired["aws_sdk_glue.types.path_list.PathList"]
    """<p>A list of glob patterns used to exclude from the crawl. For more information, see <a href=\"https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html\">Catalog Tables with a Crawler</a>.</p>"""
    maximum_traversal_depth: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The maximum depth of Amazon S3 paths that the crawler can traverse to discover the Iceberg metadata folder in your Amazon S3 path. Used to limit the crawler run time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergTarget) -> dict:
    out: dict = {}
    if "paths" in value:
        import aws_sdk_glue.types.path_list

        out["Paths"] = aws_sdk_glue.types.path_list.serialize_aws_json_1_1(
            value["paths"]
        )
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "exclusions" in value:
        import aws_sdk_glue.types.path_list

        out["Exclusions"] = aws_sdk_glue.types.path_list.serialize_aws_json_1_1(
            value["exclusions"]
        )
    if "maximum_traversal_depth" in value:
        out["MaximumTraversalDepth"] = value["maximum_traversal_depth"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergTarget:
    out: IcebergTarget = {}  # type: ignore[typeddict-item]
    if "Paths" in data:
        import aws_sdk_glue.types.path_list

        out["paths"] = aws_sdk_glue.types.path_list.deserialize_aws_json_1_1(
            data["Paths"]
        )
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "Exclusions" in data:
        import aws_sdk_glue.types.path_list

        out["exclusions"] = aws_sdk_glue.types.path_list.deserialize_aws_json_1_1(
            data["Exclusions"]
        )
    if "MaximumTraversalDepth" in data:
        out["maximum_traversal_depth"] = data["MaximumTraversalDepth"]
    return out
