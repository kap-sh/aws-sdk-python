"""Generated from Smithy shape ``com.amazonaws.lightsail#GetStaticIpResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.static_ip


class GetStaticIpResult(TypedDict, closed=True):
    static_ip: NotRequired["aws_sdk_lightsail.types.static_ip.StaticIp"]
    """<p>An array of key-value pairs containing information about the requested static IP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStaticIpResult) -> dict:
    out: dict = {}
    if "static_ip" in value:
        import aws_sdk_lightsail.types.static_ip

        out["staticIp"] = aws_sdk_lightsail.types.static_ip.serialize_aws_json_1_1(
            value["static_ip"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStaticIpResult:
    out: GetStaticIpResult = {}  # type: ignore[typeddict-item]
    if "staticIp" in data:
        import aws_sdk_lightsail.types.static_ip

        out["static_ip"] = aws_sdk_lightsail.types.static_ip.deserialize_aws_json_1_1(
            data["staticIp"]
        )
    return out
