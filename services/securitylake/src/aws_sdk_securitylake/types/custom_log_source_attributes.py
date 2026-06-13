"""Generated from Smithy shape ``com.amazonaws.securitylake#CustomLogSourceAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securitylake.types.amazon_resource_name


class CustomLogSourceAttributes(TypedDict):
    crawler_arn: NotRequired[
        "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue crawler.</p>"""
    database_arn: NotRequired[
        "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue database where results are written, such as: <code>arn:aws:daylight:us-east-1::database/sometable/*</code>.</p>"""
    table_arn: NotRequired[
        "aws_sdk_securitylake.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the Glue table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLogSourceAttributes) -> dict:
    out: dict = {}
    if "crawler_arn" in value:
        out["crawlerArn"] = value["crawler_arn"]
    if "database_arn" in value:
        out["databaseArn"] = value["database_arn"]
    if "table_arn" in value:
        out["tableArn"] = value["table_arn"]
    return out


def deserialize_json(data: dict) -> CustomLogSourceAttributes:
    out: CustomLogSourceAttributes = {}  # type: ignore[typeddict-item]
    if "crawlerArn" in data:
        out["crawler_arn"] = data["crawlerArn"]
    if "databaseArn" in data:
        out["database_arn"] = data["databaseArn"]
    if "tableArn" in data:
        out["table_arn"] = data["tableArn"]
    return out
