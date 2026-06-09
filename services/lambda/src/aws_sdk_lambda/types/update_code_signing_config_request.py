"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.allowed_publishers
    import aws_sdk_lambda.types.code_signing_config_arn
    import aws_sdk_lambda.types.code_signing_policies
    import aws_sdk_lambda.types.description


class UpdateCodeSigningConfigRequest(TypedDict):
    code_signing_config_arn: (
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>Descriptive name for this code signing configuration.</p>"""
    allowed_publishers: NotRequired[
        "aws_sdk_lambda.types.allowed_publishers.AllowedPublishers"
    ]
    """<p>Signing profiles for this code signing configuration.</p>"""
    code_signing_policies: NotRequired[
        "aws_sdk_lambda.types.code_signing_policies.CodeSigningPolicies"
    ]
    """<p>The code signing policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSigningConfigRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "allowed_publishers" in value:
        import aws_sdk_lambda.types.allowed_publishers

        out["AllowedPublishers"] = (
            aws_sdk_lambda.types.allowed_publishers.serialize_json(
                value["allowed_publishers"]
            )
        )
    if "code_signing_policies" in value:
        import aws_sdk_lambda.types.code_signing_policies

        out["CodeSigningPolicies"] = (
            aws_sdk_lambda.types.code_signing_policies.serialize_json(
                value["code_signing_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCodeSigningConfigRequest:
    out: UpdateCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AllowedPublishers" in data:
        import aws_sdk_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            aws_sdk_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    if "CodeSigningPolicies" in data:
        import aws_sdk_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            aws_sdk_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    return out
