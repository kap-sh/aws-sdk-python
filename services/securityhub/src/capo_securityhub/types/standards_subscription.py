"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.standards_controls_updatable
    import capo_securityhub.types.standards_input_parameter_map
    import capo_securityhub.types.standards_status
    import capo_securityhub.types.standards_status_reason


class StandardsSubscription(TypedDict, closed=True):
    standards_subscription_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the resource that represents your subscription to the standard.</p>"""
    standards_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the standard.</p>"""
    standards_input: NotRequired[
        "capo_securityhub.types.standards_input_parameter_map.StandardsInputParameterMap"
    ]
    """<p>A key-value pair of input for the standard.</p>"""
    standards_status: NotRequired[
        "capo_securityhub.types.standards_status.StandardsStatus"
    ]
    """<p>The status of your subscription to the standard. Possible values are:</p> <ul> <li> <p> <code>PENDING</code> - The standard is in the process of being enabled. Or the standard is already enabled and Security Hub CSPM is adding new controls to the standard.</p> </li> <li> <p> <code>READY</code> - The standard is enabled.</p> </li> <li> <p> <code>INCOMPLETE</code> - The standard could not be enabled completely. One or more errors (<code>StandardsStatusReason</code>) occurred when Security Hub CSPM attempted to enable the standard.</p> </li> <li> <p> <code>DELETING</code> - The standard is in the process of being disabled.</p> </li> <li> <p> <code>FAILED</code> - The standard could not be disabled. One or more errors (<code>StandardsStatusReason</code>) occurred when Security Hub CSPM attempted to disable the standard.</p> </li> </ul>"""
    standards_controls_updatable: NotRequired[
        "capo_securityhub.types.standards_controls_updatable.StandardsControlsUpdatable"
    ]
    """<p>Specifies whether you can retrieve information about and configure individual controls that apply to the standard. Possible values are:</p> <ul> <li> <p> <code>READY_FOR_UPDATES</code> - Controls in the standard can be retrieved and configured.</p> </li> <li> <p> <code>NOT_READY_FOR_UPDATES</code> - Controls in the standard cannot be retrieved or configured.</p> </li> </ul>"""
    standards_status_reason: NotRequired[
        "capo_securityhub.types.standards_status_reason.StandardsStatusReason"
    ]
    """<p>The reason for the current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscription) -> dict:
    out: dict = {}
    if "standards_subscription_arn" in value:
        out["StandardsSubscriptionArn"] = value["standards_subscription_arn"]
    if "standards_arn" in value:
        out["StandardsArn"] = value["standards_arn"]
    if "standards_input" in value:
        import capo_securityhub.types.standards_input_parameter_map

        out["StandardsInput"] = (
            capo_securityhub.types.standards_input_parameter_map.serialize_json(
                value["standards_input"]
            )
        )
    if "standards_status" in value:
        import capo_securityhub.types.standards_status

        out["StandardsStatus"] = capo_securityhub.types.standards_status.serialize_json(
            value["standards_status"]
        )
    if "standards_controls_updatable" in value:
        import capo_securityhub.types.standards_controls_updatable

        out["StandardsControlsUpdatable"] = (
            capo_securityhub.types.standards_controls_updatable.serialize_json(
                value["standards_controls_updatable"]
            )
        )
    if "standards_status_reason" in value:
        import capo_securityhub.types.standards_status_reason

        out["StandardsStatusReason"] = (
            capo_securityhub.types.standards_status_reason.serialize_json(
                value["standards_status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> StandardsSubscription:
    out: StandardsSubscription = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptionArn" in data:
        out["standards_subscription_arn"] = data["StandardsSubscriptionArn"]
    if "StandardsArn" in data:
        out["standards_arn"] = data["StandardsArn"]
    if "StandardsInput" in data:
        import capo_securityhub.types.standards_input_parameter_map

        out["standards_input"] = (
            capo_securityhub.types.standards_input_parameter_map.deserialize_json(
                data["StandardsInput"]
            )
        )
    if "StandardsStatus" in data:
        import capo_securityhub.types.standards_status

        out["standards_status"] = (
            capo_securityhub.types.standards_status.deserialize_json(
                data["StandardsStatus"]
            )
        )
    if "StandardsControlsUpdatable" in data:
        import capo_securityhub.types.standards_controls_updatable

        out["standards_controls_updatable"] = (
            capo_securityhub.types.standards_controls_updatable.deserialize_json(
                data["StandardsControlsUpdatable"]
            )
        )
    if "StandardsStatusReason" in data:
        import capo_securityhub.types.standards_status_reason

        out["standards_status_reason"] = (
            capo_securityhub.types.standards_status_reason.deserialize_json(
                data["StandardsStatusReason"]
            )
        )
    return out
