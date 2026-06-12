"""Generated from Smithy shape ``com.amazonaws.fms#PossibleRemediationActions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.possible_remediation_action_list


class PossibleRemediationActions(TypedDict):
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the possible remediation actions list.</p>"""
    actions: NotRequired[
        "aws_sdk_fms.types.possible_remediation_action_list.PossibleRemediationActionList"
    ]
    """<p>Information about the actions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PossibleRemediationActions) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "actions" in value:
        import aws_sdk_fms.types.possible_remediation_action_list

        out["Actions"] = (
            aws_sdk_fms.types.possible_remediation_action_list.serialize_aws_json_1_1(
                value["actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PossibleRemediationActions:
    out: PossibleRemediationActions = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Actions" in data:
        import aws_sdk_fms.types.possible_remediation_action_list

        out["actions"] = (
            aws_sdk_fms.types.possible_remediation_action_list.deserialize_aws_json_1_1(
                data["Actions"]
            )
        )
    return out
