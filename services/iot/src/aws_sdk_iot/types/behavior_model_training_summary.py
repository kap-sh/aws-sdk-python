"""Generated from Smithy shape ``com.amazonaws.iot#BehaviorModelTrainingSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_name
    import aws_sdk_iot.types.data_collection_percentage
    import aws_sdk_iot.types.model_status
    import aws_sdk_iot.types.security_profile_name
    import aws_sdk_iot.types.timestamp


class BehaviorModelTrainingSummary(TypedDict):
    security_profile_name: NotRequired[
        "aws_sdk_iot.types.security_profile_name.SecurityProfileName"
    ]
    """<p> The name of the security profile. </p>"""
    behavior_name: NotRequired["aws_sdk_iot.types.behavior_name.BehaviorName"]
    """<p> The name of the behavior. </p>"""
    training_data_collection_start_date: NotRequired[
        "aws_sdk_iot.types.timestamp.Timestamp"
    ]
    """<p> The date a training model started collecting data. </p>"""
    model_status: NotRequired["aws_sdk_iot.types.model_status.ModelStatus"]
    """<p> The status of the behavior model. </p>"""
    datapoints_collection_percentage: NotRequired[
        "aws_sdk_iot.types.data_collection_percentage.DataCollectionPercentage"
    ]
    """<p> The percentage of datapoints collected. </p>"""
    last_model_refresh_date: NotRequired["aws_sdk_iot.types.timestamp.Timestamp"]
    """<p> The date the model was last refreshed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorModelTrainingSummary) -> dict:
    out: dict = {}
    if "security_profile_name" in value:
        out["securityProfileName"] = value["security_profile_name"]
    if "behavior_name" in value:
        out["behaviorName"] = value["behavior_name"]
    if "training_data_collection_start_date" in value:
        import aws_sdk_iot.types.timestamp

        out["trainingDataCollectionStartDate"] = (
            aws_sdk_iot.types.timestamp.serialize_json(
                value["training_data_collection_start_date"]
            )
        )
    if "model_status" in value:
        import aws_sdk_iot.types.model_status

        out["modelStatus"] = aws_sdk_iot.types.model_status.serialize_json(
            value["model_status"]
        )
    if "datapoints_collection_percentage" in value:
        out["datapointsCollectionPercentage"] = value[
            "datapoints_collection_percentage"
        ]
    if "last_model_refresh_date" in value:
        import aws_sdk_iot.types.timestamp

        out["lastModelRefreshDate"] = aws_sdk_iot.types.timestamp.serialize_json(
            value["last_model_refresh_date"]
        )
    return out


def deserialize_json(data: dict) -> BehaviorModelTrainingSummary:
    out: BehaviorModelTrainingSummary = {}  # type: ignore[typeddict-item]
    if "securityProfileName" in data:
        out["security_profile_name"] = data["securityProfileName"]
    if "behaviorName" in data:
        out["behavior_name"] = data["behaviorName"]
    if "trainingDataCollectionStartDate" in data:
        import aws_sdk_iot.types.timestamp

        out["training_data_collection_start_date"] = (
            aws_sdk_iot.types.timestamp.deserialize_json(
                data["trainingDataCollectionStartDate"]
            )
        )
    if "modelStatus" in data:
        import aws_sdk_iot.types.model_status

        out["model_status"] = aws_sdk_iot.types.model_status.deserialize_json(
            data["modelStatus"]
        )
    if "datapointsCollectionPercentage" in data:
        out["datapoints_collection_percentage"] = data["datapointsCollectionPercentage"]
    if "lastModelRefreshDate" in data:
        import aws_sdk_iot.types.timestamp

        out["last_model_refresh_date"] = aws_sdk_iot.types.timestamp.deserialize_json(
            data["lastModelRefreshDate"]
        )
    return out
