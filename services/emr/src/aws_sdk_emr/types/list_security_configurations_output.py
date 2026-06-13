"""Generated from Smithy shape ``com.amazonaws.emr#ListSecurityConfigurationsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.security_configuration_list


class ListSecurityConfigurationsOutput(TypedDict):
    security_configurations: NotRequired[
        "aws_sdk_emr.types.security_configuration_list.SecurityConfigurationList"
    ]
    """<p>The creation date and time, and name, of each security configuration.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>A pagination token that indicates the next set of results to retrieve. Include the marker in the next ListSecurityConfiguration call to retrieve the next page of results, if required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecurityConfigurationsOutput) -> dict:
    out: dict = {}
    if "security_configurations" in value:
        import aws_sdk_emr.types.security_configuration_list

        out["SecurityConfigurations"] = (
            aws_sdk_emr.types.security_configuration_list.serialize_aws_json_1_1(
                value["security_configurations"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecurityConfigurationsOutput:
    out: ListSecurityConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "SecurityConfigurations" in data:
        import aws_sdk_emr.types.security_configuration_list

        out["security_configurations"] = (
            aws_sdk_emr.types.security_configuration_list.deserialize_aws_json_1_1(
                data["SecurityConfigurations"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
