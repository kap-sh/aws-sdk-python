"""Generated from Smithy shape ``com.amazonaws.emr#CancelStepsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.cancel_steps_info_list


class CancelStepsOutput(TypedDict):
    cancel_steps_info_list: NotRequired[
        "aws_sdk_emr.types.cancel_steps_info_list.CancelStepsInfoList"
    ]
    """<p>A list of <a>CancelStepsInfo</a>, which shows the status of specified cancel requests for each <code>StepID</code> specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelStepsOutput) -> dict:
    out: dict = {}
    if "cancel_steps_info_list" in value:
        import aws_sdk_emr.types.cancel_steps_info_list

        out["CancelStepsInfoList"] = (
            aws_sdk_emr.types.cancel_steps_info_list.serialize_aws_json_1_1(
                value["cancel_steps_info_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelStepsOutput:
    out: CancelStepsOutput = {}  # type: ignore[typeddict-item]
    if "CancelStepsInfoList" in data:
        import aws_sdk_emr.types.cancel_steps_info_list

        out["cancel_steps_info_list"] = (
            aws_sdk_emr.types.cancel_steps_info_list.deserialize_aws_json_1_1(
                data["CancelStepsInfoList"]
            )
        )
    return out
