"""Generated from Smithy shape ``com.amazonaws.configservice#SelectResourceConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.expression
    import aws_sdk_config_service.types.limit
    import aws_sdk_config_service.types.next_token


class SelectResourceConfigRequest(TypedDict):
    expression: "aws_sdk_config_service.types.expression.Expression"
    """<p>The SQL query <code>SELECT</code> command.</p>"""
    limit: "aws_sdk_config_service.types.limit.Limit"
    """<p>The maximum number of query results returned on each page. </p>"""
    next_token: NotRequired["aws_sdk_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned in a previous request that you use to request the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectResourceConfigRequest) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    out["Limit"] = value.get("limit", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectResourceConfigRequest:
    out: SelectResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    else:
        raise DeserializationError("SelectResourceConfigRequest.expression required")
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
