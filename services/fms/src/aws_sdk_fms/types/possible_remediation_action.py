"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fms.types.boolean
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.ordered_remediation_actions


class PossibleRemediationAction(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the list of remediation actions.</p>"""
    ordered_remediation_actions: (
        "aws_sdk_fms.types.ordered_remediation_actions.OrderedRemediationActions"
    )
    """<p>The ordered list of remediation actions.</p>"""
    is_default_action: "aws_sdk_fms.types.boolean.Boolean"
    """<p>Information about whether an action is taken by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_fms.types.ordered_remediation_actions

    out["OrderedRemediationActions"] = (
        aws_sdk_fms.types.ordered_remediation_actions.serialize_aws_json_1_1(
            value["ordered_remediation_actions"]
        )
    )
    out["IsDefaultAction"] = value.get("is_default_action", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PossibleRemediationAction:
    out: PossibleRemediationAction = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "OrderedRemediationActions" in data:
        import aws_sdk_fms.types.ordered_remediation_actions

        out["ordered_remediation_actions"] = (
            aws_sdk_fms.types.ordered_remediation_actions.deserialize_aws_json_1_1(
                data["OrderedRemediationActions"]
            )
        )
    else:
        raise DeserializationError(
            "PossibleRemediationAction.ordered_remediation_actions required"
        )
    if "IsDefaultAction" in data:
        out["is_default_action"] = data["IsDefaultAction"]
    else:
        out["is_default_action"] = False
    return out
