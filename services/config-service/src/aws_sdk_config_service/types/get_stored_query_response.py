"""Generated from Smithy shape ``com.amazonaws.configservice#GetStoredQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.stored_query


class GetStoredQueryResponse(TypedDict):
    stored_query: NotRequired["aws_sdk_config_service.types.stored_query.StoredQuery"]
    """<p>Returns a <code>StoredQuery</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStoredQueryResponse) -> dict:
    out: dict = {}
    if "stored_query" in value:
        import aws_sdk_config_service.types.stored_query

        out["StoredQuery"] = (
            aws_sdk_config_service.types.stored_query.serialize_aws_json_1_1(
                value["stored_query"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStoredQueryResponse:
    out: GetStoredQueryResponse = {}  # type: ignore[typeddict-item]
    if "StoredQuery" in data:
        import aws_sdk_config_service.types.stored_query

        out["stored_query"] = (
            aws_sdk_config_service.types.stored_query.deserialize_aws_json_1_1(
                data["StoredQuery"]
            )
        )
    return out
