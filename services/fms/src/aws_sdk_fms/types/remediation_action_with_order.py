"""Generated from Smithy shape ``com.amazonaws.fms#RemediationActionWithOrder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.basic_integer
    import aws_sdk_fms.types.remediation_action


class RemediationActionWithOrder(TypedDict):
    remediation_action: NotRequired[
        "aws_sdk_fms.types.remediation_action.RemediationAction"
    ]
    """<p>Information about an action you can take to remediate a violation.</p>"""
    order: "aws_sdk_fms.types.basic_integer.BasicInteger"
    """<p>The order of the remediation actions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationActionWithOrder) -> dict:
    out: dict = {}
    if "remediation_action" in value:
        import aws_sdk_fms.types.remediation_action

        out["RemediationAction"] = (
            aws_sdk_fms.types.remediation_action.serialize_aws_json_1_1(
                value["remediation_action"]
            )
        )
    out["Order"] = value.get("order", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationActionWithOrder:
    out: RemediationActionWithOrder = {}  # type: ignore[typeddict-item]
    if "RemediationAction" in data:
        import aws_sdk_fms.types.remediation_action

        out["remediation_action"] = (
            aws_sdk_fms.types.remediation_action.deserialize_aws_json_1_1(
                data["RemediationAction"]
            )
        )
    if "Order" in data:
        out["order"] = data["Order"]
    else:
        out["order"] = 0
    return out
