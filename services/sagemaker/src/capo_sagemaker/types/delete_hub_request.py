"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteHubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_name_or_arn


class DeleteHubRequest(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHubRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHubRequest:
    out: DeleteHubRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    return out
