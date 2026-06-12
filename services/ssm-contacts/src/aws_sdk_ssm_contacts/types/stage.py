"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Stage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.stage_duration_in_mins
    import aws_sdk_ssm_contacts.types.targets_list


class Stage(TypedDict):
    duration_in_minutes: (
        "aws_sdk_ssm_contacts.types.stage_duration_in_mins.StageDurationInMins"
    )
    """<p>The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.</p>"""
    targets: "aws_sdk_ssm_contacts.types.targets_list.TargetsList"
    """<p>The contacts or contact methods that the escalation plan or engagement plan is engaging.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Stage) -> dict:
    out: dict = {}
    out["DurationInMinutes"] = value["duration_in_minutes"]
    import aws_sdk_ssm_contacts.types.targets_list

    out["Targets"] = aws_sdk_ssm_contacts.types.targets_list.serialize_aws_json_1_1(
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
        import aws_sdk_ssm_contacts.types.targets_list

        out["targets"] = (
            aws_sdk_ssm_contacts.types.targets_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        raise DeserializationError("Stage.targets required")
    return out
