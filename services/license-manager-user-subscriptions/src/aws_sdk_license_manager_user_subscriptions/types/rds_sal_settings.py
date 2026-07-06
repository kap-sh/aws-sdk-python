"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#RdsSalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.credentials_provider


class RdsSalSettings(TypedDict, closed=True):
    rds_sal_credentials_provider: "aws_sdk_license_manager_user_subscriptions.types.credentials_provider.CredentialsProvider"
    """<p>The <code>CredentialsProvider</code> resource contains a reference to the credentials provider that's used for RDS license server user administration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsSalSettings) -> dict:
    out: dict = {}
    import aws_sdk_license_manager_user_subscriptions.types.credentials_provider

    out["RdsSalCredentialsProvider"] = (
        aws_sdk_license_manager_user_subscriptions.types.credentials_provider.serialize_json(
            value["rds_sal_credentials_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> RdsSalSettings:
    out: RdsSalSettings = {}  # type: ignore[typeddict-item]
    if "RdsSalCredentialsProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.credentials_provider

        out["rds_sal_credentials_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.credentials_provider.deserialize_json(
                data["RdsSalCredentialsProvider"]
            )
        )
    else:
        raise DeserializationError(
            "RdsSalSettings.rds_sal_credentials_provider required"
        )
    return out
