"""Generated from Smithy shape ``com.amazonaws.synthetics#EngineConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.browser_type
    import aws_sdk_synthetics.types.function_arn


class EngineConfig(TypedDict, closed=True):
    engine_arn: NotRequired["aws_sdk_synthetics.types.function_arn.FunctionArn"]
    """<p>Each engine configuration contains the ARN of the Lambda function that is used as the canary's engine for a specific browser type. </p>"""
    browser_type: NotRequired["aws_sdk_synthetics.types.browser_type.BrowserType"]
    """<p>The browser type associated with this engine configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineConfig) -> dict:
    out: dict = {}
    if "engine_arn" in value:
        out["EngineArn"] = value["engine_arn"]
    if "browser_type" in value:
        import aws_sdk_synthetics.types.browser_type

        out["BrowserType"] = aws_sdk_synthetics.types.browser_type.serialize_json(
            value["browser_type"]
        )
    return out


def deserialize_json(data: dict) -> EngineConfig:
    out: EngineConfig = {}  # type: ignore[typeddict-item]
    if "EngineArn" in data:
        out["engine_arn"] = data["EngineArn"]
    if "BrowserType" in data:
        import aws_sdk_synthetics.types.browser_type

        out["browser_type"] = aws_sdk_synthetics.types.browser_type.deserialize_json(
            data["BrowserType"]
        )
    return out
