"""Generated from Smithy shape ``com.amazonaws.configservice#GetStoredQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.query_name


class GetStoredQueryRequest(TypedDict, closed=True):
    query_name: "aws_sdk_config_service.types.query_name.QueryName"
    """<p>The name of the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStoredQueryRequest) -> dict:
    out: dict = {}
    out["QueryName"] = value["query_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStoredQueryRequest:
    out: GetStoredQueryRequest = {}  # type: ignore[typeddict-item]
    if "QueryName" in data:
        out["query_name"] = data["QueryName"]
    else:
        raise DeserializationError("GetStoredQueryRequest.query_name required")
    return out
