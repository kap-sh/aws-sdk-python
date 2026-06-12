"""Generated from Smithy shape ``com.amazonaws.workspaces#ClientPropertiesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.client_properties
    import aws_sdk_workspaces.types.non_empty_string


class ClientPropertiesResult(TypedDict):
    resource_id: NotRequired["aws_sdk_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The resource identifier, in the form of a directory ID.</p>"""
    client_properties: NotRequired[
        "aws_sdk_workspaces.types.client_properties.ClientProperties"
    ]
    """<p>Information about the Amazon WorkSpaces client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientPropertiesResult) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "client_properties" in value:
        import aws_sdk_workspaces.types.client_properties

        out["ClientProperties"] = (
            aws_sdk_workspaces.types.client_properties.serialize_aws_json_1_1(
                value["client_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientPropertiesResult:
    out: ClientPropertiesResult = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ClientProperties" in data:
        import aws_sdk_workspaces.types.client_properties

        out["client_properties"] = (
            aws_sdk_workspaces.types.client_properties.deserialize_aws_json_1_1(
                data["ClientProperties"]
            )
        )
    return out
