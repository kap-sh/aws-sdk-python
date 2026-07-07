"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityIntegrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_inspector2.types.authorization_url
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.integration_name
    import aws_sdk_inspector2.types.integration_status
    import aws_sdk_inspector2.types.integration_type
    import aws_sdk_inspector2.types.tag_map


class GetCodeSecurityIntegrationResponse(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the code security integration.</p>"""
    name: "aws_sdk_inspector2.types.integration_name.IntegrationName"
    """<p>The name of the code security integration.</p>"""
    type: "aws_sdk_inspector2.types.integration_type.IntegrationType"
    """<p>The type of repository provider for the integration.</p>"""
    status: "aws_sdk_inspector2.types.integration_status.IntegrationStatus"
    """<p>The current status of the code security integration.</p>"""
    status_reason: "str"
    """<p>The reason for the current status of the code security integration.</p>"""
    created_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was created.</p>"""
    last_update_on: "datetime.datetime"
    """<p>The timestamp when the code security integration was last updated.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the code security integration.</p>"""
    authorization_url: NotRequired[
        "aws_sdk_inspector2.types.authorization_url.AuthorizationUrl"
    ]
    """<p>The URL used to authorize the integration with the repository provider. This is only returned if reauthorization is required to fix a connection issue. Otherwise, it is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityIntegrationResponse) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    out["name"] = value["name"]
    import aws_sdk_inspector2.types.integration_type

    out["type"] = aws_sdk_inspector2.types.integration_type.serialize_json(
        value["type"]
    )
    import aws_sdk_inspector2.types.integration_status

    out["status"] = aws_sdk_inspector2.types.integration_status.serialize_json(
        value["status"]
    )
    out["statusReason"] = value["status_reason"]
    import aws_sdk_inspector2.types._prelude.timestamp

    out["createdOn"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
        value["created_on"]
    )
    import aws_sdk_inspector2.types._prelude.timestamp

    out["lastUpdateOn"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
        value["last_update_on"]
    )
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> GetCodeSecurityIntegrationResponse:
    out: GetCodeSecurityIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.integration_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.name required")
    if "type" in data:
        import aws_sdk_inspector2.types.integration_type

        out["type"] = aws_sdk_inspector2.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.type required")
    if "status" in data:
        import aws_sdk_inspector2.types.integration_status

        out["status"] = aws_sdk_inspector2.types.integration_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetCodeSecurityIntegrationResponse.status required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.status_reason required"
        )
    if "createdOn" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["created_on"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["createdOn"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.created_on required"
        )
    if "lastUpdateOn" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["last_update_on"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastUpdateOn"]
            )
        )
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationResponse.last_update_on required"
        )
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    return out
