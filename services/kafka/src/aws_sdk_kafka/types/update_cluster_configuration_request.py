"""Generated from Smithy shape ``com.amazonaws.kafka#UpdateClusterConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.configuration_info


class UpdateClusterConfigurationRequest(TypedDict, closed=True):
    cluster_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    configuration_info: NotRequired[
        "aws_sdk_kafka.types.configuration_info.ConfigurationInfo"
    ]
    """<p>Represents the configuration that you want MSK to use for the brokers in a cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of the cluster that needs to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateClusterConfigurationRequest) -> dict:
    out: dict = {}
    if "configuration_info" in value:
        import aws_sdk_kafka.types.configuration_info

        out["configurationInfo"] = (
            aws_sdk_kafka.types.configuration_info.serialize_json(
                value["configuration_info"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    return out


def deserialize_json(data: dict) -> UpdateClusterConfigurationRequest:
    out: UpdateClusterConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "configurationInfo" in data:
        import aws_sdk_kafka.types.configuration_info

        out["configuration_info"] = (
            aws_sdk_kafka.types.configuration_info.deserialize_json(
                data["configurationInfo"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    return out
