"""Generated from Smithy shape ``com.amazonaws.glue#GetSecurityConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.security_configuration_list


class GetSecurityConfigurationsResponse(TypedDict):
    security_configurations: NotRequired[
        "aws_sdk_glue.types.security_configuration_list.SecurityConfigurationList"
    ]
    """<p>A list of security configurations.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if there are more security configurations to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSecurityConfigurationsResponse) -> dict:
    out: dict = {}
    if "security_configurations" in value:
        import aws_sdk_glue.types.security_configuration_list

        out["SecurityConfigurations"] = (
            aws_sdk_glue.types.security_configuration_list.serialize_aws_json_1_1(
                value["security_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSecurityConfigurationsResponse:
    out: GetSecurityConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "SecurityConfigurations" in data:
        import aws_sdk_glue.types.security_configuration_list

        out["security_configurations"] = (
            aws_sdk_glue.types.security_configuration_list.deserialize_aws_json_1_1(
                data["SecurityConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
