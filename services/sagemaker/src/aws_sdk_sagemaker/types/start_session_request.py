"""Generated from Smithy shape ``com.amazonaws.sagemaker#StartSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_identifier


class StartSessionRequest(TypedDict):
    resource_identifier: NotRequired[
        "aws_sdk_sagemaker.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource to which the remote connection will be established. For example, this identifies the specific ARN space application you want to connect to from your local IDE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionRequest) -> dict:
    out: dict = {}
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionRequest:
    out: StartSessionRequest = {}  # type: ignore[typeddict-item]
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    return out
