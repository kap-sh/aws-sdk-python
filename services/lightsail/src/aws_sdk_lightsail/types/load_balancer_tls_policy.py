"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string
    import aws_sdk_lightsail.types.string_list


class LoadBalancerTlsPolicy(TypedDict):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the TLS security policy.</p>"""
    is_default: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether the TLS security policy is the default.</p>"""
    description: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The description of the TLS security policy.</p>"""
    protocols: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>The protocols used in a given TLS security policy.</p>"""
    ciphers: NotRequired["aws_sdk_lightsail.types.string_list.StringList"]
    """<p>The ciphers used by the TLS security policy.</p> <p>The ciphers are listed in order of preference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsPolicy) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "is_default" in value:
        out["isDefault"] = value["is_default"]
    if "description" in value:
        out["description"] = value["description"]
    if "protocols" in value:
        import aws_sdk_lightsail.types.string_list

        out["protocols"] = aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
            value["protocols"]
        )
    if "ciphers" in value:
        import aws_sdk_lightsail.types.string_list

        out["ciphers"] = aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
            value["ciphers"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerTlsPolicy:
    out: LoadBalancerTlsPolicy = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "isDefault" in data:
        out["is_default"] = data["isDefault"]
    if "description" in data:
        out["description"] = data["description"]
    if "protocols" in data:
        import aws_sdk_lightsail.types.string_list

        out["protocols"] = aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["protocols"]
        )
    if "ciphers" in data:
        import aws_sdk_lightsail.types.string_list

        out["ciphers"] = aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["ciphers"]
        )
    return out
