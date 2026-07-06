"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.fleet_context_code
    import aws_sdk_codebuild.types.fleet_status_code
    import aws_sdk_codebuild.types.string


class FleetStatus(TypedDict, closed=True):
    status_code: NotRequired[
        "aws_sdk_codebuild.types.fleet_status_code.FleetStatusCode"
    ]
    """<p>The status code of the compute fleet. Valid values include:</p> <ul> <li> <p> <code>CREATING</code>: The compute fleet is being created.</p> </li> <li> <p> <code>UPDATING</code>: The compute fleet is being updated.</p> </li> <li> <p> <code>ROTATING</code>: The compute fleet is being rotated.</p> </li> <li> <p> <code>PENDING_DELETION</code>: The compute fleet is pending deletion.</p> </li> <li> <p> <code>DELETING</code>: The compute fleet is being deleted.</p> </li> <li> <p> <code>CREATE_FAILED</code>: The compute fleet has failed to create.</p> </li> <li> <p> <code>UPDATE_ROLLBACK_FAILED</code>: The compute fleet has failed to update and could not rollback to previous state.</p> </li> <li> <p> <code>ACTIVE</code>: The compute fleet has succeeded and is active.</p> </li> </ul>"""
    context: NotRequired["aws_sdk_codebuild.types.fleet_context_code.FleetContextCode"]
    """<p>Additional information about a compute fleet. Valid values include:</p> <ul> <li> <p> <code>CREATE_FAILED</code>: The compute fleet has failed to create.</p> </li> <li> <p> <code>UPDATE_FAILED</code>: The compute fleet has failed to update.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>A message associated with the status of a compute fleet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetStatus) -> dict:
    out: dict = {}
    if "status_code" in value:
        import aws_sdk_codebuild.types.fleet_status_code

        out["statusCode"] = (
            aws_sdk_codebuild.types.fleet_status_code.serialize_aws_json_1_1(
                value["status_code"]
            )
        )
    if "context" in value:
        import aws_sdk_codebuild.types.fleet_context_code

        out["context"] = (
            aws_sdk_codebuild.types.fleet_context_code.serialize_aws_json_1_1(
                value["context"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FleetStatus:
    out: FleetStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        import aws_sdk_codebuild.types.fleet_status_code

        out["status_code"] = (
            aws_sdk_codebuild.types.fleet_status_code.deserialize_aws_json_1_1(
                data["statusCode"]
            )
        )
    if "context" in data:
        import aws_sdk_codebuild.types.fleet_context_code

        out["context"] = (
            aws_sdk_codebuild.types.fleet_context_code.deserialize_aws_json_1_1(
                data["context"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
