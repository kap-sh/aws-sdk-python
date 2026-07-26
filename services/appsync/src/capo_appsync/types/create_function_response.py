"""Generated from Smithy shape ``com.amazonaws.appsync#CreateFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.function_configuration


class CreateFunctionResponse(TypedDict, closed=True):
    function_configuration: NotRequired[
        "capo_appsync.types.function_configuration.FunctionConfiguration"
    ]
    """<p>The <code>Function</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFunctionResponse) -> dict:
    out: dict = {}
    if "function_configuration" in value:
        import capo_appsync.types.function_configuration

        out["functionConfiguration"] = (
            capo_appsync.types.function_configuration.serialize_json(
                value["function_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateFunctionResponse:
    out: CreateFunctionResponse = {}  # type: ignore[typeddict-item]
    if "functionConfiguration" in data:
        import capo_appsync.types.function_configuration

        out["function_configuration"] = (
            capo_appsync.types.function_configuration.deserialize_json(
                data["functionConfiguration"]
            )
        )
    return out
