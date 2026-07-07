"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterNetworkInterfaceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_interface_type


class ClusterNetworkInterfaceDetails(TypedDict, closed=True):
    interface_type: NotRequired[
        "aws_sdk_sagemaker.types.cluster_interface_type.ClusterInterfaceType"
    ]
    """<p>The type of network interface for the instance group. Valid values are <code>efa</code> and <code>efa-only</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNetworkInterfaceDetails) -> dict:
    out: dict = {}
    if "interface_type" in value:
        import aws_sdk_sagemaker.types.cluster_interface_type

        out["InterfaceType"] = (
            aws_sdk_sagemaker.types.cluster_interface_type.serialize_aws_json_1_1(
                value["interface_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNetworkInterfaceDetails:
    out: ClusterNetworkInterfaceDetails = {}  # type: ignore[typeddict-item]
    if "InterfaceType" in data:
        import aws_sdk_sagemaker.types.cluster_interface_type

        out["interface_type"] = (
            aws_sdk_sagemaker.types.cluster_interface_type.deserialize_aws_json_1_1(
                data["InterfaceType"]
            )
        )
    return out
