"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CreateRetrainingSchedulerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.idempotence_token
    import aws_sdk_lookoutequipment.types.lookback_window
    import aws_sdk_lookoutequipment.types.model_name
    import aws_sdk_lookoutequipment.types.model_promote_mode
    import aws_sdk_lookoutequipment.types.retraining_frequency
    import aws_sdk_lookoutequipment.types.timestamp


class CreateRetrainingSchedulerRequest(TypedDict):
    model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model to add the retraining scheduler to. </p>"""
    retraining_start_date: NotRequired[
        "aws_sdk_lookoutequipment.types.timestamp.Timestamp"
    ]
    """<p>The start date for the retraining scheduler. Lookout for Equipment truncates the time you provide to the nearest UTC day.</p>"""
    retraining_frequency: (
        "aws_sdk_lookoutequipment.types.retraining_frequency.RetrainingFrequency"
    )
    r"""<p>This parameter uses the <a href=\"https://en.wikipedia.org/wiki/ISO_8601#Durations\">ISO 8601</a> standard to set the frequency at which you want retraining to occur in terms of Years, Months, and/or Days (note: other parameters like Time are not currently supported). The minimum value is 30 days (P30D) and the maximum value is 1 year (P1Y). For example, the following values are valid:</p> <ul> <li> <p>P3M15D – Every 3 months and 15 days</p> </li> <li> <p>P2M – Every 2 months</p> </li> <li> <p>P150D – Every 150 days</p> </li> </ul>"""
    lookback_window: "aws_sdk_lookoutequipment.types.lookback_window.LookbackWindow"
    """<p>The number of past days of data that will be used for retraining.</p>"""
    promote_mode: NotRequired[
        "aws_sdk_lookoutequipment.types.model_promote_mode.ModelPromoteMode"
    ]
    r"""<p>Indicates how the service will use new models. In <code>MANAGED</code> mode, new models will automatically be used for inference if they have better performance than the current model. In <code>MANUAL</code> mode, the new models will not be used <a href=\"https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/versioning-model.html#model-activation\">until they are manually activated</a>.</p>"""
    client_token: "aws_sdk_lookoutequipment.types.idempotence_token.IdempotenceToken"
    """<p>A unique identifier for the request. If you do not set the client request token, Amazon Lookout for Equipment generates one. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRetrainingSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    if "retraining_start_date" in value:
        import aws_sdk_lookoutequipment.types.timestamp

        out["RetrainingStartDate"] = (
            aws_sdk_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["retraining_start_date"]
            )
        )
    out["RetrainingFrequency"] = value["retraining_frequency"]
    out["LookbackWindow"] = value["lookback_window"]
    if "promote_mode" in value:
        import aws_sdk_lookoutequipment.types.model_promote_mode

        out["PromoteMode"] = (
            aws_sdk_lookoutequipment.types.model_promote_mode.serialize_aws_json_1_0(
                value["promote_mode"]
            )
        )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRetrainingSchedulerRequest:
    out: CreateRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError(
            "CreateRetrainingSchedulerRequest.model_name required"
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
    else:
        raise DeserializationError(
            "CreateRetrainingSchedulerRequest.retraining_frequency required"
        )
    if "LookbackWindow" in data:
        out["lookback_window"] = data["LookbackWindow"]
    else:
        raise DeserializationError(
            "CreateRetrainingSchedulerRequest.lookback_window required"
        )
    if "PromoteMode" in data:
        import aws_sdk_lookoutequipment.types.model_promote_mode

        out["promote_mode"] = (
            aws_sdk_lookoutequipment.types.model_promote_mode.deserialize_aws_json_1_0(
                data["PromoteMode"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CreateRetrainingSchedulerRequest.client_token required"
        )
    return out
