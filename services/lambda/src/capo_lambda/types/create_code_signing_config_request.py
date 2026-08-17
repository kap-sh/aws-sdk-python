"""Generated from Smithy shape ``com.amazonaws.lambda#CreateCodeSigningConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.description
    import capo_lambda.types.tags


class CreateCodeSigningConfigRequest(TypedDict, closed=True):
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>Descriptive name for this code signing configuration.</p>"""
    allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers"
    """<p>Signing profiles for this code signing configuration.</p>"""
    code_signing_policies: NotRequired[
        "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
    ]
    """<p>The code signing policies define the actions to take if the validation checks fail. </p>"""
    tags: NotRequired["capo_lambda.types.tags.Tags"]
    """<p>A list of tags to add to the code signing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSigningConfigRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
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
    if "tags" in value:
        import capo_lambda.types.tags

        out["Tags"] = capo_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCodeSigningConfigRequest:
    out: CreateCodeSigningConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("AllowedPublishers") is not None:
        import capo_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            capo_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeSigningConfigRequest.allowed_publishers required"
        )
    if data.get("CodeSigningPolicies") is not None:
        import capo_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            capo_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    if data.get("Tags") is not None:
        import capo_lambda.types.tags

        out["tags"] = capo_lambda.types.tags.deserialize_json(data["Tags"])
    return out
