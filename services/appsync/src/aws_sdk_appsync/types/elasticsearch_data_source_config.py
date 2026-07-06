"""Generated from Smithy shape ``com.amazonaws.appsync#ElasticsearchDataSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class ElasticsearchDataSourceConfig(TypedDict, closed=True):
    endpoint: "aws_sdk_appsync.types.string.String"
    """<p>The endpoint.</p>"""
    aws_region: "aws_sdk_appsync.types.string.String"
    """<p>The Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchDataSourceConfig) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    out["awsRegion"] = value["aws_region"]
    return out


def deserialize_json(data: dict) -> ElasticsearchDataSourceConfig:
    out: ElasticsearchDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("ElasticsearchDataSourceConfig.endpoint required")
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    else:
        raise DeserializationError("ElasticsearchDataSourceConfig.aws_region required")
    return out
