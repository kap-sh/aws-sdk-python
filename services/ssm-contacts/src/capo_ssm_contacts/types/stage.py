"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Stage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.stage_duration_in_mins
    import capo_ssm_contacts.types.targets_list


class Stage(TypedDict, closed=True):
    duration_in_minutes: (
        "capo_ssm_contacts.types.stage_duration_in_mins.StageDurationInMins"
    )
    """<p>The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.</p>"""
    targets: "capo_ssm_contacts.types.targets_list.TargetsList"
    """<p>The contacts or contact methods that the escalation plan or engagement plan is engaging.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Stage) -> dict:
    out: dict = {}
    out["DurationInMinutes"] = value["duration_in_minutes"]
    import capo_ssm_contacts.types.targets_list

    out["Targets"] = capo_ssm_contacts.types.targets_list.serialize_aws_json_1_1(
        value["targets"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Stage:
    out: Stage = {}  # type: ignore[typeddict-item]
    if "DurationInMinutes" in data:
        out["duration_in_minutes"] = data["DurationInMinutes"]
    else:
        raise DeserializationError("Stage.duration_in_minutes required")
    if "Targets" in data:
        import capo_ssm_contacts.types.targets_list

        out["targets"] = capo_ssm_contacts.types.targets_list.deserialize_aws_json_1_1(
            data["Targets"]
        )
    else:
        raise DeserializationError("Stage.targets required")
    return out
