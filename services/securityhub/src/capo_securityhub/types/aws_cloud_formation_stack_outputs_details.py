"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFormationStackOutputsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCloudFormationStackOutputsDetails(TypedDict, closed=True):
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A user-defined description associated with the output. </p>"""
    output_key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The key associated with the output. </p>"""
    output_value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value associated with the output. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFormationStackOutputsDetails) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "output_key" in value:
        out["OutputKey"] = value["output_key"]
    if "output_value" in value:
        out["OutputValue"] = value["output_value"]
    return out


def deserialize_json(data: dict) -> AwsCloudFormationStackOutputsDetails:
    out: AwsCloudFormationStackOutputsDetails = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "OutputKey" in data:
        out["output_key"] = data["OutputKey"]
    if "OutputValue" in data:
        out["output_value"] = data["OutputValue"]
    return out
