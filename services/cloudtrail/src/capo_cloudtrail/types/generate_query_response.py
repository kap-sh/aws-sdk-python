"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GenerateQueryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.query_alias
    import capo_cloudtrail.types.query_statement


class GenerateQueryResponse(TypedDict, closed=True):
    query_statement: NotRequired["capo_cloudtrail.types.query_statement.QueryStatement"]
    """<p> The SQL query statement generated from the prompt. </p>"""
    query_alias: NotRequired["capo_cloudtrail.types.query_alias.QueryAlias"]
    """<p> An alias that identifies the prompt. When you run the <code>StartQuery</code> operation, you can pass in either the <code>QueryAlias</code> or <code>QueryStatement</code> parameter. </p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateQueryResponse) -> dict:
    out: dict = {}
    if "query_statement" in value:
        out["QueryStatement"] = value["query_statement"]
    if "query_alias" in value:
        out["QueryAlias"] = value["query_alias"]
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerateQueryResponse:
    out: GenerateQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    if "QueryAlias" in data:
        out["query_alias"] = data["QueryAlias"]
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
