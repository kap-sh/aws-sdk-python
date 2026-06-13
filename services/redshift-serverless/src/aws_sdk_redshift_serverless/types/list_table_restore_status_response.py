"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListTableRestoreStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.table_restore_status_list


class ListTableRestoreStatusResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>If your initial <code>ListTableRestoreStatus</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListTableRestoreStatus</code> operations. This will returns results on the next page.</p>"""
    table_restore_statuses: NotRequired[
        "aws_sdk_redshift_serverless.types.table_restore_status_list.TableRestoreStatusList"
    ]
    """<p>The array of returned <code>TableRestoreStatus</code> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTableRestoreStatusResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "table_restore_statuses" in value:
        import aws_sdk_redshift_serverless.types.table_restore_status_list

        out["tableRestoreStatuses"] = (
            aws_sdk_redshift_serverless.types.table_restore_status_list.serialize_aws_json_1_1(
                value["table_restore_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTableRestoreStatusResponse:
    out: ListTableRestoreStatusResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "tableRestoreStatuses" in data:
        import aws_sdk_redshift_serverless.types.table_restore_status_list

        out["table_restore_statuses"] = (
            aws_sdk_redshift_serverless.types.table_restore_status_list.deserialize_aws_json_1_1(
                data["tableRestoreStatuses"]
            )
        )
    return out
