"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoRollbackConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.alarm_list


class AutoRollbackConfig(TypedDict, closed=True):
    alarms: NotRequired["aws_sdk_sagemaker.types.alarm_list.AlarmList"]
    """<p>List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRollbackConfig) -> dict:
    out: dict = {}
    if "alarms" in value:
        import aws_sdk_sagemaker.types.alarm_list

        out["Alarms"] = aws_sdk_sagemaker.types.alarm_list.serialize_aws_json_1_1(
            value["alarms"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoRollbackConfig:
    out: AutoRollbackConfig = {}  # type: ignore[typeddict-item]
    if "Alarms" in data:
        import aws_sdk_sagemaker.types.alarm_list

        out["alarms"] = aws_sdk_sagemaker.types.alarm_list.deserialize_aws_json_1_1(
            data["Alarms"]
        )
    return out
