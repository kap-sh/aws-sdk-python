"""Generated from Smithy shape ``com.amazonaws.kendra#ListAccessControlConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.access_control_configuration_summary_list
    import aws_sdk_kendra.types.string


class ListAccessControlConfigurationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_kendra.types.string.String"]
    """<p>If the response is truncated, Amazon Kendra returns this token, which you can use in the subsequent request to retrieve the next set of access control configurations.</p>"""
    access_control_configurations: "aws_sdk_kendra.types.access_control_configuration_summary_list.AccessControlConfigurationSummaryList"
    """<p>The details of your access control configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAccessControlConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_kendra.types.access_control_configuration_summary_list

    out["AccessControlConfigurations"] = (
        aws_sdk_kendra.types.access_control_configuration_summary_list.serialize_aws_json_1_1(
            value["access_control_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAccessControlConfigurationsResponse:
    out: ListAccessControlConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "AccessControlConfigurations" in data:
        import aws_sdk_kendra.types.access_control_configuration_summary_list

        out["access_control_configurations"] = (
            aws_sdk_kendra.types.access_control_configuration_summary_list.deserialize_aws_json_1_1(
                data["AccessControlConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListAccessControlConfigurationsResponse.access_control_configurations required"
        )
    return out
