"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceMetadataServiceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.minimum_instance_metadata_service_version


class InstanceMetadataServiceConfiguration(TypedDict):
    minimum_instance_metadata_service_version: NotRequired[
        "aws_sdk_sagemaker.types.minimum_instance_metadata_service_version.MinimumInstanceMetadataServiceVersion"
    ]
    """<p>Indicates the minimum IMDS version that the notebook instance supports. When passed as part of <code>CreateNotebookInstance</code>, if no value is selected, then it defaults to IMDSv1. This means that both IMDSv1 and IMDSv2 are supported. If passed as part of <code>UpdateNotebookInstance</code>, there is no default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceMetadataServiceConfiguration) -> dict:
    out: dict = {}
    if "minimum_instance_metadata_service_version" in value:
        out["MinimumInstanceMetadataServiceVersion"] = value[
            "minimum_instance_metadata_service_version"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceMetadataServiceConfiguration:
    out: InstanceMetadataServiceConfiguration = {}  # type: ignore[typeddict-item]
    if "MinimumInstanceMetadataServiceVersion" in data:
        out["minimum_instance_metadata_service_version"] = data[
            "MinimumInstanceMetadataServiceVersion"
        ]
    return out
