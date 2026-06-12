"""Generated from Smithy shape ``com.amazonaws.configservice#DeleteStoredQueryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.query_name


class DeleteStoredQueryRequest(TypedDict):
    query_name: "aws_sdk_config_service.types.query_name.QueryName"
    """<p>The name of the query that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStoredQueryRequest) -> dict:
    out: dict = {}
    out["QueryName"] = value["query_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStoredQueryRequest:
    out: DeleteStoredQueryRequest = {}  # type: ignore[typeddict-item]
    if "QueryName" in data:
        out["query_name"] = data["QueryName"]
    else:
        raise DeserializationError("DeleteStoredQueryRequest.query_name required")
    return out
