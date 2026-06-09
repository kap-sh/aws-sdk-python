"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeServiceRevisionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.failures
    import aws_sdk_ecs.types.service_revisions


class DescribeServiceRevisionsResponse(TypedDict):
    service_revisions: NotRequired[
        "aws_sdk_ecs.types.service_revisions.ServiceRevisions"
    ]
    """<p>The list of service revisions described.</p>"""
    failures: NotRequired["aws_sdk_ecs.types.failures.Failures"]
    """<p>Any failures associated with the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceRevisionsResponse) -> dict:
    out: dict = {}
    if "service_revisions" in value:
        import aws_sdk_ecs.types.service_revisions

        out["serviceRevisions"] = (
            aws_sdk_ecs.types.service_revisions.serialize_aws_json_1_1(
                value["service_revisions"]
            )
        )
    if "failures" in value:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.serialize_aws_json_1_1(
            value["failures"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceRevisionsResponse:
    out: DescribeServiceRevisionsResponse = {}  # type: ignore[typeddict-item]
    if "serviceRevisions" in data:
        import aws_sdk_ecs.types.service_revisions

        out["service_revisions"] = (
            aws_sdk_ecs.types.service_revisions.deserialize_aws_json_1_1(
                data["serviceRevisions"]
            )
        )
    if "failures" in data:
        import aws_sdk_ecs.types.failures

        out["failures"] = aws_sdk_ecs.types.failures.deserialize_aws_json_1_1(
            data["failures"]
        )
    return out
