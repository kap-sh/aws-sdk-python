"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails(
    TypedDict, closed=True
):
    assign_public_ip: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Whether the task's elastic network interface receives a public IP address. The default value is <code>DISABLED</code>.</p> <p>Valid values: <code>ENABLED</code> | <code>DISABLED</code> </p>"""
    security_groups: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The IDs of the security groups associated with the task or service.</p> <p>You can provide up to five security groups.</p>"""
    subnets: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The IDs of the subnets associated with the task or service.</p> <p>You can provide up to 16 subnets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails,
) -> dict:
    out: dict = {}
    if "assign_public_ip" in value:
        out["AssignPublicIp"] = value["assign_public_ip"]
    if "security_groups" in value:
        import capo_securityhub.types.non_empty_string_list

        out["SecurityGroups"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["security_groups"]
            )
        )
    if "subnets" in value:
        import capo_securityhub.types.non_empty_string_list

        out["Subnets"] = capo_securityhub.types.non_empty_string_list.serialize_json(
            value["subnets"]
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails:
    out: AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "AssignPublicIp" in data:
        out["assign_public_ip"] = data["AssignPublicIp"]
    if "SecurityGroups" in data:
        import capo_securityhub.types.non_empty_string_list

        out["security_groups"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroups"]
            )
        )
    if "Subnets" in data:
        import capo_securityhub.types.non_empty_string_list

        out["subnets"] = capo_securityhub.types.non_empty_string_list.deserialize_json(
            data["Subnets"]
        )
    return out
