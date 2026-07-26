"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_arn


class UpdateHubResponse(TypedDict, closed=True):
    hub_arn: NotRequired["capo_sagemaker.types.hub_arn.HubArn"]
    """<p>The Amazon Resource Name (ARN) of the updated hub.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHubResponse) -> dict:
    out: dict = {}
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHubResponse:
    out: UpdateHubResponse = {}  # type: ignore[typeddict-item]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    return out
