"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.stage

StagesList: TypeAlias = list["aws_sdk_ssm_contacts.types.stage.Stage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StagesList) -> list:
    import aws_sdk_ssm_contacts.types.stage

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.stage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StagesList:
    import aws_sdk_ssm_contacts.types.stage

    out: StagesList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.stage.deserialize_aws_json_1_1(item))
    return out
