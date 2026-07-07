"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ListSnapshotsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""
    namespace_name: NotRequired["str"]
    """<p>The namespace from which to list all snapshots.</p>"""
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the namespace from which to list all snapshots.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services account of the snapshot.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The time when the creation of the snapshot was initiated.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp showing when the snapshot creation finished.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSnapshotsRequest) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "start_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["startTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["endTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSnapshotsRequest:
    out: ListSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "startTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["start_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["end_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    return out
