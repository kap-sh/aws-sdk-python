"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#DeleteResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.progress_event


class DeleteResourceOutput(TypedDict):
    progress_event: NotRequired[
        "aws_sdk_cloudcontrol.types.progress_event.ProgressEvent"
    ]
    """<p>Represents the current status of the resource deletion request.</p> <p>After you have initiated a resource deletion request, you can monitor the progress of your request by calling <a href=\"https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html\">GetResourceRequestStatus</a> using the <code>RequestToken</code> of the <code>ProgressEvent</code> returned by <code>DeleteResource</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteResourceOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import aws_sdk_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            aws_sdk_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteResourceOutput:
    out: DeleteResourceOutput = {}  # type: ignore[typeddict-item]
    if "ProgressEvent" in data:
        import aws_sdk_cloudcontrol.types.progress_event

        out["progress_event"] = (
            aws_sdk_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    return out
