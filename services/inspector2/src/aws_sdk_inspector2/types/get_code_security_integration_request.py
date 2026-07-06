"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_integration_arn
    import aws_sdk_inspector2.types.tag_map


class GetCodeSecurityIntegrationRequest(TypedDict, closed=True):
    integration_arn: "aws_sdk_inspector2.types.code_security_integration_arn.CodeSecurityIntegrationArn"
    """<p>The Amazon Resource Name (ARN) of the code security integration to retrieve.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCodeSecurityIntegrationRequest:
    out: GetCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "integrationArn" in data:
        out["integration_arn"] = data["integrationArn"]
    else:
        raise DeserializationError(
            "GetCodeSecurityIntegrationRequest.integration_arn required"
        )
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
