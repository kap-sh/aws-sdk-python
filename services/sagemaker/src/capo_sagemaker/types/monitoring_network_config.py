"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringNetworkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.boolean
    import capo_sagemaker.types.vpc_config


class MonitoringNetworkConfig(TypedDict, closed=True):
    enable_inter_container_traffic_encryption: NotRequired[
        "capo_sagemaker.types.boolean.Boolean"
    ]
    """<p>Whether to encrypt all communications between the instances used for the monitoring jobs. Choose <code>True</code> to encrypt communications. Encryption provides greater security for distributed jobs, but the processing might take longer.</p>"""
    enable_network_isolation: NotRequired["capo_sagemaker.types.boolean.Boolean"]
    """<p>Whether to allow inbound and outbound network calls to and from the containers used for the monitoring job.</p>"""
    vpc_config: NotRequired["capo_sagemaker.types.vpc_config.VpcConfig"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringNetworkConfig) -> dict:
    out: dict = {}
    if "enable_inter_container_traffic_encryption" in value:
        out["EnableInterContainerTrafficEncryption"] = value[
            "enable_inter_container_traffic_encryption"
        ]
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "vpc_config" in value:
        import capo_sagemaker.types.vpc_config

        out["VpcConfig"] = capo_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringNetworkConfig:
    out: MonitoringNetworkConfig = {}  # type: ignore[typeddict-item]
    if "EnableInterContainerTrafficEncryption" in data:
        out["enable_inter_container_traffic_encryption"] = data[
            "EnableInterContainerTrafficEncryption"
        ]
    if "EnableNetworkIsolation" in data:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if "VpcConfig" in data:
        import capo_sagemaker.types.vpc_config

        out["vpc_config"] = capo_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    return out
