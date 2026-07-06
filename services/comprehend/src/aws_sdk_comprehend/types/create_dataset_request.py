"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.client_request_token_string
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.dataset_input_data_config
    import aws_sdk_comprehend.types.dataset_type
    import aws_sdk_comprehend.types.description
    import aws_sdk_comprehend.types.tag_list


class CreateDatasetRequest(TypedDict, closed=True):
    flywheel_arn: (
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    )
    """<p>The Amazon Resource Number (ARN) of the flywheel of the flywheel to receive the data.</p>"""
    dataset_name: "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    """<p>Name of the dataset.</p>"""
    dataset_type: NotRequired["aws_sdk_comprehend.types.dataset_type.DatasetType"]
    """<p>The dataset type. You can specify that the data in a dataset is for training the model or for testing the model.</p>"""
    description: NotRequired["aws_sdk_comprehend.types.description.Description"]
    """<p>Description of the dataset.</p>"""
    input_data_config: (
        "aws_sdk_comprehend.types.dataset_input_data_config.DatasetInputDataConfig"
    )
    """<p>Information about the input data configuration. The type of input data varies based on the format of the input and whether the data is for a classifier model or an entity recognition model.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_comprehend.types.client_request_token_string.ClientRequestTokenString"
    ]
    """<p>A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.</p>"""
    tags: NotRequired["aws_sdk_comprehend.types.tag_list.TagList"]
    """<p>Tags for the dataset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    out["FlywheelArn"] = value["flywheel_arn"]
    out["DatasetName"] = value["dataset_name"]
    if "dataset_type" in value:
        import aws_sdk_comprehend.types.dataset_type

        out["DatasetType"] = (
            aws_sdk_comprehend.types.dataset_type.serialize_aws_json_1_1(
                value["dataset_type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_comprehend.types.dataset_input_data_config

    out["InputDataConfig"] = (
        aws_sdk_comprehend.types.dataset_input_data_config.serialize_aws_json_1_1(
            value["input_data_config"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_comprehend.types.tag_list

        out["Tags"] = aws_sdk_comprehend.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    else:
        raise DeserializationError("CreateDatasetRequest.flywheel_arn required")
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if "DatasetType" in data:
        import aws_sdk_comprehend.types.dataset_type

        out["dataset_type"] = (
            aws_sdk_comprehend.types.dataset_type.deserialize_aws_json_1_1(
                data["DatasetType"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "InputDataConfig" in data:
        import aws_sdk_comprehend.types.dataset_input_data_config

        out["input_data_config"] = (
            aws_sdk_comprehend.types.dataset_input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetRequest.input_data_config required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_comprehend.types.tag_list

        out["tags"] = aws_sdk_comprehend.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
