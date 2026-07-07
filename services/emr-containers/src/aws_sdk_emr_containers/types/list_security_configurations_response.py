"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListSecurityConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.next_token
    import aws_sdk_emr_containers.types.security_configurations


class ListSecurityConfigurationsResponse(TypedDict, closed=True):
    security_configurations: NotRequired[
        "aws_sdk_emr_containers.types.security_configurations.SecurityConfigurations"
    ]
    """<p>The list of returned security configurations.</p>"""
    next_token: NotRequired["aws_sdk_emr_containers.types.next_token.NextToken"]
    """<p>The token for the next set of security configurations to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityConfigurationsResponse) -> dict:
    out: dict = {}
    if "security_configurations" in value:
        import aws_sdk_emr_containers.types.security_configurations

        out["securityConfigurations"] = (
            aws_sdk_emr_containers.types.security_configurations.serialize_json(
                value["security_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityConfigurationsResponse:
    out: ListSecurityConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "securityConfigurations" in data:
        import aws_sdk_emr_containers.types.security_configurations

        out["security_configurations"] = (
            aws_sdk_emr_containers.types.security_configurations.deserialize_json(
                data["securityConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
