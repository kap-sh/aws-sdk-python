"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#BillingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.billing_mode


class BillingConfiguration(TypedDict):
    billing_mode: "aws_sdk_workspaces_instances.types.billing_mode.BillingMode"
    """<p>Specifies the billing mode for WorkSpace Instances. MONTHLY provides fixed monthly rates for predictable budgeting, while HOURLY enables pay-per-second billing for actual usage.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_instances.types.billing_mode

    out["BillingMode"] = (
        aws_sdk_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingConfiguration:
    out: BillingConfiguration = {}  # type: ignore[typeddict-item]
    if "BillingMode" in data:
        import aws_sdk_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    else:
        raise DeserializationError("BillingConfiguration.billing_mode required")
    return out
