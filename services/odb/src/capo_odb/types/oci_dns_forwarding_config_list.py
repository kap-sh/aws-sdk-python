"""Generated from Smithy shape ``com.amazonaws.odb#OciDnsForwardingConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.oci_dns_forwarding_config

OciDnsForwardingConfigList: TypeAlias = list[
    "capo_odb.types.oci_dns_forwarding_config.OciDnsForwardingConfig"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciDnsForwardingConfigList) -> list:
    import capo_odb.types.oci_dns_forwarding_config

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.oci_dns_forwarding_config.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OciDnsForwardingConfigList:
    import capo_odb.types.oci_dns_forwarding_config

    out: OciDnsForwardingConfigList = []
    for item in data:
        out.append(
            capo_odb.types.oci_dns_forwarding_config.deserialize_aws_json_1_0(item)
        )
    return out
