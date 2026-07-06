"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdConnectConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.entity_id_prefix
    import aws_sdk_verifiedpermissions.types.issuer
    import aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration
    import aws_sdk_verifiedpermissions.types.open_id_connect_token_selection


class OpenIdConnectConfiguration(TypedDict, closed=True):
    issuer: "aws_sdk_verifiedpermissions.types.issuer.Issuer"
    """<p>The issuer URL of an OIDC identity provider. This URL must have an OIDC discovery endpoint at the path <code>.well-known/openid-configuration</code>.</p>"""
    entity_id_prefix: NotRequired[
        "aws_sdk_verifiedpermissions.types.entity_id_prefix.EntityIdPrefix"
    ]
    """<p>A descriptive string that you want to prefix to user entities from your OIDC identity provider. For example, if you set an <code>entityIdPrefix</code> of <code>MyOIDCProvider</code>, you can reference principals in your policies in the format <code>MyCorp::User::MyOIDCProvider|Carlos</code>.</p>"""
    group_configuration: NotRequired[
        "aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration.OpenIdConnectGroupConfiguration"
    ]
    """<p>The claim in OIDC identity provider tokens that indicates a user's group membership, and the entity type that you want to map it to. For example, this object can map the contents of a <code>groups</code> claim to <code>MyCorp::UserGroup</code>.</p>"""
    token_selection: "aws_sdk_verifiedpermissions.types.open_id_connect_token_selection.OpenIdConnectTokenSelection"
    """<p>The token type that you want to process from your OIDC identity provider. Your policy store can process either identity (ID) or access tokens from a given OIDC identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdConnectConfiguration) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
    if "entity_id_prefix" in value:
        out["entityIdPrefix"] = value["entity_id_prefix"]
    if "group_configuration" in value:
        import aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration

        out["groupConfiguration"] = (
            aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    import aws_sdk_verifiedpermissions.types.open_id_connect_token_selection

    out["tokenSelection"] = (
        aws_sdk_verifiedpermissions.types.open_id_connect_token_selection.serialize_aws_json_1_0(
            value["token_selection"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpenIdConnectConfiguration:
    out: OpenIdConnectConfiguration = {}  # type: ignore[typeddict-item]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("OpenIdConnectConfiguration.issuer required")
    if "entityIdPrefix" in data:
        out["entity_id_prefix"] = data["entityIdPrefix"]
    if "groupConfiguration" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration

        out["group_configuration"] = (
            aws_sdk_verifiedpermissions.types.open_id_connect_group_configuration.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    if "tokenSelection" in data:
        import aws_sdk_verifiedpermissions.types.open_id_connect_token_selection

        out["token_selection"] = (
            aws_sdk_verifiedpermissions.types.open_id_connect_token_selection.deserialize_aws_json_1_0(
                data["tokenSelection"]
            )
        )
    else:
        raise DeserializationError(
            "OpenIdConnectConfiguration.token_selection required"
        )
    return out
