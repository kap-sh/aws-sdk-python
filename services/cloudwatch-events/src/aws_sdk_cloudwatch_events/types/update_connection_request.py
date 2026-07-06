"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.connection_authorization_type
    import aws_sdk_cloudwatch_events.types.connection_description
    import aws_sdk_cloudwatch_events.types.connection_name
    import aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters


class UpdateConnectionRequest(TypedDict, closed=True):
    name: "aws_sdk_cloudwatch_events.types.connection_name.ConnectionName"
    """<p>The name of the connection to update.</p>"""
    description: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_description.ConnectionDescription"
    ]
    """<p>A description for the connection.</p>"""
    authorization_type: NotRequired[
        "aws_sdk_cloudwatch_events.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The type of authorization to use for the connection.</p>"""
    auth_parameters: NotRequired[
        "aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters.UpdateConnectionAuthRequestParameters"
    ]
    """<p>The authorization parameters to use for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "authorization_type" in value:
        import aws_sdk_cloudwatch_events.types.connection_authorization_type

        out["AuthorizationType"] = (
            aws_sdk_cloudwatch_events.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "auth_parameters" in value:
        import aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters

        out["AuthParameters"] = (
            aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters.serialize_aws_json_1_1(
                value["auth_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionRequest:
    out: UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateConnectionRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "AuthorizationType" in data:
        import aws_sdk_cloudwatch_events.types.connection_authorization_type

        out["authorization_type"] = (
            aws_sdk_cloudwatch_events.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if "AuthParameters" in data:
        import aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters

        out["auth_parameters"] = (
            aws_sdk_cloudwatch_events.types.update_connection_auth_request_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    return out
