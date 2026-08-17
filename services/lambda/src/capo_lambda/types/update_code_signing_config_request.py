"""Generated from Smithy shape ``com.amazonaws.lambda#UpdateCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.description


class UpdateCodeSigningConfigRequest(TypedDict, closed=True):
    code_signing_config_arn: (
        "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The The Amazon Resource Name (ARN) of the code signing configuration.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>Descriptive name for this code signing configuration.</p>"""
    allowed_publishers: NotRequired[
        "capo_lambda.types.allowed_publishers.AllowedPublishers"
    ]
    """<p>Signing profiles for this code signing configuration.</p>"""
    code_signing_policies: NotRequired[
        "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
    ]
    """<p>The code signing policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSigningConfigRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "allowed_publishers" in value:
        import capo_lambda.types.allowed_publishers

        out["AllowedPublishers"] = capo_lambda.types.allowed_publishers.serialize_json(
            value["allowed_publishers"]
        )
    if "code_signing_policies" in value:
        import capo_lambda.types.code_signing_policies

        out["CodeSigningPolicies"] = (
            capo_lambda.types.code_signing_policies.serialize_json(
                value["code_signing_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCodeSigningConfigRequest:
    out: UpdateCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AllowedPublishers") is not None:
        import capo_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            capo_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    if data.get("CodeSigningPolicies") is not None:
        import capo_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            capo_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    return out
