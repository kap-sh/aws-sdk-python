"""Generated from Smithy shape ``com.amazonaws.glue#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.code_gen_node_args


class Location(TypedDict, closed=True):
    jdbc: NotRequired["aws_sdk_glue.types.code_gen_node_args.CodeGenNodeArgs"]
    """<p>A JDBC location.</p>"""
    s3: NotRequired["aws_sdk_glue.types.code_gen_node_args.CodeGenNodeArgs"]
    """<p>An Amazon Simple Storage Service (Amazon S3) location.</p>"""
    dynamo_db: NotRequired["aws_sdk_glue.types.code_gen_node_args.CodeGenNodeArgs"]
    """<p>An Amazon DynamoDB table location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    if "jdbc" in value:
        import aws_sdk_glue.types.code_gen_node_args

        out["Jdbc"] = aws_sdk_glue.types.code_gen_node_args.serialize_aws_json_1_1(
            value["jdbc"]
        )
    if "s3" in value:
        import aws_sdk_glue.types.code_gen_node_args

        out["S3"] = aws_sdk_glue.types.code_gen_node_args.serialize_aws_json_1_1(
            value["s3"]
        )
    if "dynamo_db" in value:
        import aws_sdk_glue.types.code_gen_node_args

        out["DynamoDB"] = aws_sdk_glue.types.code_gen_node_args.serialize_aws_json_1_1(
            value["dynamo_db"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "Jdbc" in data:
        import aws_sdk_glue.types.code_gen_node_args

        out["jdbc"] = aws_sdk_glue.types.code_gen_node_args.deserialize_aws_json_1_1(
            data["Jdbc"]
        )
    if "S3" in data:
        import aws_sdk_glue.types.code_gen_node_args

        out["s3"] = aws_sdk_glue.types.code_gen_node_args.deserialize_aws_json_1_1(
            data["S3"]
        )
    if "DynamoDB" in data:
        import aws_sdk_glue.types.code_gen_node_args

        out["dynamo_db"] = (
            aws_sdk_glue.types.code_gen_node_args.deserialize_aws_json_1_1(
                data["DynamoDB"]
            )
        )
    return out
