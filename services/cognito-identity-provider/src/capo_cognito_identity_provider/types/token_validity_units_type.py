"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#TokenValidityUnitsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.time_units_type


class TokenValidityUnitsType(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.time_units_type.TimeUnitsType"
    ]
    """<p> A time unit for the value that you set in the <code>AccessTokenValidity</code> parameter. The default <code>AccessTokenValidity</code> time unit is <code>hours</code>. <code>AccessTokenValidity</code> duration can range from five minutes to one day.</p>"""
    id_token: NotRequired[
        "capo_cognito_identity_provider.types.time_units_type.TimeUnitsType"
    ]
    """<p>A time unit for the value that you set in the <code>IdTokenValidity</code> parameter. The default <code>IdTokenValidity</code> time unit is <code>hours</code>. <code>IdTokenValidity</code> duration can range from five minutes to one day.</p>"""
    refresh_token: NotRequired[
        "capo_cognito_identity_provider.types.time_units_type.TimeUnitsType"
    ]
    """<p>A time unit for the value that you set in the <code>RefreshTokenValidity</code> parameter. The default <code>RefreshTokenValidity</code> time unit is <code>days</code>. <code>RefreshTokenValidity</code> duration can range from 60 minutes to 10 years.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TokenValidityUnitsType) -> dict:
    out: dict = {}
    if "access_token" in value:
        import capo_cognito_identity_provider.types.time_units_type

        out["AccessToken"] = (
            capo_cognito_identity_provider.types.time_units_type.serialize_aws_json_1_1(
                value["access_token"]
            )
        )
    if "id_token" in value:
        import capo_cognito_identity_provider.types.time_units_type

        out["IdToken"] = (
            capo_cognito_identity_provider.types.time_units_type.serialize_aws_json_1_1(
                value["id_token"]
            )
        )
    if "refresh_token" in value:
        import capo_cognito_identity_provider.types.time_units_type

        out["RefreshToken"] = (
            capo_cognito_identity_provider.types.time_units_type.serialize_aws_json_1_1(
                value["refresh_token"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TokenValidityUnitsType:
    out: TokenValidityUnitsType = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        import capo_cognito_identity_provider.types.time_units_type

        out["access_token"] = (
            capo_cognito_identity_provider.types.time_units_type.deserialize_aws_json_1_1(
                data["AccessToken"]
            )
        )
    if "IdToken" in data:
        import capo_cognito_identity_provider.types.time_units_type

        out["id_token"] = (
            capo_cognito_identity_provider.types.time_units_type.deserialize_aws_json_1_1(
                data["IdToken"]
            )
        )
    if "RefreshToken" in data:
        import capo_cognito_identity_provider.types.time_units_type

        out["refresh_token"] = (
            capo_cognito_identity_provider.types.time_units_type.deserialize_aws_json_1_1(
                data["RefreshToken"]
            )
        )
    return out
