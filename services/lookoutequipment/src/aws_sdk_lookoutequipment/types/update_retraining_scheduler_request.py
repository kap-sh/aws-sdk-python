"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateRetrainingSchedulerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.lookback_window
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_promote_mode
    import aws_sdk_lookoutequipment.types.retraining_frequency
    import aws_sdk_lookoutequipment.types.timestamp


class UpdateRetrainingSchedulerRequest(TypedDict):
    model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model whose retraining scheduler you want to update. </p>"""
    retraining_start_date: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>"""
    retraining_frequency: NotRequired[
        "aws_sdk_lookoutequipment.types.retraining_frequency.RetrainingFrequency"
    ]
    r"""<p>This parameter uses the <a href=\"https://en.wikipedia.org/wiki/ISO_8601#Durations\">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>"""
    lookback_window: NotRequired[
        "aws_sdk_lookoutequipment.types.lookback_window.LookbackWindow"
    ]
    """<p>The number of past days of data that will be used for retraining.</p>"""
    promote_mode: NotRequired[
        "aws_sdk_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
    ]
    r"""<p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation\">until they are manually activated</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRetrainingSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    if "retraining_start_date" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["RetrainingStartDate"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["retraining_start_date"]
            )
        )
    if "retraining_frequency" in value:
        out["RetrainingFrequency"] = value["retraining_frequency"]
    if "lookback_window" in value:
        out["LookbackWindow"] = value["lookback_window"]
    if "promote_mode" in value:
        import aws_sdk_lookoutequipment.types.model_promote_mode

        out["PromoteMode"] = (
            aws_sdk_lookoutequipment.types.model_promote_mode.serialize_aws_json_1_0(
                value["promote_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRetrainingSchedulerRequest:
    out: UpdateRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError(
            "UpdateRetrainingSchedulerRequest.model_name required"
        )
    if "RetrainingStartDate" in data:
        import aws_sdk_lookoutequipment.types.timestamp

        out["retraining_start_date"] = (
            aws_sdk_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["RetrainingStartDate"]
            )
        )
    if "RetrainingFrequency" in data:
        out["retraining_frequency"] = data["RetrainingFrequency"]
    if "LookbackWindow" in data:
        out["lookback_window"] = data["LookbackWindow"]
    if "PromoteMode" in data:
        import aws_sdk_lookoutequipment.types.model_promote_mode

        out["promote_mode"] = (
            aws_sdk_lookoutequipment.types.model_promote_mode.deserialize_aws_json_1_0(
                data["PromoteMode"]
            )
        )
    return out
