"""Generated from Smithy shape ``com.amazonaws.glue#GetBlueprintResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blueprint


class GetBlueprintResponse(TypedDict, closed=True):
    blueprint: NotRequired["capo_glue.types.blueprint.Blueprint"]
    """<p>Returns a <code>Blueprint</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlueprintResponse) -> dict:
    out: dict = {}
    if "blueprint" in value:
        import capo_glue.types.blueprint

        out["Blueprint"] = capo_glue.types.blueprint.serialize_aws_json_1_1(
            value["blueprint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlueprintResponse:
    out: GetBlueprintResponse = {}  # type: ignore[typeddict-item]
    if "Blueprint" in data:
        import capo_glue.types.blueprint

        out["blueprint"] = capo_glue.types.blueprint.deserialize_aws_json_1_1(
            data["Blueprint"]
        )
    return out
