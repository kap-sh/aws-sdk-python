"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.allowed_publishers
    import aws_sdk_lambda.types.code_signing_policies
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.tags


class CreateCodeSigningConfigRequest(TypedDict):
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>Descriptive name for this code signing configuration.</p>"""
    allowed_publishers: "aws_sdk_lambda.types.allowed_publishers.AllowedPublishers"
    """<p>Signing profiles for this code signing configuration.</p>"""
    code_signing_policies: NotRequired[
        "aws_sdk_lambda.types.code_signing_policies.CodeSigningPolicies"
    ]
    """<p>The code signing policies define the actions to take if the validation checks fail. </p>"""
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    """<p>A list of tags to add to the code signing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSigningConfigRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_lambda.types.allowed_publishers

    out["AllowedPublishers"] = aws_sdk_lambda.types.allowed_publishers.serialize_json(
        value["allowed_publishers"]
    )
    if "code_signing_policies" in value:
        import aws_sdk_lambda.types.code_signing_policies

        out["CodeSigningPolicies"] = (
            aws_sdk_lambda.types.code_signing_policies.serialize_json(
                value["code_signing_policies"]
            )
        )
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCodeSigningConfigRequest:
    out: CreateCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "AllowedPublishers" in data:
        import aws_sdk_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            aws_sdk_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeSigningConfigRequest.allowed_publishers required"
        )
    if "CodeSigningPolicies" in data:
        import aws_sdk_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            aws_sdk_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    return out
