"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.blueprint_run


class GetBlueprintRunResponse(TypedDict):
    blueprint_run: NotRequired["aws_sdk_glue.types.blueprint_run.BlueprintRun"]
    """<p>Returns a <code>BlueprintRun</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintRunResponse) -> dict:
    out: dict = {}
    if "blueprint_run" in value:
        import aws_sdk_glue.types.blueprint_run

        out["BlueprintRun"] = aws_sdk_glue.types.blueprint_run.serialize_aws_json_1_1(
            value["blueprint_run"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintRunResponse:
    out: GetBlueprintRunResponse = {}  # type: ignore[typeddict-item]
    if "BlueprintRun" in data:
        import aws_sdk_glue.types.blueprint_run

        out["blueprint_run"] = (
            aws_sdk_glue.types.blueprint_run.deserialize_aws_json_1_1(
                data["BlueprintRun"]
            )
        )
    return out
