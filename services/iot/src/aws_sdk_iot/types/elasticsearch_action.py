"""Generated from Smithy shape ``com.amazonaws.iot#ElasticsearchAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_arn
    import aws_sdk_iot.types.elasticsearch_endpoint
    import aws_sdk_iot.types.elasticsearch_id
    import aws_sdk_iot.types.elasticsearch_index
    import aws_sdk_iot.types.elasticsearch_type


class ElasticsearchAction(TypedDict, closed=True):
    role_arn: "aws_sdk_iot.types.aws_arn.AwsArn"
    """<p>The IAM role ARN that has access to OpenSearch.</p>"""
    endpoint: "aws_sdk_iot.types.elasticsearch_endpoint.ElasticsearchEndpoint"
    """<p>The endpoint of your OpenSearch domain.</p>"""
    index: "aws_sdk_iot.types.elasticsearch_index.ElasticsearchIndex"
    """<p>The index where you want to store your data.</p>"""
    type: "aws_sdk_iot.types.elasticsearch_type.ElasticsearchType"
    """<p>The type of document you are storing.</p>"""
    id: "aws_sdk_iot.types.elasticsearch_id.ElasticsearchId"
    """<p>The unique identifier for the document you are storing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["endpoint"] = value["endpoint"]
    out["index"] = value["index"]
    out["type"] = value["type"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ElasticsearchAction:
    out: ElasticsearchAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ElasticsearchAction.role_arn required")
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("ElasticsearchAction.endpoint required")
    if "index" in data:
        out["index"] = data["index"]
    else:
        raise DeserializationError("ElasticsearchAction.index required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ElasticsearchAction.type required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ElasticsearchAction.id required")
    return out
