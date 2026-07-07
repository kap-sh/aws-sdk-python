"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryCodeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.blueprint_types
    import aws_sdk_synthetics.types.dependencies
    import aws_sdk_synthetics.types.string


class CanaryCodeOutput(TypedDict, closed=True):
    source_location_arn: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>The ARN of the Lambda layer where Synthetics stores the canary script code.</p>"""
    handler: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>The entry point to use for the source code when running the canary.</p> <p>This field is required when you don't specify <code>BlueprintTypes</code> and is not allowed when you specify <code>BlueprintTypes</code>.</p>"""
    blueprint_types: NotRequired[
        "aws_sdk_synthetics.types.blueprint_types.BlueprintTypes"
    ]
    """<p> <code>BlueprintTypes</code> is a list of templates that enable simplified canary creation. You can create canaries for common monitoring scenarios by providing only a JSON configuration file instead of writing custom scripts. The only supported value is <code>multi-checks</code>.</p> <p>Multi-checks monitors HTTP/DNS/SSL/TCP endpoints with built-in authentication schemes (Basic, API Key, OAuth, SigV4) and assertion capabilities. When you specify <code>BlueprintTypes</code>, the Handler field cannot be specified since the blueprint provides a pre-defined entry point.</p> <p> <code>BlueprintTypes</code> is supported only on canaries for syn-nodejs-3.0 runtime or later.</p>"""
    dependencies: NotRequired["aws_sdk_synthetics.types.dependencies.Dependencies"]
    """<p>A list of dependencies that are used for running this canary. The dependencies are specified as a key-value pair, where the key is the type of dependency and the value is the dependency reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryCodeOutput) -> dict:
    out: dict = {}
    if "source_location_arn" in value:
        out["SourceLocationArn"] = value["source_location_arn"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    if "blueprint_types" in value:
        import aws_sdk_synthetics.types.blueprint_types

        out["BlueprintTypes"] = aws_sdk_synthetics.types.blueprint_types.serialize_json(
            value["blueprint_types"]
        )
    if "dependencies" in value:
        import aws_sdk_synthetics.types.dependencies

        out["Dependencies"] = aws_sdk_synthetics.types.dependencies.serialize_json(
            value["dependencies"]
        )
    return out


def deserialize_json(data: dict) -> CanaryCodeOutput:
    out: CanaryCodeOutput = {}  # type: ignore[typeddict-item]
    if "SourceLocationArn" in data:
        out["source_location_arn"] = data["SourceLocationArn"]
    if "Handler" in data:
        out["handler"] = data["Handler"]
    if "BlueprintTypes" in data:
        import aws_sdk_synthetics.types.blueprint_types

        out["blueprint_types"] = (
            aws_sdk_synthetics.types.blueprint_types.deserialize_json(
                data["BlueprintTypes"]
            )
        )
    if "Dependencies" in data:
        import aws_sdk_synthetics.types.dependencies

        out["dependencies"] = aws_sdk_synthetics.types.dependencies.deserialize_json(
            data["Dependencies"]
        )
    return out
