"""Generated from Smithy shape ``com.amazonaws.lambda#CodeSigningConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.allowed_publishers
    import capo_lambda.types.code_signing_config_arn
    import capo_lambda.types.code_signing_config_id
    import capo_lambda.types.code_signing_policies
    import capo_lambda.types.description
    import capo_lambda.types.timestamp


class CodeSigningConfig(TypedDict, closed=True):
    code_signing_config_id: (
        "capo_lambda.types.code_signing_config_id.CodeSigningConfigId"
    )
    """<p>Unique identifer for the Code signing configuration.</p>"""
    code_signing_config_arn: (
        "capo_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Code signing configuration.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>Code signing configuration description.</p>"""
    allowed_publishers: "capo_lambda.types.allowed_publishers.AllowedPublishers"
    """<p>List of allowed publishers.</p>"""
    code_signing_policies: "capo_lambda.types.code_signing_policies.CodeSigningPolicies"
    """<p>The code signing policy controls the validation failure action for signature mismatch or expiry.</p>"""
    last_modified: "capo_lambda.types.timestamp.Timestamp"
    """<p>The date and time that the Code signing configuration was last modified, in ISO-8601 format (YYYY-MM-DDThh:mm:ss.sTZD). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSigningConfig) -> dict:
    out: dict = {}
    out["CodeSigningConfigId"] = value["code_signing_config_id"]
    out["CodeSigningConfigArn"] = value["code_signing_config_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_lambda.types.allowed_publishers

    out["AllowedPublishers"] = capo_lambda.types.allowed_publishers.serialize_json(
        value["allowed_publishers"]
    )
    import capo_lambda.types.code_signing_policies

    out["CodeSigningPolicies"] = capo_lambda.types.code_signing_policies.serialize_json(
        value["code_signing_policies"]
    )
    out["LastModified"] = value["last_modified"]
    return out


def deserialize_json(data: dict) -> CodeSigningConfig:
    out: CodeSigningConfig = {}  # type: ignore[typeddict-item]
    if "CodeSigningConfigId" in data:
        out["code_signing_config_id"] = data["CodeSigningConfigId"]
    else:
        raise DeserializationError("CodeSigningConfig.code_signing_config_id required")
    if "CodeSigningConfigArn" in data:
        out["code_signing_config_arn"] = data["CodeSigningConfigArn"]
    else:
        raise DeserializationError("CodeSigningConfig.code_signing_config_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "AllowedPublishers" in data:
        import capo_lambda.types.allowed_publishers

        out["allowed_publishers"] = (
            capo_lambda.types.allowed_publishers.deserialize_json(
                data["AllowedPublishers"]
            )
        )
    else:
        raise DeserializationError("CodeSigningConfig.allowed_publishers required")
    if "CodeSigningPolicies" in data:
        import capo_lambda.types.code_signing_policies

        out["code_signing_policies"] = (
            capo_lambda.types.code_signing_policies.deserialize_json(
                data["CodeSigningPolicies"]
            )
        )
    else:
        raise DeserializationError("CodeSigningConfig.code_signing_policies required")
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    else:
        raise DeserializationError("CodeSigningConfig.last_modified required")
    return out
