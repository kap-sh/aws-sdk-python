"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdleSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.idle_timeout_in_minutes
    import capo_sagemaker.types.lifecycle_management


class IdleSettings(TypedDict, closed=True):
    lifecycle_management: NotRequired[
        "capo_sagemaker.types.lifecycle_management.LifecycleManagement"
    ]
    """<p>Indicates whether idle shutdown is activated for the application type.</p>"""
    idle_timeout_in_minutes: NotRequired[
        "capo_sagemaker.types.idle_timeout_in_minutes.IdleTimeoutInMinutes"
    ]
    """<p>The time that SageMaker waits after the application becomes idle before shutting it down.</p>"""
    min_idle_timeout_in_minutes: NotRequired[
        "capo_sagemaker.types.idle_timeout_in_minutes.IdleTimeoutInMinutes"
    ]
    """<p>The minimum value in minutes that custom idle shutdown can be set to by the user.</p>"""
    max_idle_timeout_in_minutes: NotRequired[
        "capo_sagemaker.types.idle_timeout_in_minutes.IdleTimeoutInMinutes"
    ]
    """<p>The maximum value in minutes that custom idle shutdown can be set to by the user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdleSettings) -> dict:
    out: dict = {}
    if "lifecycle_management" in value:
        import capo_sagemaker.types.lifecycle_management

        out["LifecycleManagement"] = (
            capo_sagemaker.types.lifecycle_management.serialize_aws_json_1_1(
                value["lifecycle_management"]
            )
        )
    if "idle_timeout_in_minutes" in value:
        out["IdleTimeoutInMinutes"] = value["idle_timeout_in_minutes"]
    if "min_idle_timeout_in_minutes" in value:
        out["MinIdleTimeoutInMinutes"] = value["min_idle_timeout_in_minutes"]
    if "max_idle_timeout_in_minutes" in value:
        out["MaxIdleTimeoutInMinutes"] = value["max_idle_timeout_in_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdleSettings:
    out: IdleSettings = {}  # type: ignore[typeddict-item]
    if "LifecycleManagement" in data:
        import capo_sagemaker.types.lifecycle_management

        out["lifecycle_management"] = (
            capo_sagemaker.types.lifecycle_management.deserialize_aws_json_1_1(
                data["LifecycleManagement"]
            )
        )
    if "IdleTimeoutInMinutes" in data:
        out["idle_timeout_in_minutes"] = data["IdleTimeoutInMinutes"]
    if "MinIdleTimeoutInMinutes" in data:
        out["min_idle_timeout_in_minutes"] = data["MinIdleTimeoutInMinutes"]
    if "MaxIdleTimeoutInMinutes" in data:
        out["max_idle_timeout_in_minutes"] = data["MaxIdleTimeoutInMinutes"]
    return out
