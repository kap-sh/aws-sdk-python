"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitContainerStateChangeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class SubmitContainerStateChangeResponse(TypedDict):
    acknowledgment: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Acknowledgement of the state change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitContainerStateChangeResponse) -> dict:
    out: dict = {}
    if "acknowledgment" in value:
        out["acknowledgment"] = value["acknowledgment"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitContainerStateChangeResponse:
    out: SubmitContainerStateChangeResponse = {}  # type: ignore[typeddict-item]
    if "acknowledgment" in data:
        out["acknowledgment"] = data["acknowledgment"]
    return out
