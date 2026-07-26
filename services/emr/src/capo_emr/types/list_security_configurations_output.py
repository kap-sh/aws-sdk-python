"""Generated from Smithy shape ``com.amazonaws.emr#ListSecurityConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.marker
    import capo_emr.types.security_configuration_list


class ListSecurityConfigurationsOutput(TypedDict, closed=True):
    security_configurations: NotRequired[
        "capo_emr.types.security_configuration_list.SecurityConfigurationList"
    ]
    """<p>The creation date and time, and name, of each security configuration.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>A pagination token that indicates the next set of results to retrieve. Include the marker in the next ListSecurityConfiguration call to retrieve the next page of results, if required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecurityConfigurationsOutput) -> dict:
    out: dict = {}
    if "security_configurations" in value:
        import capo_emr.types.security_configuration_list

        out["SecurityConfigurations"] = (
            capo_emr.types.security_configuration_list.serialize_aws_json_1_1(
                value["security_configurations"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecurityConfigurationsOutput:
    out: ListSecurityConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "SecurityConfigurations" in data:
        import capo_emr.types.security_configuration_list

        out["security_configurations"] = (
            capo_emr.types.security_configuration_list.deserialize_aws_json_1_1(
                data["SecurityConfigurations"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
