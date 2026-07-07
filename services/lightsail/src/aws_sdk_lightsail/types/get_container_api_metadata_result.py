"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerAPIMetadataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_metadata_entry_list


class GetContainerAPIMetadataResult(TypedDict, closed=True):
    metadata: NotRequired[
        "aws_sdk_lightsail.types.container_service_metadata_entry_list.ContainerServiceMetadataEntryList"
    ]
    """<p>Metadata about Lightsail containers, such as the current version of the Lightsail Control (lightsailctl) plugin.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerAPIMetadataResult) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_lightsail.types.container_service_metadata_entry_list

        out["metadata"] = (
            aws_sdk_lightsail.types.container_service_metadata_entry_list.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerAPIMetadataResult:
    out: GetContainerAPIMetadataResult = {}  # type: ignore[typeddict-item]
    if "metadata" in data:
        import aws_sdk_lightsail.types.container_service_metadata_entry_list

        out["metadata"] = (
            aws_sdk_lightsail.types.container_service_metadata_entry_list.deserialize_aws_json_1_1(
                data["metadata"]
            )
        )
    return out
