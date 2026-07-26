"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails(
    TypedDict, closed=True
):
    minimum_instance_metadata_service_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Indicates the minimum IMDS version that the notebook instance supports. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails,
) -> dict:
    out: dict = {}
    if "minimum_instance_metadata_service_version" in value:
        out["MinimumInstanceMetadataServiceVersion"] = value[
            "minimum_instance_metadata_service_version"
        ]
    return out


def deserialize_json(
    data: dict,
) -> AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails:
    out: AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "MinimumInstanceMetadataServiceVersion" in data:
        out["minimum_instance_metadata_service_version"] = data[
            "MinimumInstanceMetadataServiceVersion"
        ]
    return out
