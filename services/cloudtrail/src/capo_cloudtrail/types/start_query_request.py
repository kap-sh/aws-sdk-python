"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StartQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.account_id
    import capo_cloudtrail.types.delivery_s3_uri
    import capo_cloudtrail.types.query_alias
    import capo_cloudtrail.types.query_parameters
    import capo_cloudtrail.types.query_statement


class StartQueryRequest(TypedDict, closed=True):
    query_statement: NotRequired["capo_cloudtrail.types.query_statement.QueryStatement"]
    """<p>The SQL code of your query.</p>"""
    delivery_s3_uri: NotRequired["capo_cloudtrail.types.delivery_s3_uri.DeliveryS3Uri"]
    """<p> The URI for the S3 bucket where CloudTrail delivers the query results. </p>"""
    query_alias: NotRequired["capo_cloudtrail.types.query_alias.QueryAlias"]
    """<p> The alias that identifies a query template. </p>"""
    query_parameters: NotRequired[
        "capo_cloudtrail.types.query_parameters.QueryParameters"
    ]
    """<p> The query parameters for the specified <code>QueryAlias</code>. </p>"""
    event_data_store_owner_account_id: NotRequired[
        "capo_cloudtrail.types.account_id.AccountId"
    ]
    """<p> The account ID of the event data store owner. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartQueryRequest) -> dict:
    out: dict = {}
    if "query_statement" in value:
        out["QueryStatement"] = value["query_statement"]
    if "delivery_s3_uri" in value:
        out["DeliveryS3Uri"] = value["delivery_s3_uri"]
    if "query_alias" in value:
        out["QueryAlias"] = value["query_alias"]
    if "query_parameters" in value:
        import capo_cloudtrail.types.query_parameters

        out["QueryParameters"] = (
            capo_cloudtrail.types.query_parameters.serialize_aws_json_1_1(
                value["query_parameters"]
            )
        )
    if "event_data_store_owner_account_id" in value:
        out["EventDataStoreOwnerAccountId"] = value["event_data_store_owner_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartQueryRequest:
    out: StartQueryRequest = {}  # type: ignore[typeddict-item]
    if "QueryStatement" in data:
        out["query_statement"] = data["QueryStatement"]
    if "DeliveryS3Uri" in data:
        out["delivery_s3_uri"] = data["DeliveryS3Uri"]
    if "QueryAlias" in data:
        out["query_alias"] = data["QueryAlias"]
    if "QueryParameters" in data:
        import capo_cloudtrail.types.query_parameters

        out["query_parameters"] = (
            capo_cloudtrail.types.query_parameters.deserialize_aws_json_1_1(
                data["QueryParameters"]
            )
        )
    if "EventDataStoreOwnerAccountId" in data:
        out["event_data_store_owner_account_id"] = data["EventDataStoreOwnerAccountId"]
    return out
