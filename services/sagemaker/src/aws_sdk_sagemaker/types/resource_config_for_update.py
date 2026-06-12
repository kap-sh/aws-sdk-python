"""Generated from Smithy shape ``com.amazonaws.sagemaker#ResourceConfigForUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.keep_alive_period_in_seconds


class ResourceConfigForUpdate(TypedDict):
    keep_alive_period_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.keep_alive_period_in_seconds.KeepAlivePeriodInSeconds"
    ]
    """<p>The <code>KeepAlivePeriodInSeconds</code> value specified in the <code>ResourceConfig</code> to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceConfigForUpdate) -> dict:
    out: dict = {}
    if "keep_alive_period_in_seconds" in value:
        out["KeepAlivePeriodInSeconds"] = value["keep_alive_period_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceConfigForUpdate:
    out: ResourceConfigForUpdate = {}  # type: ignore[typeddict-item]
    if "KeepAlivePeriodInSeconds" in data:
        out["keep_alive_period_in_seconds"] = data["KeepAlivePeriodInSeconds"]
    return out
