"""Generated from Smithy shape ``com.amazonaws.imagebuilder#StartResourceStateUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.date_time_timestamp
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.resource_state
    import aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules
    import aws_sdk_imagebuilder.types.resource_state_update_include_resources
    import aws_sdk_imagebuilder.types.role_name_or_arn


class StartResourceStateUpdateRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Image Builder resource that is updated. The state update might also impact associated resources.</p>"""
    state: "aws_sdk_imagebuilder.types.resource_state.ResourceState"
    """<p>Indicates the lifecycle action to take for this request.</p>"""
    execution_role: NotRequired[
        "aws_sdk_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that’s used to update image state.</p>"""
    include_resources: NotRequired[
        "aws_sdk_imagebuilder.types.resource_state_update_include_resources.ResourceStateUpdateIncludeResources"
    ]
    """<p>A list of image resources to update state for.</p>"""
    exclusion_rules: NotRequired[
        "aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules.ResourceStateUpdateExclusionRules"
    ]
    """<p>Skip action on the image resource and associated resources if specified exclusion rules are met.</p>"""
    update_at: NotRequired[
        "aws_sdk_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The timestamp that indicates when resources are updated by a lifecycle action.</p>"""
    client_token: "aws_sdk_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartResourceStateUpdateRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import aws_sdk_imagebuilder.types.resource_state

    out["state"] = aws_sdk_imagebuilder.types.resource_state.serialize_json(
        value["state"]
    )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "include_resources" in value:
        import aws_sdk_imagebuilder.types.resource_state_update_include_resources

        out["includeResources"] = (
            aws_sdk_imagebuilder.types.resource_state_update_include_resources.serialize_json(
                value["include_resources"]
            )
        )
    if "exclusion_rules" in value:
        import aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules

        out["exclusionRules"] = (
            aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules.serialize_json(
                value["exclusion_rules"]
            )
        )
    if "update_at" in value:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["updateAt"] = aws_sdk_imagebuilder.types.date_time_timestamp.serialize_json(
            value["update_at"]
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartResourceStateUpdateRequest:
    out: StartResourceStateUpdateRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "StartResourceStateUpdateRequest.resource_arn required"
        )
    if "state" in data:
        import aws_sdk_imagebuilder.types.resource_state

        out["state"] = aws_sdk_imagebuilder.types.resource_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("StartResourceStateUpdateRequest.state required")
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "includeResources" in data:
        import aws_sdk_imagebuilder.types.resource_state_update_include_resources

        out["include_resources"] = (
            aws_sdk_imagebuilder.types.resource_state_update_include_resources.deserialize_json(
                data["includeResources"]
            )
        )
    if "exclusionRules" in data:
        import aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules

        out["exclusion_rules"] = (
            aws_sdk_imagebuilder.types.resource_state_update_exclusion_rules.deserialize_json(
                data["exclusionRules"]
            )
        )
    if "updateAt" in data:
        import aws_sdk_imagebuilder.types.date_time_timestamp

        out["update_at"] = (
            aws_sdk_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["updateAt"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "StartResourceStateUpdateRequest.client_token required"
        )
    return out
