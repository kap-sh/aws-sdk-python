"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreatePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.kms_key_arn
    import aws_sdk_bedrock_agent.types.prompt_arn
    import aws_sdk_bedrock_agent.types.prompt_description
    import aws_sdk_bedrock_agent.types.prompt_id
    import aws_sdk_bedrock_agent.types.prompt_name
    import aws_sdk_bedrock_agent.types.prompt_variant_list
    import aws_sdk_bedrock_agent.types.prompt_variant_name
    import aws_sdk_bedrock_agent.types.version


class CreatePromptResponse(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agent.types.prompt_name.PromptName"
    """<p>The name of the prompt.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>The description of the prompt.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key that you encrypted the prompt with.</p>"""
    default_variant: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_variant_name.PromptVariantName"
    ]
    """<p>The name of the default variant for your prompt.</p>"""
    variants: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_variant_list.PromptVariantList"
    ]
    """<p>A list of objects, each containing details about a variant of the prompt.</p>"""
    id: "aws_sdk_bedrock_agent.types.prompt_id.PromptId"
    """<p>The unique identifier of the prompt.</p>"""
    arn: "aws_sdk_bedrock_agent.types.prompt_arn.PromptArn"
    """<p>The Amazon Resource Name (ARN) of the prompt.</p>"""
    version: "aws_sdk_bedrock_agent.types.version.Version"
    """<p>The version of the prompt. When you create a prompt, the version created is the <code>DRAFT</code> version.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptResponse) -> dict:
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
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["version"] = value["version"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> CreatePromptResponse:
    out: CreatePromptResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePromptResponse.name required")
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
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreatePromptResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreatePromptResponse.arn required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreatePromptResponse.version required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreatePromptResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreatePromptResponse.updated_at required")
    return out
