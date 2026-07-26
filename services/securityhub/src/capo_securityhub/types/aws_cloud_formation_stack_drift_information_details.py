"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFormationStackDriftInformationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsCloudFormationStackDriftInformationDetails(TypedDict, closed=True):
    stack_drift_status: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Status of the stack's actual configuration compared to its expected template configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFormationStackDriftInformationDetails) -> dict:
    out: dict = {}
    if "stack_drift_status" in value:
        out["StackDriftStatus"] = value["stack_drift_status"]
    return out


def deserialize_json(data: dict) -> AwsCloudFormationStackDriftInformationDetails:
    out: AwsCloudFormationStackDriftInformationDetails = {}  # type: ignore[typeddict-item]
    if "StackDriftStatus" in data:
        out["stack_drift_status"] = data["StackDriftStatus"]
    return out
