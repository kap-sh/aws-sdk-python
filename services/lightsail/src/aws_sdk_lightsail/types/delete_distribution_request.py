"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDistributionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DeleteDistributionRequest(TypedDict):
    distribution_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution to delete.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDistributionRequest) -> dict:
    out: dict = {}
    if "distribution_name" in value:
        out["distributionName"] = value["distribution_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDistributionRequest:
    out: DeleteDistributionRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    return out
