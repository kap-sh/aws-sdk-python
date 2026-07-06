"""Generated from Smithy shape ``com.amazonaws.rum#DeobfuscationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.java_script_source_maps


class DeobfuscationConfiguration(TypedDict, closed=True):
    java_script_source_maps: NotRequired[
        "aws_sdk_rum.types.java_script_source_maps.JavaScriptSourceMaps"
    ]
    """<p> A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeobfuscationConfiguration) -> dict:
    out: dict = {}
    if "java_script_source_maps" in value:
        import aws_sdk_rum.types.java_script_source_maps

        out["JavaScriptSourceMaps"] = (
            aws_sdk_rum.types.java_script_source_maps.serialize_json(
                value["java_script_source_maps"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeobfuscationConfiguration:
    out: DeobfuscationConfiguration = {}  # type: ignore[typeddict-item]
    if "JavaScriptSourceMaps" in data:
        import aws_sdk_rum.types.java_script_source_maps

        out["java_script_source_maps"] = (
            aws_sdk_rum.types.java_script_source_maps.deserialize_json(
                data["JavaScriptSourceMaps"]
            )
        )
    return out
