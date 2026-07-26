"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskExceptionConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.blocked_ip_range_list_type
    import capo_cognito_identity_provider.types.skipped_ip_range_list_type


class RiskExceptionConfigurationType(TypedDict, closed=True):
    blocked_ip_range_list: NotRequired[
        "capo_cognito_identity_provider.types.blocked_ip_range_list_type.BlockedIPRangeListType"
    ]
    """<p>An always-block IP address list. Overrides the risk decision and always blocks authentication requests. This parameter is displayed and set in CIDR notation.</p>"""
    skipped_ip_range_list: NotRequired[
        "capo_cognito_identity_provider.types.skipped_ip_range_list_type.SkippedIPRangeListType"
    ]
    """<p>An always-allow IP address list. Risk detection isn't performed on the IP addresses in this range list. This parameter is displayed and set in CIDR notation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RiskExceptionConfigurationType) -> dict:
    out: dict = {}
    if "blocked_ip_range_list" in value:
        import capo_cognito_identity_provider.types.blocked_ip_range_list_type

        out["BlockedIPRangeList"] = (
            capo_cognito_identity_provider.types.blocked_ip_range_list_type.serialize_aws_json_1_1(
                value["blocked_ip_range_list"]
            )
        )
    if "skipped_ip_range_list" in value:
        import capo_cognito_identity_provider.types.skipped_ip_range_list_type

        out["SkippedIPRangeList"] = (
            capo_cognito_identity_provider.types.skipped_ip_range_list_type.serialize_aws_json_1_1(
                value["skipped_ip_range_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RiskExceptionConfigurationType:
    out: RiskExceptionConfigurationType = {}  # type: ignore[typeddict-item]
    if "BlockedIPRangeList" in data:
        import capo_cognito_identity_provider.types.blocked_ip_range_list_type

        out["blocked_ip_range_list"] = (
            capo_cognito_identity_provider.types.blocked_ip_range_list_type.deserialize_aws_json_1_1(
                data["BlockedIPRangeList"]
            )
        )
    if "SkippedIPRangeList" in data:
        import capo_cognito_identity_provider.types.skipped_ip_range_list_type

        out["skipped_ip_range_list"] = (
            capo_cognito_identity_provider.types.skipped_ip_range_list_type.deserialize_aws_json_1_1(
                data["SkippedIPRangeList"]
            )
        )
    return out
