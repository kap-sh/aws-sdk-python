"""Generated from Smithy shape ``com.amazonaws.forecast#UpdateDatasetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.arn_list


class UpdateDatasetGroupRequest(TypedDict, closed=True):
    dataset_group_arn: "capo_forecast.types.arn.Arn"
    """<p>The ARN of the dataset group.</p>"""
    dataset_arns: "capo_forecast.types.arn_list.ArnList"
    """<p>An array of the Amazon Resource Names (ARNs) of the datasets to add to the dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDatasetGroupRequest) -> dict:
    out: dict = {}
    out["DatasetGroupArn"] = value["dataset_group_arn"]
    import capo_forecast.types.arn_list

    out["DatasetArns"] = capo_forecast.types.arn_list.serialize_aws_json_1_1(
        value["dataset_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDatasetGroupRequest:
    out: UpdateDatasetGroupRequest = {}  # type: ignore[typeddict-item]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    else:
        raise DeserializationError(
            "UpdateDatasetGroupRequest.dataset_group_arn required"
        )
    if "DatasetArns" in data:
        import capo_forecast.types.arn_list

        out["dataset_arns"] = capo_forecast.types.arn_list.deserialize_aws_json_1_1(
            data["DatasetArns"]
        )
    else:
        raise DeserializationError("UpdateDatasetGroupRequest.dataset_arns required")
    return out
