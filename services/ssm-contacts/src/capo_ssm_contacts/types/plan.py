"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Plan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.ssm_contacts_arn_list
    import capo_ssm_contacts.types.stages_list


class Plan(TypedDict, closed=True):
    stages: NotRequired["capo_ssm_contacts.types.stages_list.StagesList"]
    """<p>A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.</p>"""
    rotation_ids: NotRequired[
        "capo_ssm_contacts.types.ssm_contacts_arn_list.SsmContactsArnList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Plan) -> dict:
    out: dict = {}
    if "stages" in value:
        import capo_ssm_contacts.types.stages_list

        out["Stages"] = capo_ssm_contacts.types.stages_list.serialize_aws_json_1_1(
            value["stages"]
        )
    if "rotation_ids" in value:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["RotationIds"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.serialize_aws_json_1_1(
                value["rotation_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Plan:
    out: Plan = {}  # type: ignore[typeddict-item]
    if "Stages" in data:
        import capo_ssm_contacts.types.stages_list

        out["stages"] = capo_ssm_contacts.types.stages_list.deserialize_aws_json_1_1(
            data["Stages"]
        )
    if "RotationIds" in data:
        import capo_ssm_contacts.types.ssm_contacts_arn_list

        out["rotation_ids"] = (
            capo_ssm_contacts.types.ssm_contacts_arn_list.deserialize_aws_json_1_1(
                data["RotationIds"]
            )
        )
    return out
