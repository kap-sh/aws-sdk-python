"""Generated from Smithy shape ``com.amazonaws.workmail#ListAvailabilityConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.availability_configuration_list
    import aws_sdk_workmail.types.next_token


class ListAvailabilityConfigurationsResponse(TypedDict):
    availability_configurations: NotRequired[
        "aws_sdk_workmail.types.availability_configuration_list.AvailabilityConfigurationList"
    ]
    """<p>The list of <code>AvailabilityConfiguration</code>'s that exist for the specified WorkMail organization.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The value is <code>null</code> when there are no further results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailabilityConfigurationsResponse) -> dict:
    out: dict = {}
    if "availability_configurations" in value:
        import aws_sdk_workmail.types.availability_configuration_list

        out["AvailabilityConfigurations"] = (
            aws_sdk_workmail.types.availability_configuration_list.serialize_aws_json_1_1(
                value["availability_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailabilityConfigurationsResponse:
    out: ListAvailabilityConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "AvailabilityConfigurations" in data:
        import aws_sdk_workmail.types.availability_configuration_list

        out["availability_configurations"] = (
            aws_sdk_workmail.types.availability_configuration_list.deserialize_aws_json_1_1(
                data["AvailabilityConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
