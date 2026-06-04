"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeDaemonRevisionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class DescribeDaemonRevisionsRequest(TypedDict):
    daemon_revision_arns: "aws_sdk_ecs.types.string_list.StringList"
    """<p>The ARN of the daemon revisions to describe. You can specify up to 20 ARNs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDaemonRevisionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.string_list

    out["daemonRevisionArns"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
        value["daemon_revision_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDaemonRevisionsRequest:
    out: DescribeDaemonRevisionsRequest = {}  # type: ignore[typeddict-item]
    if "daemonRevisionArns" in data:
        import aws_sdk_ecs.types.string_list

        out["daemon_revision_arns"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["daemonRevisionArns"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDaemonRevisionsRequest.daemon_revision_arns required"
        )
    return out
