"""Generated from Smithy shape ``com.amazonaws.kendra#DescribePrincipalMappingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.group_id
    import capo_kendra.types.group_ordering_id_summaries
    import capo_kendra.types.index_id


class DescribePrincipalMappingResponse(TypedDict, closed=True):
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>Shows the identifier of the index to see information on the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>Shows the identifier of the data source to see information on the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""
    group_id: NotRequired["capo_kendra.types.group_id.GroupId"]
    """<p>Shows the identifier of the group to see information on the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups.</p>"""
    group_ordering_id_summaries: NotRequired[
        "capo_kendra.types.group_ordering_id_summaries.GroupOrderingIdSummaries"
    ]
    """<p>Shows the following information on the processing of <code>PUT</code> and <code>DELETE</code> actions for mapping users to their groups:</p> <ul> <li> <p>Status—the status can be either <code>PROCESSING</code>, <code>SUCCEEDED</code>, <code>DELETING</code>, <code>DELETED</code>, or <code>FAILED</code>.</p> </li> <li> <p>Last updated—the last date-time an action was updated.</p> </li> <li> <p>Received—the last date-time an action was received or submitted.</p> </li> <li> <p>Ordering ID—the latest action that should process and apply after other actions.</p> </li> <li> <p>Failure reason—the reason an action could not be processed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePrincipalMappingResponse) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_ordering_id_summaries" in value:
        import capo_kendra.types.group_ordering_id_summaries

        out["GroupOrderingIdSummaries"] = (
            capo_kendra.types.group_ordering_id_summaries.serialize_aws_json_1_1(
                value["group_ordering_id_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePrincipalMappingResponse:
    out: DescribePrincipalMappingResponse = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "GroupOrderingIdSummaries" in data:
        import capo_kendra.types.group_ordering_id_summaries

        out["group_ordering_id_summaries"] = (
            capo_kendra.types.group_ordering_id_summaries.deserialize_aws_json_1_1(
                data["GroupOrderingIdSummaries"]
            )
        )
    return out
