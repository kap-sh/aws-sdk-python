"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateDomainInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.create_web_app_configuration
    import aws_sdk_connecthealth.types.domain_name
    import aws_sdk_connecthealth.types.kms_key_arn
    import aws_sdk_connecthealth.types.tag_map


class CreateDomainInput(TypedDict):
    name: "aws_sdk_connecthealth.types.domain_name.DomainName"
    """<p>The name for the new Domain.</p>"""
    kms_key_arn: NotRequired["aws_sdk_connecthealth.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key to use for encrypting data in this Domain.</p>"""
    web_app_setup_configuration: NotRequired[
        "aws_sdk_connecthealth.types.create_web_app_configuration.CreateWebAppConfiguration"
    ]
    """<p>Configuration for the Domain web application. Optional, but if provided all fields are required.</p>"""
    tags: NotRequired["aws_sdk_connecthealth.types.tag_map.TagMap"]
    """<p>Tags to associate with the Domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDomainInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "web_app_setup_configuration" in value:
        import aws_sdk_connecthealth.types.create_web_app_configuration

        out["webAppSetupConfiguration"] = (
            aws_sdk_connecthealth.types.create_web_app_configuration.serialize_json(
                value["web_app_setup_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_connecthealth.types.tag_map

        out["tags"] = aws_sdk_connecthealth.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDomainInput:
    out: CreateDomainInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDomainInput.name required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "webAppSetupConfiguration" in data:
        import aws_sdk_connecthealth.types.create_web_app_configuration

        out["web_app_setup_configuration"] = (
            aws_sdk_connecthealth.types.create_web_app_configuration.deserialize_json(
                data["webAppSetupConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_connecthealth.types.tag_map

        out["tags"] = aws_sdk_connecthealth.types.tag_map.deserialize_json(data["tags"])
    return out
