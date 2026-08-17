"""Generated from Smithy shape ``com.amazonaws.lambda#ImageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.string_list
    import capo_lambda.types.working_directory


class ImageConfig(TypedDict, closed=True):
    entry_point: NotRequired["capo_lambda.types.string_list.StringList"]
    """<p>Specifies the entry point to their application, which is typically the location of the runtime executable.</p>"""
    command: NotRequired["capo_lambda.types.string_list.StringList"]
    """<p>Specifies parameters that you want to pass in with ENTRYPOINT.</p>"""
    working_directory: NotRequired[
        "capo_lambda.types.working_directory.WorkingDirectory"
    ]
    """<p>Specifies the working directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageConfig) -> dict:
    out: dict = {}
    if "entry_point" in value:
        import capo_lambda.types.string_list

        out["EntryPoint"] = capo_lambda.types.string_list.serialize_json(
            value["entry_point"]
        )
    if "command" in value:
        import capo_lambda.types.string_list

        out["Command"] = capo_lambda.types.string_list.serialize_json(value["command"])
    if "working_directory" in value:
        out["WorkingDirectory"] = value["working_directory"]
    return out


def deserialize_json(data: dict) -> ImageConfig:
    out: ImageConfig = {}  # type: ignore[typeddict-item]
    if data.get("EntryPoint") is not None:
        import capo_lambda.types.string_list

        out["entry_point"] = capo_lambda.types.string_list.deserialize_json(
            data["EntryPoint"]
        )
    if data.get("Command") is not None:
        import capo_lambda.types.string_list

        out["command"] = capo_lambda.types.string_list.deserialize_json(data["Command"])
    if data.get("WorkingDirectory") is not None:
        out["working_directory"] = data["WorkingDirectory"]
    return out
