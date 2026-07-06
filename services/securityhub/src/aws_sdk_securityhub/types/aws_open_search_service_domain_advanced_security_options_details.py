"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details
    import aws_sdk_securityhub.types.boolean


class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Enables fine-grained access control. </p>"""
    internal_user_database_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Enables the internal user database. </p>"""
    master_user_options: NotRequired[
        "aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details.AwsOpenSearchServiceDomainMasterUserOptionsDetails"
    ]
    """<p>Specifies information about the master user of the domain. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "master_user_options" in value:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details

        out["MasterUserOptions"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details.serialize_json(
                value["master_user_options"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails:
    out: AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "InternalUserDatabaseEnabled" in data:
        out["internal_user_database_enabled"] = data["InternalUserDatabaseEnabled"]
    if "MasterUserOptions" in data:
        import aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details

        out["master_user_options"] = (
            aws_sdk_securityhub.types.aws_open_search_service_domain_master_user_options_details.deserialize_json(
                data["MasterUserOptions"]
            )
        )
    return out
