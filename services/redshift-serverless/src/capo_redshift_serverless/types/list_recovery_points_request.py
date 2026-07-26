"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListRecoveryPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.namespace_name


class ListRecoveryPointsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListRecoveryPoints</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in following <code>ListRecoveryPoints</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to display the next page of results.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The time when the recovery point's creation was initiated.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time when creation of the recovery point finished.</p>"""
    namespace_name: NotRequired[
        "capo_redshift_serverless.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace to list recovery points for.</p>"""
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the namespace from which to list recovery points.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRecoveryPointsRequest) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["startTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_redshift_serverless.types._prelude.timestamp

        out["endTime"] = (
            capo_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRecoveryPointsRequest:
    out: ListRecoveryPointsRequest = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_redshift_serverless.types._prelude.timestamp

        out["start_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_redshift_serverless.types._prelude.timestamp

        out["end_time"] = (
            capo_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["endTime"]
            )
        )
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    return out
