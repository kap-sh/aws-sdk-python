"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientApplicationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_source_type
    import aws_sdk_quicksight.types.o_auth_client_application_id
    import aws_sdk_quicksight.types.o_auth_client_authentication_type
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.vpc_connection_properties


class OAuthClientApplicationSummary(TypedDict, closed=True):
    o_auth_client_application_id: NotRequired[
        "aws_sdk_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    ]
    """<p>The ID of the OAuthClientApplication. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.resource_name.ResourceName"]
    """<p>The display name of the OAuthClientApplication.</p>"""
    o_auth_client_authentication_type: NotRequired[
        "aws_sdk_quicksight.types.o_auth_client_authentication_type.OAuthClientAuthenticationType"
    ]
    """<p>The OAuth client authentication type used by the OAuthClientApplication. Valid values are <code>TOKEN</code>.</p>"""
    data_source_type: NotRequired[
        "aws_sdk_quicksight.types.data_source_type.DataSourceType"
    ]
    """<p>The type of data source that the OAuthClientApplication is used with. Valid values are <code>SNOWFLAKE</code>.</p>"""
    identity_provider_vpc_connection_properties: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the OAuthClientApplication was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the OAuthClientApplication was last updated.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the OAuthClientApplication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthClientApplicationSummary) -> dict:
    out: dict = {}
    if "o_auth_client_application_id" in value:
        out["OAuthClientApplicationId"] = value["o_auth_client_application_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "o_auth_client_authentication_type" in value:
        import aws_sdk_quicksight.types.o_auth_client_authentication_type

        out["OAuthClientAuthenticationType"] = (
            aws_sdk_quicksight.types.o_auth_client_authentication_type.serialize_json(
                value["o_auth_client_authentication_type"]
            )
        )
    if "data_source_type" in value:
        import aws_sdk_quicksight.types.data_source_type

        out["DataSourceType"] = (
            aws_sdk_quicksight.types.data_source_type.serialize_json(
                value["data_source_type"]
            )
        )
    if "identity_provider_vpc_connection_properties" in value:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["IdentityProviderVpcConnectionProperties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.serialize_json(
                value["identity_provider_vpc_connection_properties"]
            )
        )
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> OAuthClientApplicationSummary:
    out: OAuthClientApplicationSummary = {}  # type: ignore[typeddict-item]
    if "OAuthClientApplicationId" in data:
        out["o_auth_client_application_id"] = data["OAuthClientApplicationId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OAuthClientAuthenticationType" in data:
        import aws_sdk_quicksight.types.o_auth_client_authentication_type

        out["o_auth_client_authentication_type"] = (
            aws_sdk_quicksight.types.o_auth_client_authentication_type.deserialize_json(
                data["OAuthClientAuthenticationType"]
            )
        )
    if "DataSourceType" in data:
        import aws_sdk_quicksight.types.data_source_type

        out["data_source_type"] = (
            aws_sdk_quicksight.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "IdentityProviderVpcConnectionProperties" in data:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["identity_provider_vpc_connection_properties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.deserialize_json(
                data["IdentityProviderVpcConnectionProperties"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
