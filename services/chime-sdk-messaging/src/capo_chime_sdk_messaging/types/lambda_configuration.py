"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#LambdaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.invocation_type
    import capo_chime_sdk_messaging.types.lambda_function_arn


class LambdaConfiguration(TypedDict, closed=True):
    resource_arn: "capo_chime_sdk_messaging.types.lambda_function_arn.LambdaFunctionArn"
    """<p>The ARN of the Lambda message processing function.</p>"""
    invocation_type: "capo_chime_sdk_messaging.types.invocation_type.InvocationType"
    """<p>Controls how the Lambda function is invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaConfiguration) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_chime_sdk_messaging.types.invocation_type

    out["InvocationType"] = (
        capo_chime_sdk_messaging.types.invocation_type.serialize_json(
            value["invocation_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> LambdaConfiguration:
    out: LambdaConfiguration = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("LambdaConfiguration.resource_arn required")
    if "InvocationType" in data:
        import capo_chime_sdk_messaging.types.invocation_type

        out["invocation_type"] = (
            capo_chime_sdk_messaging.types.invocation_type.deserialize_json(
                data["InvocationType"]
            )
        )
    else:
        raise DeserializationError("LambdaConfiguration.invocation_type required")
    return out
