"""Generated from Smithy shape ``com.amazonaws.configservice#PutStoredQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.query_arn


class PutStoredQueryResponse(TypedDict):
    query_arn: NotRequired["aws_sdk_config_service.types.query_arn.QueryArn"]
    """<p>Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutStoredQueryResponse) -> dict:
    out: dict = {}
    if "query_arn" in value:
        out["QueryArn"] = value["query_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutStoredQueryResponse:
    out: PutStoredQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryArn" in data:
        out["query_arn"] = data["QueryArn"]
    return out
