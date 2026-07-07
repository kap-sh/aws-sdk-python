"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRevisionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_revisions
    import aws_sdk_ecs.types.failures


class DescribeDaemonRevisionsResponse(TypedDict, closed=True):
    daemon_revisions: NotRequired["aws_sdk_ecs.types.daemon_revisions.DaemonRevisions"]
    """<p>The list of daemon revisions.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonRevisionsResponse) -> dict:
    out: dict = {}
    if "daemon_revisions" in value:
        import aws_sdk_ecs.types.daemon_revisions

        out["daemonRevisions"] = (
            aws_sdk_ecs.types.daemon_revisions.serialize_aws_json_1_1(
                value["daemon_revisions"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonRevisionsResponse:
    out: DescribeDaemonRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "daemonRevisions" in data:
        import aws_sdk_ecs.types.daemon_revisions

        out["daemon_revisions"] = (
            aws_sdk_ecs.types.daemon_revisions.deserialize_aws_json_1_1(
                data["daemonRevisions"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
