"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDashboardIndicatorAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean


class ModelDashboardIndicatorAction(TypedDict):
    enabled: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Indicates whether the alert action is turned on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDashboardIndicatorAction) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDashboardIndicatorAction:
    out: ModelDashboardIndicatorAction = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
