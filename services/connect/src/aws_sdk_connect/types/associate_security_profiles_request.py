"""Generated from Smithy shape ``com.amazonaws.connect#AssociateSecurityProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.entity_arn
    import aws_sdk_connect.types.entity_type
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.security_profiles


class AssociateSecurityProfilesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p> The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance. </p>"""
    security_profiles: "aws_sdk_connect.types.security_profiles.SecurityProfiles"
    """<p> List of Security Profile Object. </p>"""
    entity_type: "aws_sdk_connect.types.entity_type.EntityType"
    """<p> Only supported type is AI_AGENT. </p>"""
    entity_arn: "aws_sdk_connect.types.entity_arn.EntityArn"
    """<p> Arn of a Q in Connect AI Agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSecurityProfilesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.security_profiles

    out["SecurityProfiles"] = aws_sdk_connect.types.security_profiles.serialize_json(
        value["security_profiles"]
    )
    import aws_sdk_connect.types.entity_type

    out["EntityType"] = aws_sdk_connect.types.entity_type.serialize_json(
        value["entity_type"]
    )
    out["EntityArn"] = value["entity_arn"]
    return out


def deserialize_json(data: dict) -> AssociateSecurityProfilesRequest:
    out: AssociateSecurityProfilesRequest = {}  # type: ignore[typeddict-item]
    if "SecurityProfiles" in data:
        import aws_sdk_connect.types.security_profiles

        out["security_profiles"] = (
            aws_sdk_connect.types.security_profiles.deserialize_json(
                data["SecurityProfiles"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateSecurityProfilesRequest.security_profiles required"
        )
    if "EntityType" in data:
        import aws_sdk_connect.types.entity_type

        out["entity_type"] = aws_sdk_connect.types.entity_type.deserialize_json(
            data["EntityType"]
        )
    else:
        raise DeserializationError(
            "AssociateSecurityProfilesRequest.entity_type required"
        )
    if "EntityArn" in data:
        out["entity_arn"] = data["EntityArn"]
    else:
        raise DeserializationError(
            "AssociateSecurityProfilesRequest.entity_arn required"
        )
    return out
