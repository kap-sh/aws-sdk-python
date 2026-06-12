"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteTLSInspectionConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_name


class DeleteTLSInspectionConfigurationRequest(TypedDict):
    tls_inspection_configuration_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the TLS inspection configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    tls_inspection_configuration_name: NotRequired[
        "aws_sdk_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteTLSInspectionConfigurationRequest) -> dict:
    out: dict = {}
    if "tls_inspection_configuration_arn" in value:
        out["TLSInspectionConfigurationArn"] = value["tls_inspection_configuration_arn"]
    if "tls_inspection_configuration_name" in value:
        out["TLSInspectionConfigurationName"] = value[
            "tls_inspection_configuration_name"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteTLSInspectionConfigurationRequest:
    out: DeleteTLSInspectionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TLSInspectionConfigurationArn" in data:
        out["tls_inspection_configuration_arn"] = data["TLSInspectionConfigurationArn"]
    if "TLSInspectionConfigurationName" in data:
        out["tls_inspection_configuration_name"] = data[
            "TLSInspectionConfigurationName"
        ]
    return out
