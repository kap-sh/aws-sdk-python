"""Generated from Smithy shape ``com.amazonaws.mediatailor#CustomOutputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__map_of__string
    import aws_sdk_mediatailor.types.runtime_type


class CustomOutputConfiguration(TypedDict):
    runtime: "aws_sdk_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. Set this to <code>JSONata</code>.</p>"""
    output: NotRequired["aws_sdk_mediatailor.types.__map_of__string.__mapOf__string"]
    r"""<p>A map of output bindings. Each key is a namespaced output path (such as <code>player_params.device_type</code> or <code>temp.variant</code>), and each value is an expression that MediaTailor evaluates at runtime against the current session state. For more information about expression syntax, see <a href=\"https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html\">JSONata expression reference</a> in the <i>MediaTailor User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomOutputConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_mediatailor.types.runtime_type

    out["Runtime"] = aws_sdk_mediatailor.types.runtime_type.serialize_json(
        value["runtime"]
    )
    if "output" in value:
        import aws_sdk_mediatailor.types.__map_of__string

        out["Output"] = aws_sdk_mediatailor.types.__map_of__string.serialize_json(
            value["output"]
        )
    return out


def deserialize_json(data: dict) -> CustomOutputConfiguration:
    out: CustomOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "Runtime" in data:
        import aws_sdk_mediatailor.types.runtime_type

        out["runtime"] = aws_sdk_mediatailor.types.runtime_type.deserialize_json(
            data["Runtime"]
        )
    else:
        raise DeserializationError("CustomOutputConfiguration.runtime required")
    if "Output" in data:
        import aws_sdk_mediatailor.types.__map_of__string

        out["output"] = aws_sdk_mediatailor.types.__map_of__string.deserialize_json(
            data["Output"]
        )
    return out
