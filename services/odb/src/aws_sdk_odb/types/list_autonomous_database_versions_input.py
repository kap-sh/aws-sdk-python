"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabaseVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.db_workload


class ListAutonomousDatabaseVersionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    db_workload: NotRequired["aws_sdk_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database to return versions for, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabaseVersionsInput) -> dict:
    out: dict = {}
    if "db_workload" in value:
        import aws_sdk_odb.types.db_workload

        out["dbWorkload"] = aws_sdk_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabaseVersionsInput:
    out: ListAutonomousDatabaseVersionsInput = {}  # type: ignore[typeddict-item]
    if "dbWorkload" in data:
        import aws_sdk_odb.types.db_workload

        out["db_workload"] = aws_sdk_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    return out
