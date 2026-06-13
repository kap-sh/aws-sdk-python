"""Generated from Smithy shape ``com.amazonaws.mailmanager#PublicNetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.ip_type


class PublicNetworkConfiguration(TypedDict):
    ip_type: "aws_sdk_mailmanager.types.ip_type.IpType"
    """<p>The IP address type for the public ingress point. Valid values are IPV4 and DUAL_STACK.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PublicNetworkConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.ip_type

    out["IpType"] = aws_sdk_mailmanager.types.ip_type.serialize_aws_json_1_0(
        value.get("ip_type", "IPV4")
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PublicNetworkConfiguration:
    out: PublicNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "IpType" in data:
        import aws_sdk_mailmanager.types.ip_type

        out["ip_type"] = aws_sdk_mailmanager.types.ip_type.deserialize_aws_json_1_0(
            data["IpType"]
        )
    else:
        out["ip_type"] = "IPV4"
    return out
