"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdatePromptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.kms_key_arn
    import aws_sdk_bedrock_agent.types.prompt_description
    import aws_sdk_bedrock_agent.types.prompt_identifier
    import aws_sdk_bedrock_agent.types.prompt_name
    import aws_sdk_bedrock_agent.types.prompt_variant_list
    import aws_sdk_bedrock_agent.types.prompt_variant_name


class UpdatePromptRequest(TypedDict):
    name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName"
    """<p>A name for the prompt.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>A description for the prompt.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key to encrypt the prompt.</p>"""
    default_variant: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
    ]
    r"""<p>The name of the default variant for the prompt. This value must match the <code>name</code> field in the relevant <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PromptVariant.html\">PromptVariant</a> object.</p>"""
    variants: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
    ]
    """<p>A list of objects, each containing details about a variant of the prompt.</p>"""
    prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    """<p>The unique identifier of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePromptRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    if "default_variant" in value:
        out["defaultVariant"] = value["default_variant"]
    if "variants" in value:
        import aws_sdk_bedrock_agent.types.prompt_variant_list

        out["variants"] = (
            aws_sdk_bedrock_agent.types.prompt_variant_list.serialize_json(
                value["variants"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePromptRequest:
    out: UpdatePromptRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePromptRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if "defaultVariant" in data:
        out["default_variant"] = data["defaultVariant"]
    if "variants" in data:
        import aws_sdk_bedrock_agent.types.prompt_variant_list

        out["variants"] = (
            aws_sdk_bedrock_agent.types.prompt_variant_list.deserialize_json(
                data["variants"]
            )
        )
    return out
