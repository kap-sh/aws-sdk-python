"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetBlueprintsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.blueprint_names
    import capo_glue.types.blueprints


class BatchGetBlueprintsResponse(TypedDict, closed=True):
    blueprints: NotRequired["capo_glue.types.blueprints.Blueprints"]
    """<p>Returns a list of blueprint as a <code>Blueprints</code> object.</p>"""
    missing_blueprints: NotRequired["capo_glue.types.blueprint_names.BlueprintNames"]
    """<p>Returns a list of <code>BlueprintNames</code> that were not found.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetBlueprintsResponse) -> dict:
    out: dict = {}
    if "blueprints" in value:
        import capo_glue.types.blueprints

        out["Blueprints"] = capo_glue.types.blueprints.serialize_aws_json_1_1(
            value["blueprints"]
        )
    if "missing_blueprints" in value:
        import capo_glue.types.blueprint_names

        out["MissingBlueprints"] = (
            capo_glue.types.blueprint_names.serialize_aws_json_1_1(
                value["missing_blueprints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetBlueprintsResponse:
    out: BatchGetBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if "Blueprints" in data:
        import capo_glue.types.blueprints

        out["blueprints"] = capo_glue.types.blueprints.deserialize_aws_json_1_1(
            data["Blueprints"]
        )
    if "MissingBlueprints" in data:
        import capo_glue.types.blueprint_names

        out["missing_blueprints"] = (
            capo_glue.types.blueprint_names.deserialize_aws_json_1_1(
                data["MissingBlueprints"]
            )
        )
    return out
