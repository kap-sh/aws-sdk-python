"""Generated from Smithy shape ``com.amazonaws.sagemaker#InfraCheckConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.enable_infra_check


class InfraCheckConfig(TypedDict, closed=True):
    enable_infra_check: NotRequired[
        "capo_sagemaker.types.enable_infra_check.EnableInfraCheck"
    ]
    """<p>Enables an infrastructure health check.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InfraCheckConfig) -> dict:
    out: dict = {}
    if "enable_infra_check" in value:
        out["EnableInfraCheck"] = value["enable_infra_check"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InfraCheckConfig:
    out: InfraCheckConfig = {}  # type: ignore[typeddict-item]
    if "EnableInfraCheck" in data:
        out["enable_infra_check"] = data["EnableInfraCheck"]
    return out
