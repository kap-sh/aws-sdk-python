"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelsInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.label_group_name
    import aws_sdk_lookoutequipment.types.labels_s3_input_configuration


class LabelsInputConfiguration(TypedDict, closed=True):
    s3_input_configuration: NotRequired[
        "aws_sdk_lookoutequipment.types.labels_s3_input_configuration.LabelsS3InputConfiguration"
    ]
    """<p>Contains location information for the S3 location being used for label data. </p>"""
    label_group_name: NotRequired[
        "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    ]
    """<p> The name of the label group to be used for label data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelsInputConfiguration) -> dict:
    out: dict = {}
    if "s3_input_configuration" in value:
        import aws_sdk_lookoutequipment.types.labels_s3_input_configuration

        out["S3InputConfiguration"] = (
            aws_sdk_lookoutequipment.types.labels_s3_input_configuration.serialize_aws_json_1_0(
                value["s3_input_configuration"]
            )
        )
    if "label_group_name" in value:
        out["LabelGroupName"] = value["label_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LabelsInputConfiguration:
    out: LabelsInputConfiguration = {}  # type: ignore[typeddict-item]
    if "S3InputConfiguration" in data:
        import aws_sdk_lookoutequipment.types.labels_s3_input_configuration

        out["s3_input_configuration"] = (
            aws_sdk_lookoutequipment.types.labels_s3_input_configuration.deserialize_aws_json_1_0(
                data["S3InputConfiguration"]
            )
        )
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    return out
