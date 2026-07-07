"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateServiceNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_type
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.service_network_name
    import aws_sdk_vpc_lattice.types.sharing_config
    import aws_sdk_vpc_lattice.types.tag_map


class CreateServiceNetworkRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    name: "aws_sdk_vpc_lattice.types.service_network_name.ServiceNetworkName"
    """<p>The name of the service network. The name must be unique to the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    auth_type: NotRequired["aws_sdk_vpc_lattice.types.auth_type.AuthType"]
    """<p>The type of IAM policy.</p> <ul> <li> <p> <code>NONE</code>: The resource does not use an IAM policy. This is the default.</p> </li> <li> <p> <code>AWS_IAM</code>: The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the service network.</p>"""
    sharing_config: NotRequired[
        "aws_sdk_vpc_lattice.types.sharing_config.SharingConfig"
    ]
    """<p>Specify if the service network should be enabled for sharing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceNetworkRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "auth_type" in value:
        out["authType"] = value["auth_type"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    if "sharing_config" in value:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharingConfig"] = aws_sdk_vpc_lattice.types.sharing_config.serialize_json(
            value["sharing_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateServiceNetworkRequest:
    out: CreateServiceNetworkRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateServiceNetworkRequest.name required")
    if "authType" in data:
        out["auth_type"] = data["authType"]
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    if "sharingConfig" in data:
        import aws_sdk_vpc_lattice.types.sharing_config

        out["sharing_config"] = (
            aws_sdk_vpc_lattice.types.sharing_config.deserialize_json(
                data["sharingConfig"]
            )
        )
    return out
